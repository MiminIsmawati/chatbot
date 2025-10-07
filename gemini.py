import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import asyncio

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Fungsi untuk baca isi knowledge.txt
def load_knowledge():
    try:
        with open("public/knowledge.txt", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return ""

async def ask_gemini(prompt: str) -> str:
    try:
        # Muat knowledge base
        knowledge = load_knowledge()

        # Gabungkan knowledge + user prompt
        full_prompt = f"""
Berikut adalah informasi latar belakang untuk membantumu menjawab:

{knowledge}

Sekarang, jawab pertanyaan berikut ini berdasarkan informasi di atas (jika relevan):
{prompt}
"""

        def sync_call():
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=full_prompt,
                config=types.GenerateContentConfig(
                    thinking_config=types.ThinkingConfig(thinking_budget=0)
                ),
            )
            return response.text.strip()

        return await asyncio.to_thread(sync_call)
    
    except Exception as e:
        return f"Error: {str(e)}"
