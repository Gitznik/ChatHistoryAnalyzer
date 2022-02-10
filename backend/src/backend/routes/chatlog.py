from backend.operations.db import DatabaseConnection, MongoDBConnection
from backend.operations.message import Message
from fastapi import APIRouter

router = APIRouter()
DB_CONN: DatabaseConnection = MongoDBConnection()


@router.post("/")
def save_chatlog(message: Message):
    print(DB_CONN.insert_one("Messages", "SubmittedMessage", message.dict()))
    return {"message": "Chatlog saved"}


@router.get("/")
def get_chatlog(user: str):
    return DB_CONN.retrieve_one("Messages", "SubmittedMessage", {"user": user})
