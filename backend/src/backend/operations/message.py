from pydantic import BaseModel


class Message(BaseModel):
    message: str
    user: str
    timestamp: str
