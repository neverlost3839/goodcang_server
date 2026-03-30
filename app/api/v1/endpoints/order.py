from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Body, Depends, Path, Query
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
    reference_no: Optional[str] = None,
    platform: Optional[str] = None,
    warehouse_code: Optional[str] = None,
    country_code: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    email: Optional[str] = None,
    verify: Optional[int] = None,
    order_code: Optional[str] = None,
    updated_at_from: Optional[datetime] = None,
    updated_at_to: Optional[datetime] = None,
    db: AsyncSession = Depends(get_db),
):
    result = await order_service.list(
        db,
        page=page,
        page_size=page_size,
        reference_no=reference_no,
        platform=platform,
        warehouse_code=warehouse_code,
        country_code=country_code,
        name=name,
        phone=phone,
        email=email,
        verify=verify,
        order_code=order_code,
        updated_at_from=updated_at_from,
        updated_at_to=updated_at_to,
    )
    return PaginatedResponse(data=result)


@router.get("/get_detail", response_model=Response[OrderOut])
async def get_detail(
    id: int = Query(..., description="订单ID"),
    db: AsyncSession = Depends(get_db),
):
    result = await order_service.get(db, id=id)
    return Response(data=result)


@router.post("/create", response_model=Response[OrderOut])
async def create(
    obj_in: OrderCreate,
    db: AsyncSession = Depends(get_db),
):
    result = await order_service.create(db, obj_in=obj_in)
    return Response(data=result)


@router.put("/update/{id}", response_model=Response[OrderOut])
async def update(
    id: int = Path(..., description="订单ID"),
    obj_in: OrderUpdate = Body(...),
    db: AsyncSession = Depends(get_db),
):
    result = await order_service.update(db, id=id, obj_in=obj_in)
    return Response(data=result)


@router.delete("/delete", response_model=Response[bool])
async def delete(
    id: int = Query(..., description="订单ID"),
    db: AsyncSession = Depends(get_db),
):
    result = await order_service.delete(db, id=id)
    return Response(data=result)
