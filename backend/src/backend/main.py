from fastapi import FastAPI

from backend.operations.message import Message
from backend.routes import chatlog

app = FastAPI()

app.include_router(chatlog.router)

@app.get("/")
def root():
    return {"message": "The API is up and running!"}
