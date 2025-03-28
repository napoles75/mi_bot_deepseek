from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

@app.post("/chat")
async def chat(message: Message):
    user_query = message.text
    # Aquí deberías llamar a DeepSeek (simulamos respuesta)
    respuesta = f"🔍 DeepSeek responde: '{user_query}'. (Esta es una simulación.)"
    return {"response": respuesta}
