from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import UserORM
import uuid

class UserRepository:
    @classmethod
    async def create_user(cls, db: AsyncSession):
        new_user_id = str(uuid.uuid4())
        new_user = UserORM(user_id=new_user_id)
        db.add(new_user)
        await db.commit()
        return new_user_id
