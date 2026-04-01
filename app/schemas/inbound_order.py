from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field


class CollectingAddress(BaseModel):
    ca_first_name: str = Field(..., max_length=50, description="揽收联系人-名")
    ca_last_name: str = Field(..., max_length=50, description="揽收联系人-姓")
    ca_contact_phone: str = Field(..., max_length=50, description="揽收联系人电话")
    ca_state: str = Field(..., max_length=50, description="揽收地址州/省份")
    ca_city: str = Field(..., max_length=50, description="揽收地址城市")
    ca_country_code: str = Field(..., max_length=50, description="揽收地址国家/地区")
    ca_zipcode: str = Field(..., max_length=50, description="揽收地址邮编")
    ca_address1: str = Field(..., max_length=50, description="揽收地址1")
    ca_address2: Optional[str] = Field(None, max_length=50, description="揽收地址2")


class ShiperAddress(BaseModel):
    sa_contacter: str = Field(..., max_length=50, description="联系人")
    sa_contact_phone: str = Field(..., max_length=50, description="联系电话")
    sa_country_code: str = Field(..., max_length=2, description="发件国家/地区简称")
    sa_state: str = Field(..., max_length=50, description="省/州")
    sa_city: str = Field(..., max_length=50, description="城市")
    sa_region: Optional[str] = Field(None, max_length=50, description="区")
    sa_address1: Optional[str] = Field(None, max_length=50, description="地址1")
    sa_address2: Optional[str] = Field(None, max_length=50, description="地址2")


class CustomersSendInfo(BaseModel):
    arrive_transfer_warehouse_time: Optional[datetime] = Field(
        None, description="预计到达中转仓时间"
    )
    company_name: Optional[str] = Field(None, max_length=50, description="快递公司名称")
    delivery_code: Optional[str] = Field(
        None, max_length=500, description="快递单号(多个用逗号隔开)"
    )
    plate_no: Optional[str] = Field(None, max_length=50, description="车牌号")
    driver_name: Optional[str] = Field(None, max_length=50, description="司机姓名")
    driver_phone: Optional[str] = Field(None, max_length=50, description="司机电话")


class BoxDetail(BaseModel):
    product_sku: str = Field(..., max_length=24, description="SKU")
    quantity: int = Field(..., gt=0, description="数量")
    fba_product_code: Optional[str] = Field(
        None, max_length=20, description="FBA商品编码"
    )
    data_code: Optional[str] = Field(None, max_length=100, description="序列号集成码")
    serial_number: Optional[str] = Field(None, max_length=100, description="序列号")


class InboundOrderItemBase(BaseModel):
    box_no: int = Field(..., ge=1, description="箱号(从1开始的连续正整数)")
    reference_box_no: Optional[str] = Field(
        None, max_length=30, description="箱唛参考号"
    )
    box_details: List[BoxDetail] = Field(..., description="箱子信息")


class InboundOrderBase(BaseModel):
    transit_type: int = Field(
        ...,
        ge=0,
        le=5,
        description="入库单类型: 0-自发入库单, 3-中转入库单, 5-FBA入库单",
    )
    receiving_shipping_type: int = Field(
        ...,
        ge=0,
        le=5,
        description="运输方式: 0-空运, 1-海运散货, 2-快递, 3-铁运整柜, 4-海运整柜, 5-铁运散货",
    )
    warehouse_code: str = Field(..., max_length=32, description="海外仓仓库编码")

    reference_no: Optional[str] = Field(None, max_length=50, description="参考号")
    sm_code: Optional[str] = Field(
        None, max_length=255, description="物流产品(中转特有)"
    )
    transit_warehouse_code: Optional[str] = Field(
        None, max_length=255, description="中转仓仓库编码(中转特有)"
    )
    customs_type: Optional[int] = Field(
        None,
        ge=0,
        le=2,
        description="报关方式(中转特有): 0-EDI报关, 1-委托报关, 2-报关自理",
    )
    collecting_service: Optional[int] = Field(
        None, ge=0, le=1, description="揽收服务(中转特有): 0-自送货物, 1-上门提货"
    )
    collecting_time: Optional[datetime] = Field(None, description="揽收时间")
    value_add_service: Optional[str] = Field(
        None,
        max_length=255,
        description="增值服务: world_ease-woordease服务, origin_crt-产地证, fumigation-熏蒸",
    )
    clearance_service: Optional[int] = Field(
        None, ge=0, le=1, description="是否自有税号清关(中转特有)"
    )
    import_company: Optional[int] = Field(None, description="进口商编码")
    export_company: Optional[int] = Field(None, description="出口商编码(中转特有)")
    car_model_code: Optional[str] = Field(
        None, max_length=255, description="车型(中转特有)"
    )

    tracking_number: Optional[str] = Field(
        None, max_length=35, description="跟踪号/海柜号"
    )
    eta_date: Optional[datetime] = Field(None, description="预计到达时间(自发/FBA必填)")
    receiving_desc: Optional[str] = Field(None, max_length=255, description="备注")
    verify: int = Field(
        default=0, ge=0, le=1, description="是否审核: 0-新建不审核(草稿), 1-新建并审核"
    )
    weight: Optional[float] = Field(None, ge=0.01, le=999999.99, description="重量(kg)")
    volume: Optional[float] = Field(
        None, ge=0.01, le=99999.99, description="体积(立方米)"
    )
    wp_code: Optional[str] = Field(None, description="物理仓仓库代码")
    is_delay: int = Field(default=0, ge=0, le=1, description="是否递延: 0-否, 1-是")
    is_rollover: int = Field(
        default=0, ge=0, le=1, description="是否仓库装箱商品: 0-否, 1-是(FBA必填)"
    )

    shiper_address: Optional[ShiperAddress] = Field(
        None, description="发件人地址(自发入库单)"
    )
    collecting_address: Optional[List[CollectingAddress]] = Field(
        None, description="揽收地址(中转特有,上门揽收时必填)"
    )
    customers_send_info: Optional[CustomersSendInfo] = Field(
        None, description="客户自送信息(中转特有,自送货物时必填)"
    )

    items: List[InboundOrderItemBase] = Field(..., description="入库单明细")


