from typing import Any, Optional, List
from fastapi import APIRouter, Query

from app.client import inbound_order as inbound_order_client

router = APIRouter(tags=["入库单"])


@router.get("/get_vat_list")
async def get_vat_list(
    page: int = Query(1, description="当前页"),
    page_size: int = Query(10, description="每页数据长度"),
) -> Any:
    """获取进出口商列表"""
    return await inbound_order_client.goodcang_inbound_order.get_vat_list(
        page=page,
        page_size=page_size,
    )


@router.get("/get_smcode_twc_to_warehouse")
async def get_smcode_twc_to_warehouse() -> Any:
    """获取物流产品与目的仓中转仓"""
    return (
        await inbound_order_client.goodcang_inbound_order.get_smcode_twc_to_warehouse()
    )


@router.get("/get_grn_list")
async def get_grn_list(
    page: int = Query(1, ge=1, description="当前页"),
    page_size: int = Query(10, ge=1, le=100, description="每页数据长度"),
    receiving_code_arr: Optional[List[str]] = Query(
        None, description="多个入库单号数组"
    ),
    create_date_from: Optional[str] = Query(None, description="创建开始日期"),
    create_date_to: Optional[str] = Query(None, description="创建结束日期"),
    modify_date_from: Optional[str] = Query(None, description="修改开始时间"),
    modify_date_to: Optional[str] = Query(None, description="修改结束时间"),
    is_rollover: Optional[int] = Query(None, description="是否仓库装箱商品: 0否, 1是"),
) -> Any:
    """获取入库单列表"""
    return await inbound_order_client.goodcang_inbound_order.get_grn_list(
        page=page,
        page_size=page_size,
        receiving_code_arr=receiving_code_arr,
        create_date_from=create_date_from,
        create_date_to=create_date_to,
        modify_date_from=modify_date_from,
        modify_date_to=modify_date_to,
        is_rollover=is_rollover,
    )


@router.get("/get_grn_detail")
async def get_grn_detail(
    receiving_code: str = Query(..., description="入库单号"),
) -> Any:
    """获取入库单明细"""
    return await inbound_order_client.goodcang_inbound_order.get_grn_detail(
        receiving_code=receiving_code,
    )


@router.get("/get_batch")
async def get_batch(
    receiving_code: str = Query(..., description="入库单号"),
) -> Any:
    """获取上架批次"""
    return await inbound_order_client.goodcang_inbound_order.get_batch(
        receiving_code=receiving_code,
    )


@router.get("/get_receipt_batch")
async def get_receipt_batch(
    receiving_code: str = Query(..., description="入库单号"),
) -> Any:
    """获取收货批次"""
    return await inbound_order_client.goodcang_inbound_order.get_receipt_batch(
        receiving_code=receiving_code,
    )


@router.get("/cars_model")
async def cars_model() -> Any:
    """获取车型"""
    return await inbound_order_client.goodcang_inbound_order.cars_model()


@router.post("/get_clearance_document")
async def get_clearance_document(
    receiving_list: List[str] = Query(..., description="入库单号数组"),
) -> Any:
    """获取清关文件上传状态"""
    return await inbound_order_client.goodcang_inbound_order.get_clearance_document(
        receiving_list=receiving_list,
    )
