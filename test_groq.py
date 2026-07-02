import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

try:
    client = Groq()
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": "Ping!"}],
        max_tokens=10
    )
    print("SUCCESS: Groq API key is perfectly valid! Response:", response.choices[0].message.content)
except Exception as e:
    print(f"FAILED: Groq API Error - {e}")
