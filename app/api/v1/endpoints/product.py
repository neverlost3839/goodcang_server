from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Body, Depends, Path, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.common import PaginatedResponse, Response
from app.schemas.product import ProductCreate, ProductOut, ProductUpdate
from app.services.product_service import product_service

router = APIRouter()


@router.get("/get_list", response_model=PaginatedResponse[ProductOut])
async def get_list(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    product_sku: Optional[str] = None,
    product_name_cn: Optional[str] = None,
    product_name_en: Optional[str] = None,
    product_brand: Optional[str] = None,
    verify: Optional[int] = None,
    updated_at_from: Optional[datetime] = None,
    updated_at_to: Optional[datetime] = None,
    db: AsyncSession = Depends(get_db),
):
    result = await product_service.list(
        db,
        page=page,
        page_size=page_size,
        product_sku=product_sku,
        product_name_cn=product_name_cn,
        product_name_en=product_name_en,
        product_brand=product_brand,
        verify=verify,
        updated_at_from=updated_at_from,
        updated_at_to=updated_at_to,
    )
    return PaginatedResponse(data=result)


@router.get("/get_detail", response_model=Response[ProductOut])
async def get_detail(
    id: int = Query(..., description="商品ID"),
    db: AsyncSession = Depends(get_db),
):
    result = await product_service.get(db, id=id)
    return Response(data=result)


@router.post("/create", response_model=Response[ProductOut])
async def create(
    obj_in: ProductCreate,
    db: AsyncSession = Depends(get_db),
):
    result = await product_service.create(db, obj_in=obj_in)
    return Response(data=result)


@router.put("/update/{id}", response_model=Response[ProductOut])
async def update(
    id: int = Path(..., description="商品ID"),
    obj_in: ProductUpdate = Body(...),
    db: AsyncSession = Depends(get_db),
):
    result = await product_service.update(db, id=id, obj_in=obj_in)
    return Response(data=result)


@router.delete("/delete", response_model=Response[bool])
async def delete(
    id: int = Query(..., description="商品ID"),
    db: AsyncSession = Depends(get_db),
):
    result = await product_service.delete(db, id=id)
    return Response(data=result)
