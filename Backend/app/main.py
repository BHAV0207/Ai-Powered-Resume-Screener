from fastapi import FastAPI
from app.api.endpoints import resumes 
from app.api.endpoints import matching

app = FastAPI()

# ✅ Register API routes
app.include_router(resumes.router, prefix="/api")

app.include_router(matching.router , prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to AI Resume Screener!"}