class InboundOrderCreate(InboundOrderBase):
    pass


class InboundOrderUpdate(BaseModel):
    transit_type: Optional[int] = Field(None, ge=0, le=5, description="入库单类型")
    receiving_shipping_type: Optional[int] = Field(
        None, ge=0, le=5, description="运输方式"
    )
    warehouse_code: Optional[str] = Field(
        None, max_length=32, description="海外仓仓库编码"
    )
    reference_no: Optional[str] = Field(None, max_length=50, description="参考号")
    sm_code: Optional[str] = Field(None, max_length=255, description="物流产品")
    transit_warehouse_code: Optional[str] = Field(
        None, max_length=255, description="中转仓仓库编码"
    )
    customs_type: Optional[int] = Field(None, ge=0, le=2, description="报关方式")
    collecting_service: Optional[int] = Field(None, ge=0, le=1, description="揽收服务")
    collecting_time: Optional[datetime] = Field(None, description="揽收时间")
    value_add_service: Optional[str] = Field(
        None, max_length=255, description="增值服务"
    )
    clearance_service: Optional[int] = Field(
        None, ge=0, le=1, description="是否自有税号清关"
    )
    import_company: Optional[int] = Field(None, description="进口商编码")
    export_company: Optional[int] = Field(None, description="出口商编码")
    car_model_code: Optional[str] = Field(None, max_length=255, description="车型")
    tracking_number: Optional[str] = Field(
        None, max_length=35, description="跟踪号/海柜号"
    )
    eta_date: Optional[datetime] = Field(None, description="预计到达时间")
    receiving_desc: Optional[str] = Field(None, max_length=255, description="备注")
    verify: Optional[int] = Field(None, ge=0, le=1, description="是否审核")
    weight: Optional[float] = Field(None, ge=0.01, le=999999.99, description="重量(kg)")
    volume: Optional[float] = Field(
        None, ge=0.01, le=99999.99, description="体积(立方米)"
    )
    wp_code: Optional[str] = Field(None, description="物理仓仓库代码")
    is_delay: Optional[int] = Field(None, ge=0, le=1, description="是否递延")
    is_rollover: Optional[int] = Field(None, ge=0, le=1, description="是否仓库装箱商品")

    sa_contacter: Optional[str] = Field(None, max_length=50, description="发件人联系人")
    sa_contact_phone: Optional[str] = Field(
        None, max_length=50, description="发件人联系电话"
    )
    sa_country_code: Optional[str] = Field(
        None, max_length=2, description="发件国家/地区简称"
    )
    sa_state: Optional[str] = Field(None, max_length=50, description="发件人省/州")
    sa_city: Optional[str] = Field(None, max_length=50, description="发件人城市")
    sa_region: Optional[str] = Field(None, max_length=50, description="发件人区")
    sa_address1: Optional[str] = Field(None, max_length=50, description="发件人地址1")
    sa_address2: Optional[str] = Field(None, max_length=50, description="发件人地址2")

    ca_first_name: Optional[str] = Field(
        None, max_length=50, description="揽收联系人-名"
    )
    ca_last_name: Optional[str] = Field(
        None, max_length=50, description="揽收联系人-姓"
    )
    ca_contact_phone: Optional[str] = Field(
        None, max_length=50, description="揽收联系人电话"
    )
    ca_state: Optional[str] = Field(None, max_length=50, description="揽收地址州/省份")
    ca_city: Optional[str] = Field(None, max_length=50, description="揽收地址城市")
    ca_country_code: Optional[str] = Field(
        None, max_length=50, description="揽收地址国家/地区"
    )
    ca_zipcode: Optional[str] = Field(None, max_length=50, description="揽收地址邮编")
    ca_address1: Optional[str] = Field(None, max_length=50, description="揽收地址1")
    ca_address2: Optional[str] = Field(None, max_length=50, description="揽收地址2")

    arrive_transfer_warehouse_time: Optional[datetime] = Field(
        None, description="预计到达中转仓时间"
    )
    company_name: Optional[str] = Field(None, max_length=50, description="快递公司名称")
    delivery_code: Optional[str] = Field(None, max_length=500, description="快递单号")
    plate_no: Optional[str] = Field(None, max_length=50, description="车牌号")
    driver_name: Optional[str] = Field(None, max_length=50, description="司机姓名")
    driver_phone: Optional[str] = Field(None, max_length=50, description="司机电话")


