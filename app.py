"""
SahaayaVaani – Voice-First Welfare Scheme Agent (Telugu)
Entry point for the agentic system
"""

import sys
import time
from agent.orchestrator import run_agent
from audio.stt import listen_and_transcribe
from audio.tts import speak
from memory.session_memory import memory  # Import memory to reset it


def main():
    # Force UTF-8 for Telugu characters in terminal
    if sys.platform.startswith('win'):
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    print("--- SahaayaVaani Active ---")

    # Welcome Message
    welcome = "నమస్కారం. నేను సహాయవాణి. ప్రభుత్వ పథకాల కోసం మీకు సహాయం చేస్తాను."
    print(f"🤖 AGENT: {welcome}")
    speak(welcome)

    while True:
        # Prevent mic from catching TTS tail
        time.sleep(0.5)

        # 1. Capture User Speech
        user_text, confidence = listen_and_transcribe()

        # 2. Handle Silence or Low Confidence
        if confidence < 0.6 or not user_text.strip():
            if user_text.strip():
                err_msg = "క్షమించండి, మీ మాటలు సరిగ్గా వినిపించలేదు. దయచేసి మళ్లీ చెప్పండి."
                print(f"🤖 AGENT: {err_msg}")
                speak(err_msg)
            continue

        # 3. Exit keywords
        if any(word in user_text.lower() for word in ["ఆపండి", "బై", "సెల్వు", "stop", "bye"]):
            exit_msg = "ధన్యవాదములు. మళ్లీ కలుద్దాం."
            print(f"🤖 AGENT: {exit_msg}")
            speak(exit_msg)
            break

        # 4. Process through Orchestrator
        response = run_agent(user_text)

        # 5. Speak Response
        print(f"🤖 AGENT: {response}")
        speak(response)

        # 6. FINAL STEP: Ask if user wants to check for another person
        if (
            "పథకం" in response or
            "పథకాలు" in response or
            "లేవు" in response
        ):
            followup = "ఇంకొక వ్యక్తి కోసం చెక్ చేయాలా? అవును లేదా కాదు చెప్పండి."
            print(f"🤖 AGENT: {followup}")
            speak(followup)

            reply_text, reply_conf = listen_and_transcribe()
            reply = reply_text.lower()

            # YES → restart flow
            if any(w in reply for w in ["అవును", "అవునండి", "yes", "ha"]):
                print("\n--- Restarting for another person ---\n")
                memory.clear()
                speak("సరే. కొత్త వ్యక్తి వివరాలు చెప్పండి.")
                continue

            # NO → end conversation
            closing = "ధన్యవాదములు"
            print(f"🤖 AGENT: {closing}")
            speak(closing)
            memory.clear()
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Stopping SahaayaVaani... Bye!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
