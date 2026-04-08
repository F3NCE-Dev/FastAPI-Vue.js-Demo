from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column

class UserORM(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(unique=True, nullable=False)
    clicks: Mapped[int] = mapped_column(default=0)
