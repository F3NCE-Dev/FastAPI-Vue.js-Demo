from fastapi import APIRouter, Request, HTTPException
from app.services.click import ClickRepository
from app.dependencies import DBSession
from app.schemas.response import StatusResponse

router = APIRouter(prefix="/click", tags=["Click Management"])

@router.get("", response_model=int)
async def get_click_count(db: DBSession, request: Request):
    user_id = request.cookies.get("user_id")
    if not user_id:
        raise HTTPException(status_code=400, detail="User ID not found in cookies")
    return await ClickRepository.get_clicks(user_id, db)

@router.post("", response_model=StatusResponse)
async def click(db: DBSession, request: Request):
    user_id = request.cookies.get("user_id")
    if not user_id:
        raise HTTPException(status_code=400, detail="User ID not found in cookies")
    await ClickRepository.increment_click(user_id, db)
    return {"success": True, "detail": "Click count incremented successfully"}
