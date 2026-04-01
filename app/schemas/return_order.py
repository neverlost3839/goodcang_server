from datetime import datetime
from typing import Optional, List, Any
from pydantic import BaseModel, Field


class ReturnOrderProductDetail(BaseModel):
    product_barcode: Optional[str] = Field(None, description="商品编码")
    product_sku: Optional[str] = Field(None, description="客户商品编码")
    sellable_qty: int = Field(default=0, description="良品数量")
    unsellable_qty: int = Field(default=0, description="不良品数量")
    destruction_qty: int = Field(default=0, description="销毁数量")
    sellable_detail: List[Any] = Field(default_factory=list, description="良品明细")
    unsellable_detail: List[Any] = Field(default_factory=list, description="不良品明细")
    destruction_detail: List[Any] = Field(default_factory=list, description="销毁明细")
    return_auth: int = Field(default=0, description="退件授权: 0否,1是")
    return_replacement_sku: Optional[str] = Field(None, description="换标编码")
    photo_list: Optional[List[str]] = Field(None, description="图片信息")

    class Config:
        from_attributes = True


class ReturnOrderFeeDetails(BaseModel):
    shipping_fee: Optional[float] = Field(None, description="运输费")
    operating_fee: Optional[float] = Field(None, description="操作费用")
    fuel_surcharge: Optional[float] = Field(None, description="燃油附加费")
    other_fee: Optional[float] = Field(None, description="其它费用")
    currency_code: Optional[str] = Field(None, description="币别")

    class Config:
        from_attributes = True


class ReturnOrderBase(BaseModel):
    asro_code: str = Field(..., max_length=32, description="退件单号")
    order_code: Optional[str] = Field(None, max_length=50, description="订单号")
    reference_no: Optional[str] = Field(None, max_length=50, description="参考号")

    asro_status: str = Field(
        default="0",
        max_length=10,
        description="退件状态: 0草稿,1已提交,4收货完成,5处理完成,6废弃,7处理中",
    )
    cass_type: str = Field(
        default="1",
        max_length=10,
        description="退件类型: 0服务商退件,1客户退件,2未预报退件",
    )

    asro_add_time: Optional[datetime] = Field(None, description="创建时间")
    asro_audit_time: Optional[datetime] = Field(None, description="审核时间")
    asro_putaway_time: Optional[datetime] = Field(None, description="上架完成时间")

    warehouse_code: str = Field(..., max_length=20, description="退件收货仓库")
    sm_type: str = Field(
        default="0", max_length=10, description="派送方式: 0代选物流,1自选物流"
    )
    collect_warehouse_code: Optional[str] = Field(
        None, max_length=20, description="集货区域仓编码"
    )

    service_type: int = Field(
        default=1, description="退货服务类型: 1退件质检,2退件销毁"
    )
    is_transit: int = Field(default=2, description="是否退回集货仓: 1是,2否")
    tracking_no: Optional[str] = Field(None, max_length=50, description="跟踪号")
    asro_reason: Optional[str] = Field(None, description="退件原因")

    sm_code: Optional[str] = Field(None, max_length=50, description="物流产品编码")
    as_length: float = Field(default=0.0, description="计费长")
    as_width: float = Field(default=0.0, description="计费宽")
    as_height: float = Field(default=0.0, description="计费高")
    charge_weight: float = Field(default=0.0, description="计费重")

    asro_note: Optional[str] = Field(None, description="客服留言")
    return_identification: int = Field(
        default=2, description="退件标识: 1谷仓发货退件,2非谷仓发货退件"
    )


class ReturnOrderCreate(ReturnOrderBase):
    pass


class ReturnOrderUpdate(BaseModel):
    asro_status: Optional[str] = Field(None, max_length=10, description="退件状态")
    cass_type: Optional[str] = Field(None, max_length=10, description="退件类型")
    asro_audit_time: Optional[datetime] = Field(None, description="审核时间")
    asro_putaway_time: Optional[datetime] = Field(None, description="上架完成时间")
    tracking_no: Optional[str] = Field(None, max_length=50, description="跟踪号")
    asro_reason: Optional[str] = Field(None, description="退件原因")
    asro_note: Optional[str] = Field(None, description="客服留言")


class ReturnOrderProductDetailOut(BaseModel):
    product_barcode: Optional[str] = Field(None, description="商品编码")
    product_sku: Optional[str] = Field(None, description="客户商品编码")
    sellable_qty: int = Field(default=0, description="良品数量")
    unsellable_qty: int = Field(default=0, description="不良品数量")
    destruction_qty: int = Field(default=0, description="销毁数量")
    sellable_detail: List[dict] = Field(default_factory=list, description="良品明细")
    unsellable_detail: List[dict] = Field(
        default_factory=list, description="不良品明细"
    )
    destruction_detail: List[dict] = Field(default_factory=list, description="销毁明细")
    return_auth: int = Field(default=0, description="退件授权: 0否,1是")
    return_replacement_sku: Optional[str] = Field(None, description="换标编码")
    photo_list: Optional[str] = Field(None, description="图片信息")

    class Config:
        from_attributes = True


class ReturnOrderOut(ReturnOrderBase):
    id: int = Field(..., description="退货单ID")
    product_detail: List[ReturnOrderProductDetailOut] = Field(
        default_factory=list, description="退件产品明细"
    )
    fee_details: Optional[ReturnOrderFeeDetails] = Field(None, description="费用详情")
    created_at: datetime = Field(..., description="创建时间")
    updated_at: datetime = Field(..., description="更新时间")

    class Config:
        from_attributes = True


class ReturnOrderSimpleOut(BaseModel):
    id: int = Field(..., description="退货单ID")
    asro_code: str = Field(..., description="退件单号")
    order_code: Optional[str] = Field(None, description="订单号")
    reference_no: Optional[str] = Field(None, description="参考号")
    asro_status: str = Field(..., description="退件状态")
    warehouse_code: str = Field(..., description="退件收货仓库")

    class Config:
        from_attributes = True


class ReturnOrderSearchRequest(BaseModel):
    reference_no: Optional[str] = Field(None, max_length=50, description="参考号")
    asro_codes: Optional[str] = Field(None, max_length=32, description="退件单号")

    class Config:
        from_attributes = True
