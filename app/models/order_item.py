from datetime import datetime
from typing import Optional
from sqlalchemy import BigInteger, DateTime, Float, Index, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class OrderItem(Base):
    __tablename__ = "order_item"
    __table_args__ = (
        Index("idx_order_item_order_id", "order_id"),
        Index("idx_order_item_product_sku", "product_sku"),
        {"comment": "订单商品明细表"},
    )

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True
    )
    order_id: Mapped[int] = mapped_column(
        BigInteger, nullable=False, comment="关联order.id"
    )

    # 商品核心
    product_sku: Mapped[str] = mapped_column(
        String(24), nullable=False, comment="商品SKU"
    )
    quantity: Mapped[int] = mapped_column(
        SmallInteger, nullable=False, comment="购买数量"
    )

    # 平台交易信息
    transaction_id: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="平台交易号"
    )
    item_id: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="平台商品行号"
    )

    # FBA & 合规
    fba_product_code: Mapped[Optional[str]] = mapped_column(
        String(20), nullable=True, comment="FBA商品编码"
    )
    euro_terms_code: Mapped[Optional[str]] = mapped_column(
        String(50), nullable=True, comment="合规负责人编码"
    )
    label_replacement_qty: Mapped[Optional[int]] = mapped_column(
        SmallInteger, nullable=True, comment="内件总数量"
    )

    # 申报信息
    product_declared_value: Mapped[Optional[float]] = mapped_column(
        Float, nullable=True, comment="申报价值 USD"
    )
    hs_code: Mapped[Optional[str]] = mapped_column(
        String(10), nullable=True, comment="海关编码 6-10位"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )