from fastapi import FastAPI

from backend.routes import analysis, chatlog

app = FastAPI()

app.include_router(chatlog.router, prefix="/chatlog")
app.include_router(analysis.router, prefix="/analysis")


@app.get("/")
def root():
    return {"message": "The API is up and running!"}
