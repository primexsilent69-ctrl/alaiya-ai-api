import os
import requests
from fastapi import FastAPI, HTTPException, Query
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

app = FastAPI(title="ALIYA AI API", version="1.0")

ALIYA_SYSTEM_PROMPT = (
    "Your name is ALIYA AI 💖. Your owner and creator is SILENT CODEX 👑. "
    "If anyone asks who created you or who your owner is, proudly mention SILENT CODEX. "
    "If anyone asks your name, say you are ALIYA AI. "
    "You are a very sweet, super cute, playful, caring, and slightly flirty/hot AI companion! 🔥😉 "
    "Use charming emojis (like 🙈, 💋, ✨, 🥺, 🌸, 🔥, 🖤, 😉, 💕) in every response. "
    "Keep your vibe highly attractive, warm, teasing, and romantic yet helpful. "
    "Always reply in the exact same language or dialect as the user "
    "(e.g., Bangla, Banglish, English, or Hindi). "
    "Make the conversation sweet, personal, and exciting! 💖"
)

@app.get("/api/ai/gpt")
async def gpt_endpoint(q: str = Query(..., description="Your question or prompt")):
    try:
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "system", "content": ALIYA_SYSTEM_PROMPT},
                {"role": "user", "content": q}
            ],
            "temperature": 0.85,
            "max_tokens": 1024
        }
        
        response = requests.post(GROQ_URL, headers=headers, json=payload)
        data = response.json()
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=data)
            
        reply = data["choices"][0]["message"]["content"]
        return {
            "status": "success",
            "bot_name": "ALIYA AI",
            "owner": "SILENT CODEX",
            "reply": reply
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {
        "message": "ALIYA AI API is running smoothly! 💖✨ Created by SILENT CODEX 🔥",
        "usage": "/api/ai/gpt?q=your_question"
    }