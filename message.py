from pydantic import BaseModel

class MessageRequest(BaseModel):
    prompt: str

class MessageResponse(BaseModel):
    reply: str