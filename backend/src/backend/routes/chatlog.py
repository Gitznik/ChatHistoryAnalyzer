from backend.operations.db import create_db_conn, get_chatlog
from backend.operations.message import Message
from fastapi import APIRouter, Response

router = APIRouter()
DB_CONN = create_db_conn()


@router.post("/")
def save_chatlog(message: Message):
    print(DB_CONN.insert_one("Messages", "SubmittedMessage", message.dict()))
    return {"message": "Chatlog saved"}


@router.get("/")
def get_chatlog_route(id: str, response: Response):
    return get_chatlog(DB_CONN, id, response)
