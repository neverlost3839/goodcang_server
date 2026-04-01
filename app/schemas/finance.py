from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field


class WhInventoryStorageItem(BaseModel):
    wis_code: str = Field(..., description="单号")
    wp_settlement_cycle: str = Field(..., description="结算周期")
    ow_id_charge: str = Field(..., description="仓库代码")
    is_date: str = Field(..., description="发生时间")
    isdb_volume: str = Field(..., description="体积(m3)")
    is_amount: str = Field(..., description="计费总金额")
    currency_code: str = Field(..., description="计费货币")
    note: Optional[str] = Field(None, description="备注")

    class Config:
        from_attributes = True


class WhInventoryStorageOut(BaseModel):
    ask: str = Field(..., description="Success成功,其它值失败")
    message: str = Field(..., description="文本消息")
    count: Optional[str] = Field(None, description="总数量")
    data: List[WhInventoryStorageItem] = Field(default_factory=list, description="数据")

    class Config:
        from_attributes = True


class WarehouseRentDetailItem(BaseModel):
    wis_code: str = Field(..., description="单号")
    product_barcode: str = Field(..., description="产品代码")
    product_name: str = Field(..., description="产品名称")
    reference_no: Optional[str] = Field(None, description="参考编号")
    charge_date: str = Field(..., description="计费时间")
    putaway_date: str = Field(..., description="上架时间")
    length: str = Field(..., description="长(cm)")
    width: str = Field(..., description="宽(cm)")
    height: str = Field(..., description="高(cm)")
    quantity: str = Field(..., description="数量")
    volume: str = Field(..., description="体积(m3)")
    bill_amount: str = Field(..., description="计费金额")
    bill_currency_code: str = Field(..., description="计费币种")
    settlement_amount: str = Field(..., description="结算金额")
    settlement_currency_code: str = Field(..., description="结算币种")
    day: str = Field(..., description="库龄(天)")
    peak_season_surcharge: str = Field(..., description="旺季附加费")
    isdb_amount: str = Field(..., description="仓租金额")
    warehouse_code: str = Field(..., description="仓库代码")
    storage_shape: str = Field(..., description="存储物理形态")
    bill_unit: str = Field(..., description="计费单位")

    class Config:
        from_attributes = True


class WhInventoryStorageDetailOut(BaseModel):
    ask: str = Field(..., description="Success成功,其它值失败")
    message: str = Field(..., description="文本消息")
    data: List[WarehouseRentDetailItem] = Field(
        default_factory=list, description="仓租明细"
    )
    count: Optional[int] = Field(None, description="总数量")

    class Config:
        from_attributes = True


class CostStatementItem(BaseModel):
    order_number: str = Field(..., description="单号")
    reference_number: Optional[str] = Field(None, description="交易流水号")
    account_code: str = Field(..., description="账户编码")
    types_of_fee_name_cn: Optional[str] = Field(None, description="费用代码中文名称")
    types_of_fee_name_en: Optional[str] = Field(None, description="费用代码英文名称")
    flow_type: str = Field(..., description="流水类型")
    flow_type_text: str = Field(..., description="流水类型文本")
    amount: str = Field(..., description="发生金额")
    currency_code: str = Field(..., description="币种")
    currency_balance: str = Field(..., description="当前账户币种余额")
    exchange_rate: Optional[str] = Field(None, description="汇率")
    types_of_fee_text: Optional[str] = Field(None, description="费用类型编码描述")
    charge_type_text: Optional[str] = Field(None, description="出账状态")
    add_time: str = Field(..., description="发生时间")
    source: Optional[str] = Field(None, description="来源")
    types_of_fee: Optional[str] = Field(None, description="费用类型")
    charge_type: Optional[int] = Field(None, description="出账状态")
    business_type: Optional[str] = Field(None, description="业务类型")
    business_type_text: Optional[str] = Field(None, description="业务类型文本")
    remark: Optional[str] = Field(None, description="备注")
    id: Optional[str] = Field(None, description="ID")

    class Config:
        from_attributes = True


class CostStatementListData(BaseModel):
    total: int = Field(..., description="总数量")
    list: List[CostStatementItem] = Field(default_factory=list, description="列表数据")
    next_page_token: Optional[str] = Field(None, description="下一页token")
    prev_page_token: Optional[str] = Field(None, description="上一页token")

    class Config:
        from_attributes = True


class CostStatementListOut(BaseModel):
    code: int = Field(..., description="0成功,其它值失败")
    message: str = Field(..., description="文本消息")
    data: Optional[CostStatementListData] = Field(None, description="数据")

    class Config:
        from_attributes = True


class TopUpRecordItem(BaseModel):
    order_number: str = Field(..., description="单号")
    reference_number: Optional[str] = Field(None, description="银行流水号")
    account_code: str = Field(..., description="账户编码")
    sign_body_name: Optional[str] = Field(None, description="签约主体名称")
    service_body_type: Optional[int] = Field(None, description="服务商类型")
    service_body_name: Optional[str] = Field(None, description="服务商名称")
    sign_business_type_list: List[int] = Field(
        default_factory=list, description="签约业务类型"
    )
    sign_business_type_text: Optional[str] = Field(None, description="签约业务类型文本")
    drawee: Optional[str] = Field(None, description="付款人")
    transaction_type: int = Field(..., description="充值交易类型")
    transaction_type_text: str = Field(..., description="充值交易类型文本")
    bank_name: Optional[str] = Field(None, description="付款银行名称")
    drawee_account: Optional[str] = Field(None, description="付款账号")
    transaction_status: int = Field(..., description="交易状态")
    transaction_status_text: str = Field(..., description="交易状态文本")
    register_amount: str = Field(..., description="登记金额")
    arrival_amount: str = Field(..., description="到账金额")
    currency_code: str = Field(..., description="币种")
    exchange: str = Field(..., description="汇率")
    add_time: str = Field(..., description="添加时间")
    service_charge: str = Field(..., description="服务费")
    recharge_code: str = Field(..., description="充值币种")
    actual_amount: str = Field(..., description="实际金额")
    remark: Optional[str] = Field(None, description="备注")
    serial_number: Optional[str] = Field(None, description="流水号")
    update_time: Optional[str] = Field(None, description="更新时间")

    class Config:
        from_attributes = True


class TopUpRecordData(BaseModel):
    total: int = Field(..., description="总数量")
    list: List[TopUpRecordItem] = Field(default_factory=list, description="列表数据")

    class Config:
        from_attributes = True


class TopUpRecordOut(BaseModel):
    code: int = Field(..., description="0成功,其它值失败")
    message: str = Field(..., description="文本消息")
    data: Optional[TopUpRecordData] = Field(None, description="数据")

    class Config:
        from_attributes = True
