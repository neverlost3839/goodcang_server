from typing import Any, Optional, List
from fastapi import APIRouter, Query

from app.services.order_service import order_service

router = APIRouter(tags=["订单"])


@router.get("/get_order_by_code")
async def get_order_by_code(
    order_code: str = Query(..., description="订单号"),
) -> Any:
    """根据订单号获取单票订单信息"""
    return await order_service.get_order_by_code(
        order_code=order_code,
    )


@router.get("/get_order_list")
async def get_order_list(
    page: int = Query(1, ge=1, description="当前页"),
    page_size: int = Query(10, ge=1, le=100, description="每页数据长度"),
    order_status: Optional[str] = Query(
        None, description="订单状态: C待发货审核, W待发货, D已发货, H暂存"
    ),
    warehouse_code: Optional[str] = Query(None, description="仓库代码"),
    shipping_method: Optional[str] = Query(None, description="物流产品代码"),
    country_code: Optional[str] = Query(None, description="收件人国家"),
    reference_no: Optional[str] = Query(None, description="客户参考号"),
    order_code: Optional[str] = Query(None, description="订单号"),
    date_type: Optional[int] = Query(
        None, description="日期类型: 1创建时间, 2发货时间"
    ),
    date_from: Optional[str] = Query(None, description="开始日期"),
    date_to: Optional[str] = Query(None, description="结束日期"),
) -> Any:
    """获取订单列表"""
    return await order_service.get_order_list(
        page=page,
        page_size=page_size,
        order_status=order_status,
        warehouse_code=warehouse_code,
        shipping_method=shipping_method,
        country_code=country_code,
        reference_no=reference_no,
        order_code=order_code,
        date_type=date_type,
        date_from=date_from,
        date_to=date_to,
    )


@router.get("/get_draft_order_list")
async def get_draft_order_list(
    page: int = Query(1, ge=1, description="当前页"),
    page_size: int = Query(10, ge=1, le=100, description="每页数据长度"),
    warehouse_code: Optional[str] = Query(None, description="仓库代码"),
    reference_no: Optional[str] = Query(None, description="客户参考号"),
) -> Any:
    """获取草稿订单列表"""
    return await order_service.get_draft_order_list(
        page=page,
        page_size=page_size,
        warehouse_code=warehouse_code,
        reference_no=reference_no,
    )


@router.post("/batch_query_tracking_status")
async def batch_query_tracking_status(
    tracking_numbers: List[str] = Query(..., description="物流追踪号数组"),
) -> Any:
    """批量查询物流追踪状态"""
    return await order_service.batch_query_tracking_status(
        tracking_numbers=tracking_numbers,
    )
