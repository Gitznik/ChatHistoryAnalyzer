from fastapi import APIRouter
from backend.operations.message import Message

router = APIRouter()

@router.post("/chatlog")
async def save_chatlog(Message: Message):
    return {"message": "Chatlog saved"}