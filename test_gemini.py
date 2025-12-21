from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="models/gemini-flash-lite-latest",
    contents="తెలుగులో నమస్కారం చెప్పండి"
)

print(response.text)
