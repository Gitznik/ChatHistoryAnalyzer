from fastapi import FastAPI

from backend.operations.message import Message
from backend.routes import chatlog

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "The API is up and running!"}


app.include_router(chatlog.router, prefix="/chatlog")
