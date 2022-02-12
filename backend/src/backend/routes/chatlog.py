from backend.operations.db import (
    DatabaseConnection,
    MongoDBConnection,
    ObjectNotFoundError,
)
from backend.operations.message import Message
from fastapi import APIRouter, Response, status

router = APIRouter()
DB_CONN: DatabaseConnection = MongoDBConnection()


@router.post("/")
def save_chatlog(message: Message):
    print(DB_CONN.insert_one("Messages", "SubmittedMessage", message.dict()))
    return {"message": "Chatlog saved"}


@router.get("/")
def get_chatlog(id: str, response: Response):
    try:
        return DB_CONN.retrieve_one("Messages", "SubmittedMessage", id)
    except ObjectNotFoundError as e:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": str(e)}
