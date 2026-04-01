from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.common import PaginatedResponse, Response
from app.schemas.inventory import InventoryOut
from app.services.inventory_service import inventory_service

router = APIRouter()


@router.get("/get_list", response_model=PaginatedResponse[InventoryOut])
async def get_list(
    page: int = Query(1, ge=1, description="当前页码"),
    page_size: int = Query(20, ge=1, le=100, description="每页条数"),
    product_sku: Optional[str] = Query(None, description="商品SKU"),
    product_sku_arr: Optional[List[str]] = Query(None, description="多个商品SKU数组"),
    warehouse_code: Optional[str] = Query(None, description="仓库代码"),
    warehouse_code_arr: Optional[List[str]] = Query(
        None, description="多个仓库代码数组"
    ),
    db: AsyncSession = Depends(get_db),
):
    result = await inventory_service.list(
        db,
        page=page,
        page_size=page_size,
        product_sku=product_sku,
        product_sku_arr=product_sku_arr,
        warehouse_code=warehouse_code,
        warehouse_code_arr=warehouse_code_arr,
    )
    return PaginatedResponse(data=result)


@router.post("/sync", response_model=Response[dict])
async def sync(
    warehouse_code: Optional[str] = Query(None, description="仓库代码"),
    warehouse_code_arr: Optional[List[str]] = Query(
        None, description="多个仓库代码数组"
    ),
    product_sku: Optional[str] = Query(None, description="商品SKU"),
    product_sku_arr: Optional[List[str]] = Query(None, description="多个商品SKU数组"),
    db: AsyncSession = Depends(get_db),
):
    result = await inventory_service.sync(
        db,
        product_sku=product_sku,
        product_sku_arr=product_sku_arr,
        warehouse_code=warehouse_code,
        warehouse_code_arr=warehouse_code_arr,
    )
    return Response(data=result)
