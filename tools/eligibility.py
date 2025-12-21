# tools/eligibility.py

def normalize_state(state: str) -> str:
    """
    Converts Telugu state names to English canonical names
    """
    state_map = {
        "ఆంధ్రప్రదేశ్": "Andhra Pradesh",
        "తెలంగాణ": "Telangana",
        "కర్ణాటక": "Karnataka",
        "తమిళనాడు": "Tamil Nadu",
        "కేరళ": "Kerala",
        "మహారాష్ట్ర": "Maharashtra"
    }
    return state_map.get(state, state)


def check_eligibility(age, income, state):
    state = normalize_state(state)

    schemes = [
        {
            "name": "YSR Cheyutha",
            "min_age": 45,
            "max_age": 60,
            "max_income": 600000,
            "state": "Andhra Pradesh"
        },
        {
            "name": "Amma Vodi",
            "min_age": 5,
            "max_age": 18,
            "max_income": 120000,
            "state": "Andhra Pradesh"
        },
        {
            "name": "Rythu Bharosa",
            "min_age": 18,
            "max_age": 100,
            "max_income": 200000,
            "state": "Telangana"
        },
        {
            "name": "General Welfare Scheme",
            "min_age": 18,
            "max_age": 100,
            "max_income": 1000000,
            "state": "Andhra Pradesh"
        }
    ]

    eligible_names = []

    for s in schemes:
        if (
            s["min_age"] <= age <= s["max_age"] and
            income <= s["max_income"] and
            state == s["state"]
        ):
            eligible_names.append(s["name"])

    return eligible_names
