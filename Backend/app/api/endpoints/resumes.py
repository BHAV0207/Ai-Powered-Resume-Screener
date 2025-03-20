import pdfplumber
from fastapi import APIRouter , UploadFile , File
from app.core.database import resume_collection
from app.models.resume import Resume


router = APIRouter()

async def extract_text_from_pdf(pdf_file: UploadFile):
    with pdfplumber.open(pdf_file.file) as pdf:
      text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    return text
  
@router.post("/upload_resume")
async def upload_resume(pdf : UploadFile = File(...)):
    text = await extract_text_from_pdf(pdf)
    resume_data = {"text": text}
    result = await resume_collection.insert_one(resume_data)
    return {"id": str(result.inserted_id) , "message": "Resume Uploaded Successfully"}