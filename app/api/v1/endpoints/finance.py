from typing import Any, Optional
from fastapi import APIRouter, Query

from app.client import finance as finance_client

router = APIRouter(tags=["财务"])


@router.post("/get_wh_inventory_storage")
async def get_wh_inventory_storage(
    page: int = Query(1, ge=1, description="查询页数"),
    page_size: int = Query(10, ge=1, le=100, description="每页显示数量"),
    wis_code: Optional[str] = Query(None, description="单号"),
    ow_id_charge: Optional[str] = Query(None, description="仓库代码"),
    dateFrom: Optional[str] = Query(None, description="开始时间"),
    dateTo: Optional[str] = Query(None, description="结束时间"),
) -> Any:
    """获取仓租信息 (V1版本)"""
    return await finance_client.goodcang_finance.get_wh_inventory_storage(
        page=page,
        page_size=page_size,
        wis_code=wis_code,
        ow_id_charge=ow_id_charge,
        dateFrom=dateFrom,
        dateTo=dateTo,
    )


@router.post("/get_wh_inventory_storage_detail")
async def get_wh_inventory_storage_detail(
    wis_code: str = Query(..., description="仓租单号"),
) -> Any:
    """获取仓租明细 (V1版本)"""
    return await finance_client.goodcang_finance.get_wh_inventory_storage_detail(
        wis_code=wis_code,
    )


@router.post("/cost_flow_list")
async def cost_flow_list(
    page: int = Query(1, ge=1, description="当前分页"),
    page_size: int = Query(20, ge=1, le=200, description="分页数量"),
    happen_start_time: str = Query(..., description="发生开始时间"),
    happen_end_time: str = Query(..., description="发生结束时间"),
    flow_type: Optional[str] = Query(None, description="流水类型"),
    number_type: Optional[str] = Query(None, description="单号类型"),
    order_number: Optional[str] = Query(None, description="单号值"),
    account_code: Optional[str] = Query(None, description="账户编号"),
    business_type: Optional[int] = Query(None, description="业务类型"),
    types_of_fee: Optional[str] = Query(None, description="费用类型"),
    currency_code: Optional[str] = Query(None, description="币种"),
    charge_type: Optional[int] = Query(None, description="出账状态"),
    next_page_token: Optional[str] = Query(None, description="下一页token"),
    prev_page_token: Optional[str] = Query(None, description="上一页token"),
) -> Any:
    """获取费用流水 (V2版本)"""
    return await finance_client.goodcang_finance.cost_flow_list(
        page=page,
        page_size=page_size,
        happen_start_time=happen_start_time,
        happen_end_time=happen_end_time,
        flow_type=flow_type,
        number_type=number_type,
        order_number=order_number,
        account_code=account_code,
        business_type=business_type,
        types_of_fee=types_of_fee,
        currency_code=currency_code,
        charge_type=charge_type,
        next_page_token=next_page_token,
        prev_page_token=prev_page_token,
    )


@router.post("/top_up_record")
async def top_up_record(
    code_field: str = Query(..., description="单号类型"),
    page: int = Query(1, ge=1, description="分页页码"),
    page_size: int = Query(20, ge=1, le=200, description="分页数量"),
    begin_add_time: Optional[str] = Query(None, description="充值开始日期"),
    end_add_time: Optional[str] = Query(None, description="充值结束日期"),
    code_value: Optional[str] = Query(None, description="字段值"),
    transaction_type: Optional[int] = Query(None, description="充值交易类型"),
    transaction_gd_status: Optional[int] = Query(None, description="交易状态"),
    bank_name: Optional[str] = Query(None, description="付款银行名称"),
    account_code: Optional[str] = Query(None, description="账户编码"),
) -> Any:
    """获取充值明细 (V2版本)"""
    return await finance_client.goodcang_finance.top_up_record(
        code_field=code_field,
        page=page,
        page_size=page_size,
        begin_add_time=begin_add_time,
        end_add_time=end_add_time,
        code_value=code_value,
        transaction_type=transaction_type,
        transaction_gd_status=transaction_gd_status,
        bank_name=bank_name,
        account_code=account_code,
    )
