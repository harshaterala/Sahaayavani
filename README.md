🗣️ SahaayaVaani: Voice-First Telugu Welfare AssistantSahaayaVaani is a voice-first, Telugu-native, agentic AI assistant designed to help citizens check their eligibility for government welfare schemes using natural speech.Built with a Planner–Executor–Memory workflow, the system is designed for real-world public service kiosks, enabling end-to-end voice interaction: Speech → Reasoning → Tools → Speech.🎯 Key Features🎙️ Voice-First Interaction: Users interact completely through speech—no typing or technical literacy required.🗣️ Native Telugu Support: Full Telugu pipeline including Speech-to-Text (STT), natural language reasoning, and Text-to-Speech (TTS).🤖 Agentic Workflow: Uses local reasoning for speed and LLMs for complex explanations, navigating decisions without hard-coded flows.🧠 Conversation Memory: Remembers user attributes (age, income, state) across turns and supports multi-user sessions.🧰 Integrated Tools: * Eligibility Engine: Logic-based rule matching.Scheme Knowledge Base (KB): Comprehensive data on government programs.⚠️ Robust Error Handling: Gracefully handles silence, background noise, and missing information with intelligent fallbacks.🏗️ System ArchitectureThe assistant follows a structured pipeline to ensure accuracy and low latency:Input: User speaks in Telugu.Recognition: Google STT converts audio to Telugu text.Extraction: Local logic extracts variables (Age, Income, State) to save API costs.Reasoning: The Orchestrator queries the Eligibility Tool and Knowledge Base.Synthesis: LLM generates a friendly explanation in Telugu.Output: TTS plays the response back to the user.📁 Project StructurePlaintextsahaayavaani/
├── app.py                   # Entry point (Main Application Loop)
├── agent/
│   └── orchestrator.py      # Agent logic (Reasoning + Tool Dispatch)
├── audio/
│   ├── stt.py               # Speech-to-Text (Telugu)
│   └── tts.py               # Text-to-Speech (Telugu)
├── tools/
│   ├── eligibility.py       # Rule-based Eligibility Engine
│   └── scheme_kb.py         # Government Scheme Knowledge Base
├── memory/
│   └── session_memory.py    # Per-user conversation context
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
⚙️ Setup Instructions1. Clone the RepositoryBashgit clone https://github.com/your-username/sahaayavaani.git
cd sahaayavaani
2. Create a Virtual EnvironmentBashpython -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on Mac/Linux:
source venv/bin/activate
3. Install DependenciesBashpip install -r requirements.txt
4. Set Environment VariablesThe system requires a Gemini API Key for explanation generation.Windows (PowerShell):PowerShell$env:GEMINI_API_KEY="your_api_key_here"
Mac/Linux:Bashexport GEMINI_API_KEY="your_api_key_here"
5. Run the ApplicationBashpython app.py
🗣️ How to UseGreeting: The agent greets you in Telugu and asks for your details.Speech: Speak naturally. Example: "నా వయసు 45 ఏళ్లు, నా ఆదాయం రెండు లక్షలు, మాది ఆంధ్రప్రదేశ్."Processing: The agent normalizes Telugu numbers and terms into data points.Result: The agent announces eligible schemes and required documents via voice.Multi-User: The agent will ask if you want to check for someone else before closing the session.🛡️ Compliance ChecklistRequirementStatusVoice-first interaction✅Native Telugu Language Support✅Agentic Workflow (Reasoning/Tools)✅Dual Tool Usage (KB + Eligibility)✅Conversation Memory✅Failure/Silence Handling✅🚀 Future EnhancementsApply-Now Workflow: Integration with official portals to start applications.Mobile Auth: Capturing phone numbers for SMS follow-ups.Multilingual Expansion: Adding support for Kannada, Tamil, and Hindi.Real-time API: Fetching live scheme updates from government databases.👨‍💻 AuthorJahnavi Dingari Voice-First AI | Data & AI Engineering📜 LicenseThis project is intended for educational and demonstration purposes.