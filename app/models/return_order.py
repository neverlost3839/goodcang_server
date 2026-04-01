from datetime import datetime
from typing import Optional, List
from sqlalchemy import BigInteger, DateTime, Float, Integer, String, SmallInteger, Text
from sqlalchemy.orm import Mapped, mapped_column, Relationship
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import JSONB

from app.db.session import Base


class ReturnOrder(Base):
    __tablename__ = "return_order"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True, comment="自增主键ID"
    )
    asro_code: Mapped[str] = mapped_column(
        String(32), unique=True, index=True, comment="退件单号"
    )
    order_code: Mapped[str] = mapped_column(String(50), nullable=True, comment="订单号")
    reference_no: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, index=True, comment="参考号"
    )

    asro_status: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
        default="0",
        comment="退件状态: 0草稿,1已提交,4收货完成,5处理完成,6废弃,7处理中",
    )
    cass_type: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
        default="1",
        comment="退件类型: 0服务商退件,1客户退件,2未预报退件",
    )

    asro_add_time: Mapped[Optional[datetime]] = mapped_column(
        DateTime, nullable=True, comment="创建时间"
    )
    asro_audit_time: Mapped[Optional[datetime]] = mapped_column(
        DateTime, nullable=True, comment="审核时间"
    )
    asro_putaway_time: Mapped[Optional[datetime]] = mapped_column(
        DateTime, nullable=True, comment="上架完成时间"
    )

    warehouse_code: Mapped[str] = mapped_column(
        String(20), nullable=False, comment="退件收货仓库"
    )
    sm_type: Mapped[str] = mapped_column(
        String(10), nullable=False, default="0", comment="派送方式: 0代选物流,1自选物流"
    )
    collect_warehouse_code: Mapped[Optional[str]] = mapped_column(
        String(20), nullable=True, comment="集货区域仓编码"
    )

    service_type: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False,
        default=1,
        comment="退货服务类型: 1退件质检,2退件销毁",
    )
    is_transit: Mapped[int] = mapped_column(
        SmallInteger, nullable=False, default=2, comment="是否退回集货仓: 1是,2否"
    )
    tracking_no: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="跟踪号"
    )
    asro_reason: Mapped[Optional[str]] = mapped_column(
        Text, nullable=True, comment="退件原因"
    )

    sm_code: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="物流产品编码"
    )
    as_length: Mapped[float] = mapped_column(
        Float, nullable=False, default=0.0, comment="计费长"
    )
    as_width: Mapped[float] = mapped_column(
        Float, nullable=False, default=0.0, comment="计费宽"
    )
    as_height: Mapped[float] = mapped_column(
        Float, nullable=False, default=0.0, comment="计费高"
    )
    charge_weight: Mapped[float] = mapped_column(
        Float, nullable=False, default=0.0, comment="计费重"
    )

    asro_note: Mapped[Optional[str]] = mapped_column(
        Text, nullable=True, comment="客服留言"
    )
    return_identification: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False,
        default=2,
        comment="退件标识: 1谷仓发货退件,2非谷仓发货退件",
    )

    fee_details: Mapped[Optional[str]] = mapped_column(
        Text, nullable=True, comment="费用详情JSON"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )


class ReturnOrderProduct(Base):
    __tablename__ = "return_order_product"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True, comment="自增主键ID"
    )
    return_order_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("return_order.id"), nullable=False, comment="退货单ID"
    )

    product_barcode: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="商品编码"
    )
    product_sku: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="客户商品编码"
    )

    return_auth: Mapped[int] = mapped_column(
        SmallInteger, nullable=False, default=0, comment="退件授权: 0否,1是"
    )
    return_replacement_sku: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="换标编码"
    )
    photo_list: Mapped[Optional[str]] = mapped_column(
        Text, nullable=True, comment="图片信息JSON"
    )

    sellable_qty: Mapped[int] = mapped_column(
        Integer, nullable=False, default=0, comment="良品数量"
    )
    unsellable_qty: Mapped[int] = mapped_column(
        Integer, nullable=False, default=0, comment="不良品数量"
    )
    destruction_qty: Mapped[int] = mapped_column(
        Integer, nullable=False, default=0, comment="销毁数量"
    )

    sellable_detail: Mapped[Optional[str]] = mapped_column(
        Text, nullable=True, comment="良品明细JSON"
    )
    unsellable_detail: Mapped[Optional[str]] = mapped_column(
        Text, nullable=True, comment="不良品明细JSON"
    )
    destruction_detail: Mapped[Optional[str]] = mapped_column(
        Text, nullable=True, comment="销毁明细JSON"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )
