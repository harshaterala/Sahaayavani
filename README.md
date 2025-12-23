# 🎙️ SahaayaVaani – Voice-First Telugu Welfare Assistant

**SahaayaVaani** is a **voice-first, Telugu-native, agentic AI system** designed to help citizens identify their eligibility for Indian government welfare schemes using **natural spoken interaction**.

The system is built to simulate real-world **public service kiosks** and assisted-access environments, where users may not be comfortable with typing, reading, or navigating complex digital interfaces.

> **Speech → Reasoning → Tools → Speech**

---

## 🎯 Key Capabilities

### 🎙️ Voice-First Interaction
Users interact **entirely through voice**, making the system accessible to non-technical and low-literacy users.

### 🗣️ Native Telugu Pipeline
The system operates end-to-end in Telugu:
- Speech-to-Text (STT)
- Telugu-aware reasoning
- Text-to-Speech (TTS)

### 🤖 Agentic Workflow
Implements a clear **Planner–Executor–Memory** loop:
- The agent plans the next step based on conversation state
- Tools are invoked for eligibility checking
- Responses are validated and refined before being spoken

Local logic is used for structured reasoning, while LLMs are leveraged for fluent and natural explanations.

### 🧠 Conversation Memory
- Persists user attributes (age, income, state) across turns
- Detects missing or contradictory information
- Supports multi-user sessions with explicit memory reset

### 🧰 Tool-Driven Design
- **Eligibility Engine** – Rule-based matching against scheme criteria
- **Scheme Knowledge Base** – Structured local representation of welfare schemes

### ⚠️ Robust Failure Handling
Gracefully manages:
- Silence or background noise
- Low-confidence speech recognition
- Partial or ambiguous inputs
- Intelligent recovery prompts instead of hallucinated answers

---

## 🏗️ System Architecture

The assistant follows a low-latency, modular pipeline:

1. **Input** – User speaks in Telugu  
2. **Recognition** – STT converts speech to Telugu text  
3. **Extraction** – Local logic extracts age, income, and state  
4. **Reasoning** – Agent orchestrator plans and invokes tools  
5. **Synthesis** – LLM generates a natural Telugu explanation  
6. **Output** – TTS converts the response back to speech  

This design prioritizes **accuracy, transparency, and production feasibility**.

---

## 📁 Project Structure

```text
Agentic-Voice-Welfare-System/
├── app.py                   # Core application (CLI + agent runtime)
├── ui.py                    # Streamlit UI for demo and interaction
├── agent/
│   └── orchestrator.py      # Agent planning and tool orchestration
├── audio/
│   ├── stt.py               # Speech-to-Text (Telugu)
│   └── tts.py               # Text-to-Speech (Telugu)
├── tools/
│   ├── eligibility.py       # Rule-based eligibility engine
│   └── scheme_kb.py         # Local scheme knowledge base
├── memory/
│   └── session_memory.py    # Per-session conversation memory
├── requirements.txt
└── README.md
'''

⚙️ Setup & Execution
1️⃣ Clone the Repository
bash
Copy code
git clone https://github.com/<your-username>/Agentic-Voice-Welfare-System.git
cd Agentic-Voice-Welfare-System
2️⃣ Create and Activate Virtual Environment
bash
Copy code
python -m venv venv
Windows (PowerShell):

powershell
Copy code
venv\Scripts\activate
Mac/Linux:

bash
Copy code
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
pip install google-genai SpeechRecognition pyaudio streamlit
4️⃣ Set Environment Variables
The system uses Google Gemini for language generation.

Windows (PowerShell):

powershell
Copy code
$env:GEMINI_API_KEY="your_api_key_here"
Mac/Linux:

bash
Copy code
export GEMINI_API_KEY="your_api_key_here"
5️⃣ Run the Application
CLI Mode

bash
Copy code
python app.py
UI Mode

bash
Copy code
streamlit run ui.py
🗣️ Example Interaction
User (Telugu):

“నా వయసు 45 ఏళ్లు, నా ఆదాయం రెండు లక్షలు, మాది ఆంధ్రప్రదేశ్.”

Agent:

Extracts structured attributes

Checks eligibility via tools

Responds with applicable schemes or a clear explanation if none apply

Speaks the response in Telugu

🛡️ Requirement Coverage
Requirement	Status
Voice-first interaction	✅
Native Telugu language pipeline	✅
Agentic reasoning (Planner–Executor loop)	✅
Tool usage (Eligibility + Knowledge Base)	✅
Conversation memory across turns	✅
Failure handling & recovery	✅

🚀 Future Extensions
Integration with real government APIs

Retrieval-Augmented Generation (RAG) over official scheme documents

Multilingual support (Tamil, Kannada, Hindi)

Persistent storage (SQLite / cloud backend)

Mobile-friendly deployment

👨‍💻 Author
T Harshavardhan
Final-year BTech – Computer Science (AI & ML)
Interests: Voice AI, Agentic Systems, Applied ML

📜 License
This project is intended for educational and demonstration purposes.

