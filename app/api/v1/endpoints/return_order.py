from typing import Any, Optional
from fastapi import APIRouter, Query

from app.client import return_order as return_order_client

router = APIRouter(tags=["退货单"])


@router.get("/search")
async def search(
    reference_no: Optional[str] = Query(None, description="参考号"),
    asro_codes: Optional[str] = Query(None, description="退件单号"),
) -> Any:
    """退货单查询"""
    return await return_order_client.goodcang_return_order.search(
        reference_no=reference_no,
        asro_codes=asro_codes,
    )


@router.get("/list")
async def get_list(
    current_page: int = Query(1, description="当前页"),
    page_size: int = Query(10, description="每页数据长度"),
    start_time: Optional[str] = Query(None, description="创建开始时间"),
    end_time: Optional[str] = Query(None, description="创建结束时间"),
    start_update_time: Optional[str] = Query(None, description="修改开始时间"),
    end_update_time: Optional[str] = Query(None, description="修改结束时间"),
    asro_status: Optional[str] = Query(None, description="退件状态"),
    cass_type: Optional[str] = Query(None, description="退件类型"),
    asro_codes: Optional[str] = Query(None, description="退件单号"),
) -> Any:
    """退货单列表"""
    return await return_order_client.goodcang_return_order.list(
        current_page=current_page,
        page_size=page_size,
        start_time=start_time,
        end_time=end_time,
        start_update_time=start_update_time,
        end_update_time=end_update_time,
        asro_status=asro_status,
        cass_type=cass_type,
        asro_codes=asro_codes,
    )


@router.get("/unauthorized_list")
async def unauthorized_list(
    current_page: int = Query(1, description="当前页"),
    page_size: int = Query(10, description="每页数据长度"),
    start_time: Optional[str] = Query(None, description="创建开始时间"),
    end_time: Optional[str] = Query(None, description="创建结束时间"),
) -> Any:
    """未预报退件列表"""
    return await return_order_client.goodcang_return_order.unauthorized_list(
        current_page=current_page,
        page_size=page_size,
        start_time=start_time,
        end_time=end_time,
    )


@router.get("/claim_order_list")
async def claim_order_list(
    current_page: int = Query(1, description="当前页"),
    page_size: int = Query(10, description="每页数据长度"),
    start_time: Optional[str] = Query(None, description="创建开始时间"),
    end_time: Optional[str] = Query(None, description="创建结束时间"),
    claim_status: Optional[int] = Query(None, description="索赔状态"),
) -> Any:
    """索赔单列表"""
    return await return_order_client.goodcang_return_order.claim_order_list(
        current_page=current_page,
        page_size=page_size,
        start_time=start_time,
        end_time=end_time,
        claim_status=claim_status,
    )


@router.get("/get_service_config")
async def get_service_config() -> Any:
    """获取退件服务配置"""
    return await return_order_client.goodcang_return_order.get_service_config()


@router.get("/claim_order_details")
async def claim_order_details(
    claim_code: str = Query(..., description="索赔单号"),
) -> Any:
    """索赔单详情"""
    return await return_order_client.goodcang_return_order.claim_order_details(
        claim_code=claim_code,
    )
