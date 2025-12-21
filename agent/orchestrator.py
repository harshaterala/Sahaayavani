from google import genai
import re
import os

from memory.session_memory import memory
from tools.eligibility import check_eligibility
from tools.scheme_kb import get_scheme_details


# =========================
# GEMINI CLIENT SETUP
# =========================
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_ID = "models/gemini-flash-lite-latest"


# =========================
# TELUGU NUMBER SUPPORT
# =========================
TELUGU_ONES = {
    "ఒకటి": 1, "రెండు": 2, "మూడు": 3, "నాలుగు": 4, "ఐదు": 5,
    "ఆరు": 6, "ఏడు": 7, "ఎనిమిది": 8, "తొమ్మిది": 9
}

TELUGU_TENS = {
    "పది": 10, "ఇరవై": 20, "ముప్పై": 30, "నలభై": 40,
    "యాభై": 50, "అరవై": 60, "డెబ్బై": 70,
    "ఎనభై": 80, "తొంభై": 90
}


# =========================
# HELPER FUNCTIONS
# =========================
def is_trivial_input(text: str) -> bool:
    return any(k in text for k in ["పేరు", "హాయ్", "నమస్కారం"])


def extract_telugu_number(text: str):
    for t_word, t_val in TELUGU_TENS.items():
        if t_word in text:
            for o_word, o_val in TELUGU_ONES.items():
                if o_word in text:
                    return t_val + o_val
            return t_val

    for o_word, o_val in TELUGU_ONES.items():
        if o_word in text:
            return o_val

    return None


def extract_income(text: str):
    """
    Handles:
    - ఆదాయం రెండు లక్షలు
    - 2 లక్షలు
    - ఆదాయం 50000
    """
    # Case 1: digits
    digit_match = re.search(r"\d+", text)
    if digit_match:
        amount = int(digit_match.group())

        if "లక్ష" in text:
            return amount * 100000
        if "వేల" in text:
            return amount * 1000

        return amount

    # Case 2: Telugu words
    number = extract_telugu_number(text)
    if number:
        if "లక్ష" in text:
            return number * 100000
        if "వేల" in text:
            return number * 1000

    return None


def extract_locally(text: str) -> dict:
    data = {"age": None, "income": None, "state": None}

    # ---------- AGE ----------
    digit_age = re.search(r"\d+", text)
    if digit_age and any(w in text for w in ["వయసు", "సంవత్సరాలు", "ఏళ్ళు"]):
        data["age"] = int(digit_age.group())
    else:
        word_age = extract_telugu_number(text)
        if word_age and any(w in text for w in ["వయసు", "సంవత్సరాలు", "ఏళ్ళు"]):
            data["age"] = word_age

    # ---------- INCOME ----------
    if "ఆదాయం" in text or "లక్ష" in text or "వేల" in text:
        data["income"] = extract_income(text)

    # ---------- STATE ----------
    states = [
        "తెలంగాణ", "ఆంధ్రప్రదేశ్", "కర్ణాటక",
        "తమిళనాడు", "కేరళ", "మహారాష్ట్ర"
    ]
    for s in states:
        if s in text:
            data["state"] = s

    return data


# =========================
# MAIN AGENT FUNCTION
# =========================
def run_agent(user_text: str) -> str:

    # 1️⃣ Trivial
    if is_trivial_input(user_text):
        return (
            "ధన్యవాదాలు అండి. "
            "దయచేసి మీ వయస్సు, ఆదాయం, మరియు రాష్ట్రం చెప్పండి."
        )

    # 2️⃣ Local extraction
    extracted = extract_locally(user_text)
    for k, v in extracted.items():
        if v is not None:
            memory.update(k, v)

    # 3️⃣ Ask missing info
    if not memory.is_complete():
        labels = {"age": "వయస్సు", "income": "ఆదాయం", "state": "రాష్ట్రం"}
        missing = [labels[k] for k in ["age", "income", "state"] if not memory.get(k)]
        return "దయచేసి మీ " + " మరియు ".join(missing) + " వివరాలు చెప్పండి."

    # 4️⃣ Eligibility
    schemes = check_eligibility(
        age=memory.get("age"),
        income=memory.get("income"),
        state=memory.get("state")
    )

    if not schemes:
        return "మీ వివరాలకు సరిపడే ప్రభుత్వ పథకాలు ప్రస్తుతం లేవు."

    # 5️⃣ Final Gemini call
    scheme = schemes[0]
    details = get_scheme_details(scheme)

    prompt = f"""
    వినియోగదారు {scheme} పథకానికి అర్హుడు.
    వివరణ: {details.get('description','')}
    అవసరమైన పత్రాలు: {details.get('documents','')}
    రెండు వాక్యాల్లో సరళమైన తెలుగులో వివరించండి.
    """

    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt
        )
        return response.text.strip()

    except Exception:
        return "ప్రస్తుతం సాంకేతిక సమస్య ఉంది. దయచేసి కొద్దిసేపటి తరువాత ప్రయత్నించండి."
