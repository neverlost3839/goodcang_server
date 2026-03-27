from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.common import Response
from app.schemas.user import UserLogin, UserOut, UserProfileUpdate, UserRegister
from app.services.auth_service import auth_service

router = APIRouter()


@router.post("/register", response_model=Response[UserOut])
async def register(
    obj_in: UserRegister,
    db: AsyncSession = Depends(get_db),
):
    """注册账号"""
    result = await auth_service.register(db, obj_in=obj_in)
    return Response(data=result)


@router.post("/login", response_model=Response[UserOut])
async def login(
    obj_in: UserLogin,
    db: AsyncSession = Depends(get_db),
):
    """登录（示例版，不做加密和校验）"""
    result = await auth_service.login(db, obj_in=obj_in)
    return Response(data=result)


@router.get("/get_profile", response_model=Response[UserOut])
async def get_profile(
    user_id: int = Query(..., description="用户ID"),
    db: AsyncSession = Depends(get_db),
):
    """获取个人基础信息"""
    result = await auth_service.get_profile(db, user_id=user_id)
    return Response(data=result)


@router.post("/update_profile", response_model=Response[UserOut])
async def update_profile(
    user_id: int = Query(..., description="用户ID"),
    obj_in: UserProfileUpdate = ...,
    db: AsyncSession = Depends(get_db),
):
    """更新个人基础信息"""
    result = await auth_service.update_profile(db, user_id=user_id, obj_in=obj_in)
    return Response(data=result)
