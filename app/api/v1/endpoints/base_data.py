from typing import Any, Optional, List
from fastapi import APIRouter, Query

from app.client import base_data as base_data_client

router = APIRouter(tags=["基础数据"])


@router.get("/country")
async def get_country() -> Any:
    """获取国家/地区列表"""
    return await base_data_client.goodcang_base_data.get_country()


@router.get("/warehouse")
async def get_warehouse() -> Any:
    """获取系统仓库"""
    return await base_data_client.goodcang_base_data.get_warehouse()


@router.get("/shipping_method")
async def get_shipping_method(
    warehouse_code: Optional[str] = Query(None, description="尾程仓库代码"),
) -> Any:
    """获取物流产品"""
    return await base_data_client.goodcang_base_data.get_shipping_method(
        warehouse_code=warehouse_code
    )


@router.get("/account_list")
async def get_account_list() -> Any:
    """获取公司账户"""
    return await base_data_client.goodcang_base_data.get_account_list()


@router.post("/cost_type_list")
async def get_cost_type_list(
    sign_business_type: int = Query(..., description="业务类型: 0海外仓储, 1中转代发"),
) -> Any:
    """获取费用类型"""
    return await base_data_client.goodcang_base_data.cost_type_list(
        sign_business_type=sign_business_type
    )


@router.post("/fuel_rate_list")
async def get_fuel_rate_list(
    logistic_type: int = Query(..., description="物流类型: 0发货物流, 1退货物流"),
    sm_code: str = Query(..., description="物流产品编码"),
    begin_time: str = Query(..., description="起始生效时间"),
    end_time: str = Query(..., description="结束生效时间"),
    page: int = Query(1, ge=1, description="分页页码"),
    page_size: int = Query(10, ge=1, le=200, description="分页数量"),
) -> Any:
    """获取燃油费率"""
    return await base_data_client.goodcang_base_data.fuel_rate_list(
        logistic_type=logistic_type,
        sm_code=sm_code,
        begin_time=begin_time,
        end_time=end_time,
        page=page,
        page_size=page_size,
    )
