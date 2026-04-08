from fastapi import APIRouter, Request, Response

from app.dependencies import DBSession
from app.services.user import UserRepository
from app.schemas.response import StatusResponse

router = APIRouter(prefix="/user", tags=["User Panel"])

@router.post("/init", response_model=StatusResponse)
async def init_user(request: Request, response: Response, db: DBSession):
    user_id = request.cookies.get("user_id")

    if not user_id:
        new_user_id = await UserRepository.create_user(db)
        response.set_cookie(key="user_id", value=new_user_id, httponly=True, secure=True, samesite="strict")
        return {"success": True, "detail": f"New user created, user_id: {new_user_id}"}
