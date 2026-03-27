from datetime import datetime

from sqlalchemy import BigInteger, DateTime, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    sku: Mapped[str] = mapped_column(String(256), nullable=False, comment="产品sku")
    name: Mapped[str] = mapped_column(String(256), nullable=False, comment="产品名称")
    description: Mapped[str] = mapped_column(String(256), nullable=False, comment="产品描述")
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=True, comment="价格")
    category: Mapped[str] = mapped_column(String(256), nullable=False, comment="产品类型")
    brand: Mapped[str] = mapped_column(String(256), nullable=False, comment="产品品牌")
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="scraped", comment="状态")
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow, comment="创建时间")
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow, comment="更新时间")