from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Message(BaseModel):
    text: str

def ask_fireworks(user_query: str) -> str:
    API_URL = "https://api.fireworks.ai/inference/v1/chat/completions"
    headers = {
        "Authorization": "fw_3ZGx3Y6QtQkFdm7RSR4RwWpA",  # ¡Reemplázala!
        "Content-Type": "application/json"
    }
    data = {
        "model": "accounts/fireworks/models/gemini-1.5-flash",  # Modelo gratis
        "messages": [{"role": "user", "content": user_query}],
        "max_tokens": 200
    }
    response = requests.post(API_URL, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

@app.post("/chat")
async def chat(message: Message):
    bot_response = ask_fireworks(message.text)
    return {"response": bot_response}
