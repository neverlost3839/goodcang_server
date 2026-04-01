from datetime import datetime
from typing import Optional
from sqlalchemy import BigInteger, DateTime, Float, Integer, String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.session import Base


class InboundOrder(Base):
    __tablename__ = "inbound_order"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True, comment="自增主键ID"
    )
    receiving_code: Mapped[Optional[str]] = mapped_column(
        String(50), unique=True, nullable=True, comment="入库单号"
    )
    reference_no: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, index=True, comment="参考号"
    )

    transit_type: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        comment="入库单类型: 0-自发入库单, 3-中转入库单, 5-FBA入库单",
    )
    receiving_shipping_type: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        comment="运输方式: 0-空运, 1-海运散货, 2-快递, 3-铁运整柜, 4-海运整柜, 5-铁运散货",
    )
    warehouse_code: Mapped[str] = mapped_column(
        String(32), nullable=False, index=True, comment="海外仓仓库编码"
    )

    sm_code: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True, comment="物流产品(中转特有)"
    )
    transit_warehouse_code: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True, comment="中转仓仓库编码(中转特有)"
    )
    customs_type: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=True,
        comment="报关方式(中转特有): 0-EDI报关, 1-委托报关, 2-报关自理",
    )
    collecting_service: Mapped[Optional[int]] = mapped_column(
        Integer, nullable=True, comment="揽收服务(中转特有): 0-自送货物, 1-上门提货"
    )
    collecting_time: Mapped[Optional[datetime]] = mapped_column(
        DateTime, nullable=True, comment="揽收时间"
    )
    value_add_service: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True, comment="增值服务"
    )
    clearance_service: Mapped[Optional[int]] = mapped_column(
        Integer, nullable=True, comment="是否自有税号清关(中转特有)"
    )
    import_company: Mapped[Optional[int]] = mapped_column(
        Integer, nullable=True, comment="进口商编码"
    )
    export_company: Mapped[Optional[int]] = mapped_column(
        Integer, nullable=True, comment="出口商编码(中转特有)"
    )
    car_model_code: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True, comment="车型(中转特有)"
    )

    tracking_number: Mapped[Optional[str]] = mapped_column(
        String(35), nullable=True, comment="跟踪号/海柜号"
    )
    eta_date: Mapped[Optional[datetime]] = mapped_column(
        DateTime, nullable=True, comment="预计到达时间"
    )
    receiving_desc: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True, comment="备注"
    )
    verify: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
        comment="是否审核: 0-新建不审核(草稿), 1-新建并审核",
    )
    weight: Mapped[Optional[float]] = mapped_column(
        Float, nullable=True, comment="重量(kg)"
    )
    volume: Mapped[Optional[float]] = mapped_column(
        Float, nullable=True, comment="体积(立方米)"
    )
    wp_code: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="物理仓仓库代码"
    )
    is_delay: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False, comment="是否递延: 0-否, 1-是"
    )
    is_rollover: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False, comment="是否仓库装箱商品: 0-否, 1-是"
    )

    sa_contacter: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="发件人联系人"
    )
    sa_contact_phone: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="发件人联系电话"
    )
    sa_country_code: Mapped[Optional[str]] = mapped_column(
        String(2), nullable=True, comment="发件国家/地区简称"
    )
    sa_state: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="发件人省/州"
    )
    sa_city: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="发件人城市"
    )
    sa_region: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="发件人区"
    )
    sa_address1: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="发件人地址1"
    )
    sa_address2: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="发件人地址2"
    )

    ca_first_name: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="揽收联系人-名"
    )
    ca_last_name: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="揽收联系人-姓"
    )
    ca_contact_phone: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="揽收联系人电话"
    )
    ca_state: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="揽收地址州/省份"
    )
    ca_city: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="揽收地址城市"
    )
    ca_country_code: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="揽收地址国家/地区"
    )
    ca_zipcode: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="揽收地址邮编"
    )
    ca_address1: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="揽收地址1"
    )
    ca_address2: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="揽收地址2"
    )

    arrive_transfer_warehouse_time: Mapped[Optional[datetime]] = mapped_column(
        DateTime, nullable=True, comment="预计到达中转仓时间"
    )
    company_name: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="快递公司名称"
    )
    delivery_code: Mapped[Optional[str]] = mapped_column(
        String(500), nullable=True, comment="快递单号"
    )
    plate_no: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="车牌号"
    )
    driver_name: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="司机姓名"
    )
    driver_phone: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="司机电话"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )
    is_deleted: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    items: Mapped[list["InboundOrderItem"]] = relationship(
        "InboundOrderItem", back_populates="inbound_order", cascade="all, delete-orphan"
    )


class InboundOrderItem(Base):
    __tablename__ = "inbound_order_item"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True, comment="自增主键ID"
    )
    inbound_order_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("inbound_order.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
        comment="入库单ID",
    )

    box_no: Mapped[int] = mapped_column(Integer, nullable=False, comment="箱号")
    reference_box_no: Mapped[Optional[str]] = mapped_column(
        String(30), nullable=True, comment="箱唛参考号"
    )

    product_sku: Mapped[str] = mapped_column(String(24), nullable=False, comment="SKU")
    quantity: Mapped[int] = mapped_column(Integer, nullable=False, comment="数量")
    fba_product_code: Mapped[Optional[str]] = mapped_column(
        String(20), nullable=True, comment="FBA商品编码"
    )
    data_code: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True, comment="序列号集成码"
    )
    serial_number: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True, comment="序列号"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    is_deleted: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    inbound_order: Mapped["InboundOrder"] = relationship(
        "InboundOrder", back_populates="items"
    )