class InboundOrderItemOut(BaseModel):
    id: int = Field(..., description="明细ID")
    inbound_order_id: int = Field(..., description="入库单ID")
    box_no: int = Field(..., description="箱号")
    reference_box_no: Optional[str] = Field(None, description="箱唛参考号")
    product_sku: str = Field(..., description="SKU")
    quantity: int = Field(..., description="数量")
    fba_product_code: Optional[str] = Field(None, description="FBA商品编码")
    data_code: Optional[str] = Field(None, description="序列号集成码")
    serial_number: Optional[str] = Field(None, description="序列号")
    created_at: datetime = Field(..., description="创建时间")

    class Config:
        from_attributes = True


class InboundOrderOut(BaseModel):
    id: int = Field(..., description="入库单ID")
    receiving_code: Optional[str] = Field(None, description="入库单号")
    reference_no: Optional[str] = Field(None, description="参考号")
    transit_type: int = Field(..., description="入库单类型")
    receiving_shipping_type: int = Field(..., description="运输方式")
    warehouse_code: str = Field(..., description="海外仓仓库编码")
    sm_code: Optional[str] = Field(None, description="物流产品")
    transit_warehouse_code: Optional[str] = Field(None, description="中转仓仓库编码")
    customs_type: Optional[int] = Field(None, description="报关方式")
    collecting_service: Optional[int] = Field(None, description="揽收服务")
    collecting_time: Optional[datetime] = Field(None, description="揽收时间")
    value_add_service: Optional[str] = Field(None, description="增值服务")
    clearance_service: Optional[int] = Field(None, description="是否自有税号清关")
    import_company: Optional[int] = Field(None, description="进口商编码")
    export_company: Optional[int] = Field(None, description="出口商编码")
    car_model_code: Optional[str] = Field(None, description="车型")
    tracking_number: Optional[str] = Field(None, description="跟踪号/海柜号")
    eta_date: Optional[datetime] = Field(None, description="预计到达时间")
    receiving_desc: Optional[str] = Field(None, description="备注")
    verify: int = Field(..., description="是否审核")
    weight: Optional[float] = Field(None, description="重量(kg)")
    volume: Optional[float] = Field(None, description="体积(立方米)")
    wp_code: Optional[str] = Field(None, description="物理仓仓库代码")
    is_delay: int = Field(..., description="是否递延")
    is_rollover: int = Field(..., description="是否仓库装箱商品")

    items: List[InboundOrderItemOut] = Field(..., description="入库单明细")

    created_at: datetime = Field(..., description="创建时间")
    updated_at: datetime = Field(..., description="更新时间")
    is_deleted: int = Field(..., description="是否删除")

    class Config:
        from_attributes = True


class InboundOrderSimpleOut(BaseModel):
    id: int = Field(..., description="入库单ID")
    receiving_code: Optional[str] = Field(None, description="入库单号")
    reference_no: Optional[str] = Field(None, description="参考号")
    transit_type: int = Field(..., description="入库单类型")
    warehouse_code: str = Field(..., description="海外仓仓库编码")
    verify: int = Field(..., description="是否审核")
    created_at: datetime = Field(..., description="创建时间")

    class Config:
        from_attributes = True
