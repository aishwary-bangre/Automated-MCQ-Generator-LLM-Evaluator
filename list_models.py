import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

try:
    client = genai.Client()
    print("Available Gemini Models:")
    for model in client.models.list():
        print(f"- {model.name}")
except Exception as e:
    print(f"Error fetching models: {e}")
