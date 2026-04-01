from typing import Any, Optional, List
from fastapi import APIRouter, Query

from app.client import assistant as assistant_client

router = APIRouter(tags=["查件助手"])


@router.post("/logistic_ticket_list")
async def logistic_ticket_list(
    page: int = Query(1, ge=1, description="分页页码"),
    page_size: int = Query(20, ge=1, le=200, description="分页数量"),
    code_type: Optional[str] = Query(None, description="查单类型"),
    code_value_list: Optional[List[str]] = Query(None, description="单号值数组"),
    io_status: Optional[int] = Query(None, description="查件状态"),
    trail_status: Optional[str] = Query(None, description="轨迹状态"),
    warehouse_code: Optional[str] = Query(None, description="仓库编码"),
    sm_code: Optional[str] = Query(None, description="物流方式编码"),
    platform: Optional[str] = Query(None, description="销售平台"),
    it_type_id: Optional[int] = Query(None, description="查件类型ID"),
    time_type: Optional[str] = Query(None, description="时间类型"),
    time_start: Optional[str] = Query(None, description="开始时间"),
    time_end: Optional[str] = Query(None, description="结束时间"),
) -> Any:
    """获取查件列表"""
    return await assistant_client.goodcang_assistant.logistic_ticket_list(
        page=page,
        page_size=page_size,
        code_type=code_type,
        code_value_list=code_value_list,
        io_status=io_status,
        trail_status=trail_status,
        warehouse_code=warehouse_code,
        sm_code=sm_code,
        platform=platform,
        it_type_id=it_type_id,
        time_type=time_type,
        time_start=time_start,
        time_end=time_end,
    )


@router.post("/logistic_ticket_type_list")
async def logistic_ticket_type_list(
    sm_code: Optional[str] = Query(None, description="物流方式编码"),
) -> Any:
    """获取查件单类型列表"""
    return await assistant_client.goodcang_assistant.logistic_ticket_type_list(
        sm_code=sm_code,
    )


@router.post("/logistic_ticket_detail")
async def logistic_ticket_detail(
    io_code: str = Query(..., description="查件单号"),
) -> Any:
    """获取查件单详情"""
    return await assistant_client.goodcang_assistant.logistic_ticket_detail(
        io_code=io_code,
    )
