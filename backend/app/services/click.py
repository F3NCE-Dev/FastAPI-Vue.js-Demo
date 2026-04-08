from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import UserORM

class ClickRepository:
    @classmethod
    async def increment_click(cls, user_id: str, db: AsyncSession) -> None:
        result = await db.execute(select(UserORM).where(UserORM.user_id == user_id))
        user = result.scalar_one_or_none()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        user.clicks += 1
        await db.commit()

    @classmethod
    async def get_clicks(cls, user_id: str, db: AsyncSession) -> int:
        result = await db.execute(select(UserORM).where(UserORM.user_id == user_id))
        user = result.scalar_one_or_none()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        return user.clicks
