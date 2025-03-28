from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup

app = FastAPI()

class Message(BaseModel):
    text: str

def ask_deepseek(user_query: str) -> str:
    try:
        # Simula una solicitud a DeepSeek (ejemplo educativo, no confiable)
        response = f"🔍 Respuesta simulada de DeepSeek a: '{user_query}'"
        
        # --- Alternativa con scraping (frágil) ---
        # Si DeepSeek tiene un campo de búsqueda web:
        # url = "https://www.deepseek.com/chat"
        # page = requests.get(url).text
        # soup = BeautifulSoup(page, "html.parser")
        # response = soup.find("div", class_="respuesta").text  # Ajusta según HTML real
        
        return response
    except Exception as e:
        return f"Error al contactar DeepSeek: {str(e)}"

@app.post("/chat")
async def chat(message: Message):
    bot_response = ask_deepseek(message.text)
    return {"response": bot_response}
