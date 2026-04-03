from fastapi import APIRouter
from app.services.text import TextService
from app.schemas.response import TextResponse

router = APIRouter(prefix="/text", tags=["Text Management"])

@router.get("", response_model=TextResponse)
def get_text():
    return {"text": TextService.get_text()}
