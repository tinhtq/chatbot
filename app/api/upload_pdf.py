from fastapi import APIRouter, UploadFile, File
from app.services import handle_pdf, convert_pdf

router = APIRouter()


@router.post("/pdf")
def invoke(file: UploadFile = File(...)):
    try:
        resp = handle_pdf(file)
        return {"response": resp}
    except Exception as e:
        return {"error": str(e)}
