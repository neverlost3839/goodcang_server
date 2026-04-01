from typing import Any, Optional, List
from fastapi import APIRouter, Query

from app.client import plan_order as plan_order_client

router = APIRouter(tags=["计划单"])


@router.post("/list")
async def plan_order_list(
    page: int = Query(1, ge=1, description="分页页码"),
    page_size: int = Query(20, ge=1, le=200, description="分页数量"),
    order_status: Optional[int] = Query(None, description="计划单状态"),
    code_type: Optional[int] = Query(None, description="单号类型"),
    code_value_list: Optional[List[str]] = Query(None, description="单号值数组"),
    warehouse_code: Optional[str] = Query(None, description="发货仓库"),
    is_change_label: Optional[int] = Query(None, description="换标服务"),
    label_replacement_option: Optional[int] = Query(None, description="换标要求"),
    is_stick_label: Optional[int] = Query(None, description="贴标服务"),
    dest_warehouse_type: Optional[int] = Query(None, description="目的仓类型"),
    time_type: Optional[int] = Query(None, description="时间类型"),
    start_time: Optional[str] = Query(None, description="起始时间"),
    end_time: Optional[str] = Query(None, description="截止时间"),
) -> Any:
    """获取计划单列表"""
    return await plan_order_client.goodcang_plan_order.list(
        page=page,
        page_size=page_size,
        order_status=order_status,
        code_type=code_type,
        code_value_list=code_value_list,
        warehouse_code=warehouse_code,
        is_change_label=is_change_label,
        label_replacement_option=label_replacement_option,
        is_stick_label=is_stick_label,
        dest_warehouse_type=dest_warehouse_type,
        time_type=time_type,
        start_time=start_time,
        end_time=end_time,
    )


@router.post("/box_list")
async def plan_order_box_list(
    page: int = Query(1, ge=1, description="分页页码"),
    page_size: int = Query(20, ge=1, le=200, description="分页数量"),
    box_status: Optional[int] = Query(None, description="箱状态"),
    code_type: Optional[int] = Query(None, description="单号类型"),
    code_value_list: Optional[List[str]] = Query(None, description="单号值数组"),
    warehouse_code: Optional[str] = Query(None, description="发货仓库"),
    is_change_label: Optional[int] = Query(None, description="换标服务"),
    label_replacement_option: Optional[int] = Query(None, description="换标要求"),
    is_stick_label: Optional[int] = Query(None, description="贴标服务"),
    time_type: Optional[int] = Query(None, description="时间类型"),
    start_time: Optional[str] = Query(None, description="起始时间"),
    end_time: Optional[str] = Query(None, description="截止时间"),
) -> Any:
    """获取装箱列表"""
    return await plan_order_client.goodcang_plan_order.box_list(
        page=page,
        page_size=page_size,
        box_status=box_status,
        code_type=code_type,
        code_value_list=code_value_list,
        warehouse_code=warehouse_code,
        is_change_label=is_change_label,
        label_replacement_option=label_replacement_option,
        is_stick_label=is_stick_label,
        time_type=time_type,
        start_time=start_time,
        end_time=end_time,
    )
