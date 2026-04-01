from typing import Any, Optional, List
from fastapi import APIRouter, Query

from app.client import product as product_client

router = APIRouter(tags=["商品"])


@router.get("/get_category")
async def get_category() -> Any:
    """获取系统品类"""
    return await product_client.goodcang_product.get_category()


@router.get("/get_declare_commodity_name_list")
async def get_declare_commodity_name_list() -> Any:
    """获取建议中文申报品名"""
    return await product_client.goodcang_product.get_declare_commodity_name_list()


@router.get("/get_material_list")
async def get_material_list() -> Any:
    """获取建议材质"""
    return await product_client.goodcang_product.get_material_list()


@router.get("/get_product_sku_list")
async def get_product_sku_list(
    page: int = Query(1, ge=1, description="查询页数"),
    page_size: int = Query(10, ge=1, le=200, description="每页显示的SKU数量"),
    product_sku: Optional[str] = Query(None, description="SKU"),
    product_sku_arr: Optional[List[str]] = Query(None, description="多个SKU数组"),
    product_update_time_from: Optional[str] = Query(None, description="修改开始时间"),
    product_update_time_to: Optional[str] = Query(None, description="修改结束时间"),
) -> Any:
    """获取商品列表"""
    return await product_client.goodcang_product.get_product_sku_list(
        page=page,
        page_size=page_size,
        product_sku=product_sku,
        product_sku_arr=product_sku_arr,
        product_update_time_from=product_update_time_from,
        product_update_time_to=product_update_time_to,
    )


@router.post("/serial_number_list")
async def serial_number_list(
    code_type: int = Query(
        1, description="查询类型: 1序列号, 2商品编码, 3订单号, 4序列号集成码, 5入库单号"
    ),
    status: Optional[int] = Query(
        None, description="状态: 0待收货, 1待出库, 2已出库, 3已废弃"
    ),
    code_value: Optional[str] = Query(None, description="查询值"),
    time_type: int = Query(
        1, description="查询时间类型: 1创建时间, 3出库时间, 4废弃时间"
    ),
    start_time: Optional[str] = Query(None, description="开始时间"),
    end_time: Optional[str] = Query(None, description="结束时间"),
    page: int = Query(1, ge=1, description="分页页码"),
    page_size: int = Query(100, description="分页数量"),
) -> Any:
    """获取序列号列表"""
    return await product_client.goodcang_product.serial_number_list(
        code_type=code_type,
        status=status,
        code_value=code_value,
        time_type=time_type,
        start_time=start_time,
        end_time=end_time,
        page=page,
        page_size=page_size,
    )
