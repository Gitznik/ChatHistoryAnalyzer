from backend.operations.db import create_db_conn, get_chatlog
from backend.operations.message import Message
from fastapi import APIRouter, Response

router = APIRouter()

DB_CONN = create_db_conn()


@router.get("/")
def get_analysis_route(id: str, response: Response):
    chatlog = get_chatlog(DB_CONN, id, response)
    return {"message": "Analysis retrieved"}
