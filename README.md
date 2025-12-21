# 🗣️ SahaayaVaani – Voice-First Telugu Welfare Assistant

**SahaayaVaani** is a **voice-first, Telugu-native, agentic AI assistant** designed to help citizens identify their eligibility for Indian government welfare schemes using **natural speech**.

Built with a **Planner–Executor–Memory** workflow, the system is designed for **real-world public service kiosks** and assisted-access environments, enabling **end-to-end voice interaction**:

> **Speech → Reasoning → Tools → Speech**

---

## 🎯 Key Features

### 🎙️ Voice-First Interaction

Users interact **entirely through voice**—no typing, reading, or technical literacy required.

### 🗣️ Native Telugu Support

Complete Telugu pipeline:

* Speech-to-Text (STT)
* Telugu-native reasoning
* Text-to-Speech (TTS)

### 🤖 Agentic Workflow

Implements an **explicit agent orchestration loop**:

* Planner decides next action
* Executor invokes tools
* Evaluator validates outcomes
  Local reasoning is used for speed, with LLMs leveraged for richer explanations.

### 🧠 Conversation Memory

* Remembers user attributes (age, income, state) across turns
* Detects contradictions and asks for clarification
* Supports multi-user sessions

### 🧰 Integrated Tools

* **Eligibility Engine** – Rule-based eligibility matching
* **Scheme Knowledge Base (KB)** – Structured data on government schemes

### ⚠️ Robust Error Handling

Gracefully handles:

* Silence and background noise
* Incomplete or conflicting information
* Recognition uncertainty with intelligent fallbacks

---

## 🏗️ System Architecture

The assistant follows a structured, low-latency pipeline:

1. **Input** – User speaks in Telugu
2. **Recognition** – STT converts speech to Telugu text
3. **Extraction** – Local logic extracts age, income, and state
4. **Reasoning** – Agent orchestrator plans and invokes tools
5. **Synthesis** – LLM generates a friendly Telugu explanation
6. **Output** – TTS converts the response back to speech

This design ensures **accuracy, speed, and production feasibility**.

---

## 📁 Project Structure

```text
sahaayavaani/
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
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/sahaayavaani.git
cd sahaayavaani
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

**Activate the environment:**

* **Windows (PowerShell)**

```powershell
venv\Scripts\activate
```

* **Mac/Linux**

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Environment Variables

The system uses a **Gemini API key** for advanced explanation generation.

* **Windows (PowerShell)**

```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

* **Mac/Linux**

```bash
export GEMINI_API_KEY="your_api_key_here"
```

### 5️⃣ Run the Application

```bash
python app.py
```

---

## 🗣️ How to Use

1. **Greeting**
   The agent greets you in Telugu and requests basic details.

2. **Speak Naturally**
   Example:

   > *"నా వయసు 45 ఏళ్లు, నా ఆదాయం రెండు లక్షలు, మాది ఆంధ్రప్రదేశ్."*

3. **Processing**

   * Telugu numbers and phrases are normalized
   * Eligibility is checked using integrated tools

4. **Result**
   The agent announces:

   * Eligible schemes
   * Required documents
     via **voice output**

5. **Multi-User Support**
   The agent can start a new eligibility check for another user before closing the session.

---

## 🛡️ Compliance Checklist

| Requirement                          | Status |
| ------------------------------------ | ------ |
| Voice-first interaction              | ✅      |
| Native Telugu language pipeline      | ✅      |
| Agentic workflow (reasoning + tools) | ✅      |
| Dual tool usage (Eligibility + KB)   | ✅      |
| Conversation memory                  | ✅      |
| Failure & silence handling           | ✅      |

---

## 🚀 Future Enhancements

* **Apply-Now Workflow** – Direct integration with official government portals
* **Mobile Authentication** – Phone number capture for SMS follow-ups
* **Multilingual Expansion** – Kannada, Tamil, Hindi support
* **Live APIs** – Real-time scheme updates from government databases

---

## 👨‍💻 Author

**Jahnavi Dingari**
Voice-First AI | Data & AI Engineering

---

## 📜 License

This project is intended for **educational and demonstration purposes**.

---

