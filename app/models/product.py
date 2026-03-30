from datetime import datetime
from typing import Optional
from sqlalchemy import BigInteger, DateTime, Float, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base

class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment="自增主键ID")
    product_sku: Mapped[str] = mapped_column(String(24), nullable=False, unique=True, index=True, comment="SKU")
    reference_no: Mapped[Optional[str]] = mapped_column(String(255), nullable=True, comment="客户参考代码")
    thirdparty_sku_mapping: Mapped[Optional[str]] = mapped_column(String(50), nullable=True, comment="第三方映射编码")
    
    product_name_cn: Mapped[str] = mapped_column(String(255), nullable=False, comment="中文商品名称")
    product_name_en: Mapped[str] = mapped_column(String(255), nullable=False, comment="英文商品名称")

    product_weight: Mapped[float] = mapped_column(Float, nullable=False, comment="重量 KG")
    product_length: Mapped[float] = mapped_column(Float, nullable=False, comment="长 CM")
    product_width: Mapped[float] = mapped_column(Float, nullable=False, comment="宽 CM")
    product_height: Mapped[float] = mapped_column(Float, nullable=False, comment="高 CM")

    sku_wrapper_type: Mapped[int] = mapped_column(SmallInteger, default=1, nullable=False, comment="包装属性")
    cat_lang: Mapped[Optional[str]] = mapped_column(String(2), default="zh", comment="品类语言")
    cat_id_level2: Mapped[int] = mapped_column(BigInteger, nullable=False, comment="二级品类ID")

    contain_battery: Mapped[int] = mapped_column(SmallInteger, default=0, nullable=False, comment="货物属性")
    type_of_goods: Mapped[int] = mapped_column(SmallInteger, default=0, nullable=False, comment="包裹类型")

    branded: Mapped[int] = mapped_column(SmallInteger, default=0, nullable=False, comment="是否品牌")
    product_brand: Mapped[Optional[str]] = mapped_column(String(100), nullable=True, comment="商品品牌")
    product_model: Mapped[Optional[str]] = mapped_column(String(100), default="无", comment="商品型号")

    product_link: Mapped[str] = mapped_column(String(1000), nullable=False, comment="商品售卖链接")
    unit: Mapped[Optional[str]] = mapped_column(String(11), default="PCS", comment="成交单位")

    return_auth: Mapped[int] = mapped_column(SmallInteger, default=1, nullable=False, comment="退件授权")
    return_replacement_sku: Mapped[Optional[str]] = mapped_column(String(50), nullable=True, comment="换标编码")

    verify: Mapped[int] = mapped_column(SmallInteger, default=0, nullable=False, comment="审核状态")
    product_barcode: Mapped[Optional[str]] = mapped_column(String(50), index=True, comment="商品条码")

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    is_deleted: Mapped[int] = mapped_column(SmallInteger, default=0, nullable=False)