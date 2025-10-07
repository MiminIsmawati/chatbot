from app.models.message import MessageRequest, MessageResponse
from config.gemini import ask_gemini

async def chat_controller(request: MessageRequest) -> MessageResponse:
    reply = await ask_gemini(request.prompt)
    return MessageResponse(reply=reply)
