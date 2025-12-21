import re
from gtts import gTTS
import pygame
import os
import time

def speak(text):
    if not text: return
    
    # --- SAFE CLEANING FOR TELUGU ---
    # Instead of filtering for letters (which breaks Telugu), 
    # we ONLY remove Markdown symbols and specific problematic characters.
    # This keeps all Telugu vowels and markers (Virama/Halant) intact.
    clean_text = re.sub(r'[\*\#\_\-\>\(\)\[\]\:\;\"]', ' ', text)
    
    # Remove extra spaces but keep the gaps between words
    clean_text = " ".join(clean_text.split())
    
    # FORCE FLUSH: This ensures logs appear immediately in the terminal
    print(f"🔊 Speaking: {clean_text}", flush=True)

    try:
        # slow=False makes it sound more natural; set to True if it's too fast
        tts = gTTS(text=clean_text, lang='te', slow=False)
        filename = "response.mp3"
        tts.save(filename)
        
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        
        # Proper cleanup to prevent "file in use" errors
        pygame.mixer.music.unload()
        pygame.mixer.quit()
        
        if os.path.exists(filename):
            os.remove(filename)

    except Exception as e:
        print(f"❌ TTS Error: {e}", flush=True)