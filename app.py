import os
from openai import OpenAI
from fastapi import FastAPI, HTTPException, Query
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client with Groq
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

app = FastAPI(title="Groq AI GPT API", version="1.0")

@app.get("/api/ai/gpt")
async def gpt_endpoint(q: str = Query(..., description="Your question or prompt")):
    """
    GET endpoint that accepts a 'q' parameter and returns an AI-generated reply.
    Example: /api/ai/gpt?q=Hello
    """
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant. Reply in the same language as the user."},
                {"role": "user", "content": q}
            ],
            temperature=0.7,
            max_tokens=1024
        )
        reply = response.choices[0].message.content
        return {"reply": reply}  # JSON response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "AI GPT API is running. Use /api/ai/gpt?q=your_question"}


Ai api banao khud ka or 💀💀❌
