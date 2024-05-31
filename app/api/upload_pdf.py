from fastapi import APIRouter, UploadFile, File
from app.services import handle_pdf, convert_pdf
import shutil
import os

router = APIRouter()


@router.post("/pdf")
def invoke(uploaded_file: UploadFile = File(...)):
    try:
        file_directory = "files"
        os.makedirs(file_directory, exist_ok=True)
        file_location = f"files/{uploaded_file.filename}"
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(uploaded_file.file, file_object)
        handle_pdf(file_location)
    except Exception as e:
        return {"error": str(e)}
    finally:
        uploaded_file.file.close()
    return {"message": f"Successfully uploaded"}
