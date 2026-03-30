from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    async def get_by_username(self, db: AsyncSession, *, username: str) -> User | None:
        result = await db.execute(
            select(self.model).where(self.model.username == username)
        )
        return result.scalar_one_or_none()


crud_user = CRUDUser(User)
