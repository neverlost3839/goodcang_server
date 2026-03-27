from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.common import PaginatedResponse, Response
from app.schemas.order import OrderCreate, OrderOut, OrderUpdate
from app.services.order_service import order_service

router = APIRouter()


@router.get("/get_list", response_model=PaginatedResponse[OrderOut])
async def get_list(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    code: Optional[str] = None,
    product_id: Optional[int] = None,
    username: Optional[str] = None,
    status: Optional[str] = None,
    updated_at_from: Optional[datetime] = None,
    updated_at_to: Optional[datetime] = None,
    db: AsyncSession = Depends(get_db),
):
    """获取订单列表（分页、筛选）"""
    result = await order_service.list(
        db,
        page=page,
        page_size=page_size,
        code=code,
        product_id=product_id,
        username=username,
        status=status,
        updated_at_from=updated_at_from,
        updated_at_to=updated_at_to,
    )
    return PaginatedResponse(data=result)


@router.get("/get_detail", response_model=Response[OrderOut])
async def get_detail(
    id: int = Query(..., description="订单ID"),
    db: AsyncSession = Depends(get_db),
):
    """获取订单详情"""
    result = await order_service.get(db, id=id)
    return Response(data=result)


@router.post("/create", response_model=Response[OrderOut])
async def create(
    obj_in: OrderCreate,
    db: AsyncSession = Depends(get_db),
):
    """创建订单"""
    result = await order_service.create(db, obj_in=obj_in)
    return Response(data=result)


@router.post("/update", response_model=Response[OrderOut])
async def update(
    id: int = Query(..., description="订单ID"),
    obj_in: OrderUpdate = ...,
    db: AsyncSession = Depends(get_db),
):
    """更新订单"""
    result = await order_service.update(db, id=id, obj_in=obj_in)
    return Response(data=result)


@router.post("/delete", response_model=Response[bool])
async def delete(
    id: int = Query(..., description="订单ID"),
    db: AsyncSession = Depends(get_db),
):
    """删除订单"""
    result = await order_service.delete(db, id=id)
    return Response(data=result)
