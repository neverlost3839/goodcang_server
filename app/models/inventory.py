from datetime import datetime
from typing import Optional
from sqlalchemy import BigInteger, DateTime, Integer, String, Float, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base

class Inventory(Base):
    __tablename__ = "inventory"
    __table_args__ = {"comment": "商品库存表"}

    # 主键
    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True, comment="自增主键ID"
    )

    # 商品关联
    product_sku: Mapped[str] = mapped_column(
        String(24), nullable=False, index=True, comment="商品SKU"
    )
    product_barcode: Mapped[Optional[str]] = mapped_column(
        String(100), index=True, comment="商品编码(客户代码-商品编码)"
    )

    # 仓库信息
    warehouse_code: Mapped[str] = mapped_column(
        String(32), nullable=False, index=True, comment="仓库代码"
    )
    warehouse_desc: Mapped[Optional[str]] = mapped_column(
        String(100), comment="仓库描述/名称"
    )

    # 库存核心数量（全部严格对齐API）
    onway: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False, comment="在途数量"
    )
    pending: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False, comment="待上架数量"
    )
    sellable: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False, comment="可售库存"
    )
    unsellable: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False, comment="不可售/不合格数量"
    )
    reserved: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False, comment="预占/待出库数量"
    )
    shipped: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False, comment="历史出库数量"
    )

    # 业务库存
    stocking: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False, comment="备货数量"
    )
    pi_no_stock: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False, comment="缺货数量"
    )
    pi_freeze: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False, comment="冻结数量"
    )

    # 商品货值
    product_sales_value: Mapped[float] = mapped_column(
        Float, default=0.00, nullable=False, comment="商品销售价值"
    )

    # 系统字段
    is_deleted: Mapped[int] = mapped_column(
        SmallInteger, default=0, nullable=False, comment="0未删除 1已删除"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False, comment="创建时间"
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False, comment="更新时间"
    )