import speech_recognition as sr
import re
import time


# =========================
# SYSTEM BEEP
# =========================
def beep():
    print("\a", end="", flush=True)


# =========================
# CLEAN TELUGU TEXT (LESS AGGRESSIVE)
# =========================
def clean_user_text(text: str) -> str:
    if not text:
        return ""

    # Keep Telugu + digits + spaces
    text = re.sub(r"[^\u0C00-\u0C7F0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# =========================
# LISTEN & TRANSCRIBE
# =========================
def listen_and_transcribe():
    r = sr.Recognizer()

    # 🔥 CRITICAL FIXES
    r.pause_threshold = 0.8          # allow natural pauses
    r.energy_threshold = 150         # LOWER sensitivity
    r.dynamic_energy_threshold = False  # 🔴 VERY IMPORTANT

    with sr.Microphone() as source:
        # Short ambient calibration
        r.adjust_for_ambient_noise(source, duration=0.3)

        print("\n🎤 READY — SPEAK AFTER THE BEEP", flush=True)
        beep()
        print("🎙️ Listening NOW...", flush=True)

        try:
            audio = r.listen(
                source,
                timeout=8,            # give time to start speaking
                phrase_time_limit=6   # allow full sentence
            )

            print("⏳ Transcribing...", flush=True)

            raw_text = r.recognize_google(
                audio,
                language="te-IN"
            )

            clean_text = clean_user_text(raw_text)

            # 🔴 IMPORTANT: DO NOT reject short valid speech
            print(f"🗣️ User said: {clean_text}", flush=True)
            return clean_text, 1.0

        except sr.WaitTimeoutError:
            print("🕒 You didn’t speak in time", flush=True)
            return "", 0.0

        except sr.UnknownValueError:
            print("☁️ Couldn’t understand speech", flush=True)
            return "", 0.0

        except sr.RequestError as e:
            print(f"❌ Google STT network error: {e}", flush=True)
            return "", 0.0

        except Exception as e:
            print(f"❌ STT Error: {e}", flush=True)
            return "", 0.0
