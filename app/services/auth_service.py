from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.crud_user import crud_user
from app.schemas.user import UserCreate, UserLogin, UserOut, UserUpdate, UserRegister


class AuthService:
    async def register(self, db: AsyncSession, *, obj_in: UserRegister) -> UserOut:
        exists_user = await crud_user.get_by_username(db, username=obj_in.username)
        if exists_user:
            raise HTTPException(
                status_code=400, detail=f"用户名 {obj_in.username} 已存在"
            )

        create_data = UserCreate(**obj_in.model_dump())
        db_obj = await crud_user.create(db=db, obj_in=create_data)
        return UserOut.model_validate(db_obj)

    async def login(self, db: AsyncSession, *, obj_in: UserLogin) -> UserOut:
        db_obj = await crud_user.get_by_username(db, username=obj_in.username)
        if not db_obj or db_obj.password != obj_in.password:
            raise HTTPException(status_code=400, detail="用户名或密码错误")
        return UserOut.model_validate(db_obj)

    async def get_profile(self, db: AsyncSession, *, user_id: int) -> UserOut:
        db_obj = await crud_user.get(db, id=user_id)
        if not db_obj:
            raise HTTPException(status_code=404, detail=f"用户ID {user_id} 不存在")
        return UserOut.model_validate(db_obj)

    async def update_profile(
        self, db: AsyncSession, *, user_id: int, obj_in: UserUpdate
    ) -> UserOut:
        db_obj = await crud_user.get(db, id=user_id)
        if not db_obj:
            raise HTTPException(status_code=404, detail=f"用户ID {user_id} 不存在")

        updated_obj = await crud_user.update(db=db, db_obj=db_obj, obj_in=obj_in)
        return UserOut.model_validate(updated_obj)


auth_service = AuthService()
