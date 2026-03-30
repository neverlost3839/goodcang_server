from datetime import datetime
from typing import Optional, List, Dict
from sqlalchemy import (
    BigInteger, DateTime, Float, SmallInteger, String, JSON, Index
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class Order(Base):
    __tablename__ = "order"
    __table_args__ = (
        Index("idx_order_reference_no", "reference_no"),
        Index("idx_order_platform", "platform"),
        Index("idx_order_warehouse_code", "warehouse_code"),
        {"comment": "谷仓订单主表"},
    )

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True, comment="自增ID"
    )

    # 订单基础
    reference_no: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="订单参考号/平台单号"
    )
    platform: Mapped[Optional[str]] = mapped_column(
        String(20), default="OTHER", comment="平台代码"
    )

    # 物流与仓库
    shipping_method: Mapped[Optional[str]] = mapped_column(
        String(32), nullable=True, comment="物流产品代码"
    )
    warehouse_code: Mapped[Optional[str]] = mapped_column(
        String(32), nullable=True, comment="发货仓库代码"
    )

    # 收件人地址
    country_code: Mapped[str] = mapped_column(
        String(2), nullable=False, comment="国家二字码"
    )
    province: Mapped[str] = mapped_column(
        String(20), nullable=False, comment="省/州"
    )
    city: Mapped[str] = mapped_column(
        String(32), nullable=False, comment="城市"
    )
    company: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="公司名称"
    )
    address1: Mapped[str] = mapped_column(
        String(50), nullable=False, comment="地址1"
    )
    address2: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="地址2"
    )
    zipcode: Mapped[str] = mapped_column(
        String(20), nullable=False, comment="邮编"
    )
    doorplate: Mapped[Optional[str]] = mapped_column(
        String(20), nullable=True, comment="门牌号"
    )

    # 收件人信息
    name: Mapped[str] = mapped_column(
        String(48), nullable=False, comment="收件人名"
    )
    last_name: Mapped[Optional[str]] = mapped_column(
        String(48), nullable=True, comment="收件人姓"
    )
    cell_phone: Mapped[Optional[str]] = mapped_column(
        String(8), nullable=True, comment="分机号"
    )
    phone: Mapped[Optional[str]] = mapped_column(
        String(20), nullable=True, comment="联系电话"
    )
    email: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True, comment="邮箱"
    )

    # 订单备注与包装
    order_desc: Mapped[Optional[str]] = mapped_column(
        String(500), nullable=True, comment="订单备注"
    )
    customer_package_requirement: Mapped[Optional[int]] = mapped_column(
        SmallInteger, nullable=True, comment="包材要求 1纸箱 2快递袋 3气泡袋 4环保袋"
    )

    # 审核与修改控制
    verify: Mapped[int] = mapped_column(
        SmallInteger, default=0, comment="0草稿 1审核"
    )
    is_shipping_method_not_allow_update: Mapped[int] = mapped_column(
        SmallInteger, default=1, comment="0可修改物流 1不可修改"
    )

    # 增值服务
    is_signature: Mapped[int] = mapped_column(
        SmallInteger, default=0, comment="0无需签名 1需签名"
    )
    is_insurance: Mapped[int] = mapped_column(
        SmallInteger, default=0, comment="0无保险 1有保险"
    )
    insurance_value: Mapped[float] = mapped_column(
        Float, default=0, comment="保额"
    )

    # FBA 相关
    fba_shipment_id: Mapped[Optional[str]] = mapped_column(
        String(12), nullable=True, comment="FBA Shipment ID"
    )
    fba_shipment_id_create_time: Mapped[Optional[datetime]] = mapped_column(
        DateTime, nullable=True, comment="FBA Shipment 创建时间"
    )
    property_label: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="平台模式 SFP等"
    )
    business_type: Mapped[int] = mapped_column(
        SmallInteger, default=0, comment="0仓配一体 1仓配分离"
    )
    is_change_label: Mapped[int] = mapped_column(
        SmallInteger, default=1, comment="0不换标 1换标"
    )
    age_detection: Mapped[int] = mapped_column(
        SmallInteger, default=0, comment="0不检测 16/18年龄检测"
    )

    # 其他服务
    lift_gate: Mapped[int] = mapped_column(
        SmallInteger, default=0, name="liftgate", comment="0否 1是 LiftGate"
    )
    payment_time: Mapped[Optional[datetime]] = mapped_column(
        DateTime, nullable=True, comment="付款时间"
    )
    attachment_ids: Mapped[Optional[List[int]]] = mapped_column(
        JSON, nullable=True, comment="附件ID数组"
    )
    estimated_arrival_date: Mapped[Optional[datetime]] = mapped_column(
        DateTime, nullable=True, comment="预计到货日期"
    )
    estimated_arrival_time: Mapped[Optional[str]] = mapped_column(
        String(20), nullable=True, comment="到货时间段"
    )

    # 复杂对象结构
    sender_info: Mapped[Optional[Dict]] = mapped_column(
        JSON, nullable=True, comment="发件人信息 SenderInfo"
    )
    vat_change_info: Mapped[Optional[Dict]] = mapped_column(
        JSON, nullable=True, comment="欧盟税改信息 VatChangeInfo"
    )
    is_euro_label: Mapped[Optional[int]] = mapped_column(
        SmallInteger, nullable=True, comment="1贴标 0不贴标"
    )
    vas: Mapped[Optional[Dict]] = mapped_column(
        JSON, nullable=True, comment="增值服务 ValueAddedService"
    )

    # FBA 仓库装箱
    is_warehouse_packing: Mapped[int] = mapped_column(
        SmallInteger, default=0, comment="0否 1仓库装箱"
    )
    carton_info: Mapped[Optional[Dict]] = mapped_column(
        JSON, nullable=True, comment="FBA转仓单信息 CartonProductItem"
    )
    truck_info: Mapped[Optional[Dict]] = mapped_column(
        JSON, nullable=True, comment="卡派渠道信息 TruckInfo"
    )

    # 接口返回的平台订单号
    order_code: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="谷仓返回订单号"
    )

    # 系统字段
    is_deleted: Mapped[int] = mapped_column(
        SmallInteger, default=0, comment="0未删除 1已删除"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, comment="创建时间"
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, comment="更新时间"
    )