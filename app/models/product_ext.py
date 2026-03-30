from datetime import datetime
from typing import Optional, List, Dict
from sqlalchemy import BigInteger, DateTime, String, JSON, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base

class ProductExt(Base):
    __tablename__ = "product_ext"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True, comment="关联 product.id")

    # 申报信息
    product_declared_name_cn: Mapped[str] = mapped_column(String(255), nullable=False, comment="中文申报品名")
    product_declared_name: Mapped[Optional[str]] = mapped_column(String(255), comment="英文申报品名")
    product_material: Mapped[str] = mapped_column(String(255), nullable=False, comment="材质")
    product_function: Mapped[Optional[str]] = mapped_column(String(100), comment="用途")

    # 图片 & 证书
    image_link: Mapped[Optional[List[str]]] = mapped_column(JSON, comment="商品图片")
    certificate_url_list: Mapped[Optional[List[str]]] = mapped_column(JSON, comment="证书链接")

    # 批次管理
    batch_management_enabled: Mapped[int] = mapped_column(SmallInteger, default=0, comment="批次管理")
    batch_info: Mapped[Optional[Dict]] = mapped_column(JSON, comment="批次信息")

    # 序列号
    sn_info: Mapped[Optional[Dict]] = mapped_column(JSON, comment="序列号采集")

    # 电池信息（超标时必填）
    battery_info: Mapped[Optional[Dict]] = mapped_column(JSON, comment="电池信息")

    # 关务信息（必填）
    export_country: Mapped[Dict] = mapped_column(JSON, nullable=False, comment="出口国信息")
    import_country: Mapped[Dict] = mapped_column(JSON, nullable=False, comment="进口国信息")

    # 备注
    remark: Mapped[Optional[str]] = mapped_column(String(500), comment="备注")

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_deleted: Mapped[int] = mapped_column(SmallInteger, default=0)