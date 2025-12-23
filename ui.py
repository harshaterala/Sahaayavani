import streamlit as st
from app import run_once
from memory.session_memory import memory

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="SahaayaVaani", page_icon="🎙️")

st.title("🎙️ SahaayaVaani")
st.caption("Voice-based Telugu Public Welfare Assistant")

# -----------------------------
# Session state initialization
# -----------------------------
if "started" not in st.session_state:
    st.session_state.started = False

if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------------
# Welcome screen (UI-controlled)
# -----------------------------
if not st.session_state.started:
    welcome = "నమస్కారం. నేను సహాయవాణి. ప్రభుత్వ పథకాల కోసం మీకు సహాయం చేస్తాను."
    st.markdown(f"**🤖 Agent:** {welcome}")

    if st.button("▶️ Start Conversation"):
        st.session_state.started = True
        st.session_state.history.append(("🤖 Agent", welcome))

# -----------------------------
# Active conversation
# -----------------------------
if st.session_state.started:
    if st.button("🎧 Ask SahaayaVaani"):
        with st.spinner("Listening... Speak in Telugu"):
            user_text, response = run_once()

        if user_text and response:
            st.session_state.history.append(("🧑 User", user_text))
            st.session_state.history.append(("🤖 Agent", response))

# -----------------------------
# Conversation history
# -----------------------------
st.divider()

for role, text in st.session_state.history:
    st.markdown(f"**{role}:** {text}")

# -----------------------------
# Reset memory
# -----------------------------
if st.button("🧠 Clear Memory"):
    memory.clear()
    st.session_state.history.clear()
    st.session_state.started = False
