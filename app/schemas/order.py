from datetime import datetime
from typing import Optional, List, Dict, Any

from pydantic import BaseModel, Field


class OrderItemBase(BaseModel):
    product_sku: str = Field(..., max_length=24, description="商品SKU")
    quantity: int = Field(..., ge=1, description="购买数量")
    transaction_id: Optional[str] = Field(None, max_length=50, description="平台交易号")
    item_id: Optional[str] = Field(None, max_length=50, description="平台商品行号")
    fba_product_code: Optional[str] = Field(
        None, max_length=20, description="FBA商品编码"
    )
    euro_terms_code: Optional[str] = Field(
        None, max_length=50, description="合规负责人编码"
    )
    label_replacement_qty: Optional[int] = Field(None, ge=0, description="内件总数量")
    product_declared_value: Optional[float] = Field(
        None, ge=0, description="申报价值 USD"
    )
    hs_code: Optional[str] = Field(None, max_length=10, description="海关编码 6-10位")


class OrderItemCreate(OrderItemBase):
    order_id: int = Field(..., description="关联order.id")


class OrderItemUpdate(BaseModel):
    product_sku: Optional[str] = Field(None, max_length=24, description="商品SKU")
    quantity: Optional[int] = Field(None, ge=1, description="购买数量")
    transaction_id: Optional[str] = Field(None, max_length=50, description="平台交易号")
    item_id: Optional[str] = Field(None, max_length=50, description="平台商品行号")
    fba_product_code: Optional[str] = Field(
        None, max_length=20, description="FBA商品编码"
    )
    euro_terms_code: Optional[str] = Field(
        None, max_length=50, description="合规负责人编码"
    )
    label_replacement_qty: Optional[int] = Field(None, ge=0, description="内件总数量")
    product_declared_value: Optional[float] = Field(
        None, ge=0, description="申报价值 USD"
    )
    hs_code: Optional[str] = Field(None, max_length=10, description="海关编码 6-10位")


class OrderItemOut(OrderItemBase):
    id: int = Field(..., description="订单明细ID")
    order_id: int = Field(..., description="关联order.id")
    created_at: datetime = Field(..., description="创建时间")
    updated_at: datetime = Field(..., description="更新时间")

    class Config:
        from_attributes = True


