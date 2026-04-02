from typing import Any, Optional, List
from fastapi import APIRouter, Query

from app.services.inventory_service import inventory_service

router = APIRouter(tags=["库存"])


@router.get("/get_product_inventory")
async def get_product_inventory(
    page: int = Query(1, ge=1, description="当前页"),
    page_size: int = Query(10, ge=1, le=200, description="每页数据长度"),
    product_sku: Optional[str] = Query(None, description="商品编码"),
    product_sku_arr: Optional[List[str]] = Query(None, description="多个SKU数组"),
    warehouse_code: Optional[str] = Query(None, description="仓库代码"),
    warehouse_code_arr: Optional[List[str]] = Query(
        None, description="多个仓库代码数组"
    ),
) -> Any:
    """获取库存"""
    return await inventory_service.get_product_inventory(
        page=page,
        page_size=page_size,
        product_sku=product_sku,
        product_sku_arr=product_sku_arr,
        warehouse_code=warehouse_code,
        warehouse_code_arr=warehouse_code_arr,
    )


@router.get("/get_inventory_log")
async def get_inventory_log(
    page: int = Query(1, ge=1, description="当前页"),
    page_size: int = Query(10, ge=1, le=200, description="每页数据长度"),
    warehouse_code: Optional[str] = Query(None, description="仓库代码"),
    application_code: Optional[str] = Query(None, description="操作类型"),
    reference_no_list: Optional[List[str]] = Query(None, description="操作单号数组"),
    product_sku_list: Optional[List[str]] = Query(None, description="多个SKU数组"),
    create_date_from: Optional[str] = Query(None, description="操作开始时间"),
    create_date_end: Optional[str] = Query(None, description="操作结束时间"),
) -> Any:
    """获取库存动态列表"""
    return await inventory_service.get_inventory_log(
        page=page,
        page_size=page_size,
        warehouse_code=warehouse_code,
        application_code=application_code,
        reference_no_list=reference_no_list,
        product_sku_list=product_sku_list,
        create_date_from=create_date_from,
        create_date_end=create_date_end,
    )


@router.post("/inventory_age_list")
async def inventory_age_list(
    page: int = Query(1, ge=1, description="分页页码"),
    page_size: int = Query(20, ge=1, le=200, description="分页数量"),
    product_sku_list: Optional[List[str]] = Query(None, description="商品编码列表"),
    product_title: Optional[str] = Query(None, description="商品名称"),
    product_title_en: Optional[str] = Query(None, description="商品英文名称"),
    fifo_time_from: Optional[str] = Query(None, description="上架时间起始值"),
    fifo_time_to: Optional[str] = Query(None, description="上架时间末位值"),
    age_from: Optional[int] = Query(None, description="库龄起始值"),
    age_to: Optional[int] = Query(None, description="库龄末位值"),
    quantity_from: Optional[int] = Query(None, description="在库库存起始值"),
    quantity_to: Optional[int] = Query(None, description="在库库存末位值"),
    warning_age_type: Optional[int] = Query(
        None, description="库龄预警: 1超出, 2未超出"
    ),
    warehouse_code: Optional[str] = Query(None, description="仓库代码"),
) -> Any:
    """获取库龄列表"""
    return await inventory_service.inventory_age_list(
        page=page,
        page_size=page_size,
        product_sku_list=product_sku_list,
        product_title=product_title,
        product_title_en=product_title_en,
        fifo_time_from=fifo_time_from,
        fifo_time_to=fifo_time_to,
        age_from=age_from,
        age_to=age_to,
        quantity_from=quantity_from,
        quantity_to=quantity_to,
        warning_age_type=warning_age_type,
        warehouse_code=warehouse_code,
    )
