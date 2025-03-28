from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
import logging

# Configura logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# ----- Configuración CORS (permite llamadas desde cualquier origen) -----
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, reemplaza "*" con tu dominio frontend
    allow_methods=["POST", "GET"],  # Métodos permitidos
    allow_headers=["*"],
)

# ----- Modelo de datos para el mensaje -----
class Message(BaseModel):
    text: str
    # (Opcional) Añade más campos si WhatsApp/Meta envía datos adicionales
    # Ej: user_id: str, timestamp: str

# ----- Ruta raíz (para verificar que el bot está vivo) -----
@app.get("/")
def home():
    return {
        "status": "active",
        "message": "Envía un POST a /chat para interactuar con el bot.",
        "docs": "/docs"
    }

# ----- Ruta principal del bot (POST) -----
@app.post("/chat")
async def chat(message: Message, request: Request):
    try:
        logger.info(f"Mensaje recibido: {message.text}")
        
        # Simula una respuesta de DeepSeek (reemplaza esto con la API real si tienes acceso)
        bot_response = f"🔍 DeepSeek responde a '{message.text}'. (Modo simulación)"

        # Opcional: Registra la IP del solicitante (útil para depurar)
        client_ip = request.client.host
        logger.info(f"Solicitud desde IP: {client_ip}")

        return {"response": bot_response}

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")

# ----- Configuración para Render -----
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))  # Usa el puerto de Render o 10000 local
    uvicorn.run(app, host="0.0.0.0", port=port)
