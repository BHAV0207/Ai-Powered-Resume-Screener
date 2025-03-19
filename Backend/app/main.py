from fastapi import FastAPI
from .core.database import db 

app = FastAPI()

@app.get("/test-db")
async def test_db():
    collections = await db.list_collection_names()
    return {"collections": collections}