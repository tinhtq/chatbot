from fastapi import APIRouter, UploadFile
from app.services import handle_pdf

router = APIRouter()


@router.post("/pdf")
def invoke(file: UploadFile):
    try:
        resp = handle_pdf(file)
        return {"response": resp}
    except Exception as e:
        return {"error": str(e)}
