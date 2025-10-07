from fastapi import APIRouter
from app.models.message import MessageRequest, MessageResponse
from app.controllers.chat_controller import chat_controller

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("", response_model=MessageResponse)
async def chat_route(request: MessageRequest):
    return await chat_controller(request)
