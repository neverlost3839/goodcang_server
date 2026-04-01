from datetime import datetime
from typing import Optional, List
from sqlalchemy import BigInteger, DateTime, String, Integer, SmallInteger, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.db.session import Base

class Country(Base):
    __tablename__ = "country"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment="自增主键ID")
    country_code: Mapped[str] = mapped_column(String(10), unique=True, index=True, comment="国家/地区二字码")
    country_name: Mapped[str] = mapped_column(String(100), nullable=False, comment="国家/地区中文名")
    country_name_en: Mapped[str] = mapped_column(String(100), nullable=False, comment="国家/地区英文名")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class Warehouse(Base):
    __tablename__ = "warehouse"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment="自增主键ID")
    warehouse_code: Mapped[str] = mapped_column(String(50), unique=True, index=True, comment="仓库代码")
    warehouse_name: Mapped[str] = mapped_column(String(100), nullable=False, comment="仓库名称")
    country_code: Mapped[str] = mapped_column(String(10), nullable=False, comment="仓库所在国家/地区代码")
    wp_list: Mapped[Optional[str]] = mapped_column(Text, nullable=True, comment="物理仓列表JSON")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class ShippingMethod(Base):
    __tablename__ = "shipping_method"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment="自增主键ID")
    code: Mapped[str] = mapped_column(String(50), unique=True, index=True, comment="物流产品代码")
    name: Mapped[str] = mapped_column(String(200), nullable=False, comment="物流产品中文名称")
    name_en: Mapped[Optional[str]] = mapped_column(String(200), nullable=True, comment="物流产品英文名称")
    warehouse_code: Mapped[Optional[str]] = mapped_column(String(50), nullable=True, comment="仓库代码")
    sm_type: Mapped[Optional[str]] = mapped_column(String(10), nullable=True, comment="物流产品类型")
    sp_code: Mapped[Optional[str]] = mapped_column(String(50), nullable=True, comment="服务商代码")
    is_signature: Mapped[int] = mapped_column(SmallInteger, default=0, comment="是否支持签名服务: 0否,1是")
    address_validation_enabled: Mapped[int] = mapped_column(SmallInteger, default=0, comment="是否支持地址校验: 0不支持,1支持")
    is_truck: Mapped[int] = mapped_column(SmallInteger, default=0, comment="是否卡派渠道: 0否,1是")
    is_specify_arrival_time: Mapped[int] = mapped_column(SmallInteger, default=2, comment="是否指定到货时间: 1支持,2不支持")
    delivery_time_list: Mapped[Optional[str]] = mapped_column(Text, nullable=True, comment="支持的到货时间段JSON")
    sm_business_type: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True, comment="业务类型: 1仓配一体,3仓配分离")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class Account(Base):
    __tablename__ = "account"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment="自增主键ID")
    customer_code: Mapped[str] = mapped_column(String(50), nullable=False, comment="客户代码")
    firm_name: Mapped[Optional[str]] = mapped_column(String(200), nullable=True, comment="签约主体名称")
    firm_status: Mapped[int] = mapped_column(SmallInteger, nullable=False, comment="签约主体状态")
    server_firm_name: Mapped[Optional[str]] = mapped_column(String(200), nullable=True, comment="服务主体")
    business_type_list: Mapped[Optional[str]] = mapped_column(Text, nullable=True, comment="签约业务类型JSON")
    account_code: Mapped[str] = mapped_column(String(50), nullable=False, comment="账户代码")
    balance_list: Mapped[Optional[str]] = mapped_column(Text, nullable=True, comment="币种信息JSON")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class CostType(Base):
    __tablename__ = "cost_type"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment="自增主键ID")
    cost_name: Mapped[str] = mapped_column(String(100), nullable=False, comment="费用名称")
    cost_code: Mapped[str] = mapped_column(String(50), nullable=False, unique=True, index=True, comment="费用编码")
    sign_business_type: Mapped[int] = mapped_column(SmallInteger, nullable=False, comment="业务类型: 0海外仓储,1中转代发")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class FuelRate(Base):
    __tablename__ = "fuel_rate"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment="自增主键ID")
    fls_rate: Mapped[Optional[str]] = mapped_column(String(20), nullable=True, comment="燃油费率")
    fls_begin_time: Mapped[Optional[str]] = mapped_column(String(30), nullable=True, comment="开始有效时间")
    fls_end_time: Mapped[Optional[str]] = mapped_column(String(30), nullable=True, comment="结束有效时间")
    sm_name: Mapped[Optional[str]] = mapped_column(String(200), nullable=True, comment="物流产品名称")
    sm_code: Mapped[str] = mapped_column(String(50), nullable=False, index=True, comment="物流产品代码")
    logistic_type: Mapped[int] = mapped_column(SmallInteger, nullable=False, comment="物流类型: 0发货物流,1退货物流")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)