
from datetime import datetime

from sqlalchemy import BigInteger, DateTime, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class Order(Base):
    __tablename__="order"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(256), nullable=False, comment="订单编号")
    product_id: Mapped[int] = mapped_column(BigInteger, comment="商品id")
    description: Mapped[str] = mapped_column(String(256), nullable=False, comment="订单描述")
    username: Mapped[str] = mapped_column(String(256), nullable=False, comment="收件用户名")
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="scraped", comment="状态")
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow, comment="创建时间")
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow, comment="更新时间")