from fastapi import FastAPI
from routes.chat_router import router as chat_router
from fastapi.middleware.cors import CORSMiddleware

def create_app() -> FastAPI:
    app = FastAPI(title="Gemini v1 Chatbot")

    # Register routers
    app.include_router(chat_router)

    app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # atau ganti dengan origin React kamu
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

    return app
