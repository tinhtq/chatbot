from fastapi import APIRouter, Request
from app.services import Initializer
from pydantic import BaseModel

router = APIRouter()


class Query(BaseModel):
    prompt: str


@router.post("/ask")
def invoke(request: Query):
    try:
        model = Initializer()
        response = model.ask(request.prompt)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}
