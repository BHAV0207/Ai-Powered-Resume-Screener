from fastapi import HTTPException
from app.services.nlp_utils import match_resume_to_job
from app.core.database import resume_collection
from fastapi import APIRouter

router = APIRouter()

@router.post("/match_resume")
async def match_resume(resume_id: str, job_description: str):
    resume = await resume_collection.find_one({"_id": ObjectId(resume_id)})
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")

    score = match_resume_to_job(resume["text"], job_description)
    return {"resume_id": resume_id, "match_score": score}