class OrderBase(BaseModel):
    reference_no: Optional[str] = Field(
        None, max_length=50, description="订单参考号/平台单号"
    )
    platform: Optional[str] = Field(
        default="OTHER", max_length=20, description="平台代码"
    )
    shipping_method: Optional[str] = Field(
        None, max_length=32, description="物流产品代码"
    )
    warehouse_code: Optional[str] = Field(
        None, max_length=32, description="发货仓库代码"
    )

    country_code: str = Field(..., max_length=2, description="国家二字码")
    province: str = Field(..., max_length=20, description="省/州")
    city: str = Field(..., max_length=32, description="城市")
    company: Optional[str] = Field(None, max_length=50, description="公司名称")
    address1: str = Field(..., max_length=50, description="地址1")
    address2: Optional[str] = Field(None, max_length=50, description="地址2")
    zipcode: str = Field(..., max_length=20, description="邮编")
    doorplate: Optional[str] = Field(None, max_length=20, description="门牌号")

    name: str = Field(..., max_length=48, description="收件人名")
    last_name: Optional[str] = Field(None, max_length=48, description="收件人姓")
    cell_phone: Optional[str] = Field(None, max_length=8, description="分机号")
    phone: Optional[str] = Field(None, max_length=20, description="联系电话")
    email: Optional[str] = Field(None, max_length=100, description="邮箱")

    order_desc: Optional[str] = Field(None, max_length=500, description="订单备注")
    customer_package_requirement: Optional[int] = Field(
        None, ge=1, le=4, description="包材要求"
    )

    verify: int = Field(default=0, ge=0, le=1, description="0草稿 1审核")
    is_shipping_method_not_allow_update: int = Field(
        default=1, ge=0, le=1, description="0可修改物流 1不可修改"
    )

    is_signature: int = Field(default=0, ge=0, le=1, description="0无需签名 1需签名")
    is_insurance: int = Field(default=0, ge=0, le=1, description="0无保险 1有保险")
    insurance_value: float = Field(default=0, ge=0, description="保额")

    fba_shipment_id: Optional[str] = Field(
        None, max_length=12, description="FBA Shipment ID"
    )
    property_label: Optional[str] = Field(
        None, max_length=50, description="平台模式 SFP等"
    )
    business_type: int = Field(default=0, ge=0, le=1, description="0仓配一体 1仓配分离")
    is_change_label: int = Field(default=1, ge=0, le=1, description="0不换标 1换标")
    age_detection: int = Field(
        default=0, ge=0, le=18, description="0不检测 16/18年龄检测"
    )

    lift_gate: int = Field(default=0, ge=0, le=1, description="0否 1是 LiftGate")
    attachment_ids: Optional[List[int]] = Field(None, description="附件ID数组")
    estimated_arrival_date: Optional[datetime] = Field(None, description="预计到货日期")
    estimated_arrival_time: Optional[str] = Field(
        None, max_length=20, description="到货时间段"
    )

    is_signature: int = Field(default=0, ge=0, le=1, description="0无需签名 1需签名")
    is_euro_label: Optional[int] = Field(None, ge=0, le=1, description="1贴标 0不贴标")
    is_warehouse_packing: int = Field(
        default=0, ge=0, le=1, description="0否 1仓库装箱"
    )


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    reference_no: Optional[str] = Field(
        None, max_length=50, description="订单参考号/平台单号"
    )
    platform: Optional[str] = Field(None, max_length=20, description="平台代码")
    shipping_method: Optional[str] = Field(
        None, max_length=32, description="物流产品代码"
    )
    warehouse_code: Optional[str] = Field(
        None, max_length=32, description="发货仓库代码"
    )

    country_code: Optional[str] = Field(None, max_length=2, description="国家二字码")
    province: Optional[str] = Field(None, max_length=20, description="省/州")
    city: Optional[str] = Field(None, max_length=32, description="城市")
    company: Optional[str] = Field(None, max_length=50, description="公司名称")
    address1: Optional[str] = Field(None, max_length=50, description="地址1")
    address2: Optional[str] = Field(None, max_length=50, description="地址2")
    zipcode: Optional[str] = Field(None, max_length=20, description="邮编")
    doorplate: Optional[str] = Field(None, max_length=20, description="门牌号")

    name: Optional[str] = Field(None, max_length=48, description="收件人名")
    last_name: Optional[str] = Field(None, max_length=48, description="收件人姓")
    cell_phone: Optional[str] = Field(None, max_length=8, description="分机号")
    phone: Optional[str] = Field(None, max_length=20, description="联系电话")
    email: Optional[str] = Field(None, max_length=100, description="邮箱")

    order_desc: Optional[str] = Field(None, max_length=500, description="订单备注")
    customer_package_requirement: Optional[int] = Field(
        None, ge=1, le=4, description="包材要求"
    )

    verify: Optional[int] = Field(None, ge=0, le=1, description="0草稿 1审核")
    is_shipping_method_not_allow_update: Optional[int] = Field(
        None, ge=0, le=1, description="0可修改物流 1不可修改"
    )

    is_signature: Optional[int] = Field(
        None, ge=0, le=1, description="0无需签名 1需签名"
    )
    is_insurance: Optional[int] = Field(None, ge=0, le=1, description="0无保险 1有保险")
    insurance_value: Optional[float] = Field(None, ge=0, description="保额")

    fba_shipment_id: Optional[str] = Field(
        None, max_length=12, description="FBA Shipment ID"
    )
    property_label: Optional[str] = Field(
        None, max_length=50, description="平台模式 SFP等"
    )
    business_type: Optional[int] = Field(
        None, ge=0, le=1, description="0仓配一体 1仓配分离"
    )
    is_change_label: Optional[int] = Field(
        None, ge=0, le=1, description="0不换标 1换标"
    )
    age_detection: Optional[int] = Field(
        None, ge=0, le=18, description="0不检测 16/18年龄检测"
    )

    lift_gate: Optional[int] = Field(None, ge=0, le=1, description="0否 1是 LiftGate")
    attachment_ids: Optional[List[int]] = Field(None, description="附件ID数组")
    estimated_arrival_date: Optional[datetime] = Field(None, description="预计到货日期")
    estimated_arrival_time: Optional[str] = Field(
        None, max_length=20, description="到货时间段"
    )

    sender_info: Optional[Dict[str, Any]] = Field(None, description="发件人信息")
    vat_change_info: Optional[Dict[str, Any]] = Field(None, description="欧盟税改信息")
    is_euro_label: Optional[int] = Field(None, ge=0, le=1, description="1贴标 0不贴标")
    vas: Optional[Dict[str, Any]] = Field(None, description="增值服务")

    is_warehouse_packing: Optional[int] = Field(
        None, ge=0, le=1, description="0否 1仓库装箱"
    )
    carton_info: Optional[Dict[str, Any]] = Field(None, description="FBA转仓单信息")
    truck_info: Optional[Dict[str, Any]] = Field(None, description="卡派渠道信息")


class OrderOut(OrderBase):
    id: int = Field(..., description="订单ID")
    sender_info: Optional[Dict[str, Any]] = Field(None, description="发件人信息")
    vat_change_info: Optional[Dict[str, Any]] = Field(None, description="欧盟税改信息")
    vas: Optional[Dict[str, Any]] = Field(None, description="增值服务")
    carton_info: Optional[Dict[str, Any]] = Field(None, description="FBA转仓单信息")
    truck_info: Optional[Dict[str, Any]] = Field(None, description="卡派渠道信息")
    order_code: Optional[str] = Field(None, description="谷仓返回订单号")
    is_deleted: int = Field(..., description="0未删除 1已删除")
    created_at: datetime = Field(..., description="创建时间")
    updated_at: datetime = Field(..., description="更新时间")

    class Config:
        from_attributes = True
