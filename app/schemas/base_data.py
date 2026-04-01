from datetime import datetime
from typing import Optional, List, Any
from pydantic import BaseModel, Field


class CountryBase(BaseModel):
    country_code: str = Field(..., max_length=10, description="国家/地区二字码")
    country_name: str = Field(..., max_length=100, description="国家/地区中文名")
    country_name_en: str = Field(..., max_length=100, description="国家/地区英文名")

    class Config:
        from_attributes = True


class CountryOut(CountryBase):
    id: int = Field(..., description="国家ID")
    created_at: datetime = Field(..., description="创建时间")
    updated_at: datetime = Field(..., description="更新时间")


class PhysicalWarehouseAddress(BaseModel):
    state: Optional[str] = Field(None, description="省/州")
    city: Optional[str] = Field(None, description="城市")
    postcode: Optional[str] = Field(None, description="邮编")
    contacter: Optional[str] = Field(None, description="联系人")
    phone: Optional[str] = Field(None, description="电话")
    street_address1: Optional[str] = Field(None, description="地址1")
    street_address2: Optional[str] = Field(None, description="地址2")
    street_number: Optional[str] = Field(None, description="门牌号")


class PhysicalWarehouseItem(BaseModel):
    code: Optional[str] = Field(None, description="物理仓代码")
    name: Optional[str] = Field(None, description="物理仓名称")
    address: Optional[PhysicalWarehouseAddress] = Field(None, description="地址信息")


class WarehouseBase(BaseModel):
    warehouse_code: str = Field(..., max_length=50, description="仓库代码")
    warehouse_name: str = Field(..., max_length=100, description="仓库名称")
    country_code: str = Field(..., max_length=10, description="仓库所在国家/地区代码")
    wp_list: Optional[List[PhysicalWarehouseItem]] = Field(
        None, description="物理仓列表"
    )

    class Config:
        from_attributes = True


class WarehouseOut(WarehouseBase):
    id: int = Field(..., description="仓库ID")
    created_at: datetime = Field(..., description="创建时间")
    updated_at: datetime = Field(..., description="更新时间")


class ShippingMethodBase(BaseModel):
    code: str = Field(..., max_length=50, description="物流产品代码")
    name: str = Field(..., max_length=200, description="物流产品中文名称")
    name_en: Optional[str] = Field(None, max_length=200, description="物流产品英文名称")
    warehouse_code: Optional[str] = Field(None, max_length=50, description="仓库代码")
    sm_type: Optional[str] = Field(None, max_length=10, description="物流产品类型")
    sp_code: Optional[str] = Field(None, max_length=50, description="服务商代码")
    is_signature: int = Field(default=0, description="是否支持签名服务: 0否,1是")
    address_validation_enabled: int = Field(
        default=0, description="是否支持地址校验: 0不支持,1支持"
    )
    is_truck: int = Field(default=0, description="是否卡派渠道: 0否,1是")
    is_specify_arrival_time: int = Field(
        default=2, description="是否指定到货时间: 1支持,2不支持"
    )
    delivery_time_list: Optional[List[str]] = Field(
        None, description="支持的到货时间段"
    )
    sm_business_type: Optional[int] = Field(
        None, description="业务类型: 1仓配一体,3仓配分离"
    )

    class Config:
        from_attributes = True


class ShippingMethodOut(ShippingMethodBase):
    id: int = Field(..., description="物流ID")
    created_at: datetime = Field(..., description="创建时间")
    updated_at: datetime = Field(..., description="更新时间")


class BalanceListItem(BaseModel):
    currency_code: str = Field(..., description="币种代码")
    amount: str = Field(..., description="金额")


class AccountListItem(BaseModel):
    firm_name: Optional[str] = Field(None, description="签约主体名称")
    firm_status: int = Field(
        ...,
        description="签约主体状态: 0审核中,1审核不通过,2可用,3停用,4已作废,5草稿,6待签约",
    )
    server_firm_name: Optional[str] = Field(None, description="服务主体")
    business_type_list: List[int] = Field(
        default_factory=list, description="签约业务类型: 0海外仓储,1中转代发"
    )
    account_code: str = Field(..., description="账户代码")
    balance_list: List[BalanceListItem] = Field(
        default_factory=list, description="币种信息"
    )

    class Config:
        from_attributes = True


class AccountBase(BaseModel):
    customer_code: str = Field(..., max_length=50, description="客户代码")
    account_list: List[AccountListItem] = Field(
        default_factory=list, description="账户信息列表"
    )

    class Config:
        from_attributes = True


class AccountOut(AccountBase):
    id: int = Field(..., description="账户ID")
    created_at: datetime = Field(..., description="创建时间")
    updated_at: datetime = Field(..., description="更新时间")


class CostTypeItem(BaseModel):
    cost_name: str = Field(..., description="费用名称")
    cost_code: str = Field(..., description="费用编码")

    class Config:
        from_attributes = True


class CostTypeBase(BaseModel):
    cost_name: str = Field(..., max_length=100, description="费用名称")
    cost_code: str = Field(..., max_length=50, description="费用编码")
    sign_business_type: int = Field(..., description="业务类型: 0海外仓储,1中转代发")

    class Config:
        from_attributes = True


class CostTypeOut(CostTypeBase):
    id: int = Field(..., description="费用类型ID")
    created_at: datetime = Field(..., description="创建时间")
    updated_at: datetime = Field(..., description="更新时间")


class FuelRateItem(BaseModel):
    fls_rate: Optional[str] = Field(None, description="燃油费率")
    fls_begin_time: Optional[str] = Field(None, description="开始有效时间")
    fls_end_time: Optional[str] = Field(None, description="结束有效时间")
    sm_name: Optional[str] = Field(None, description="物流产品名称")
    sm_code: str = Field(..., description="物流产品代码")

    class Config:
        from_attributes = True


class FuelRateListResp(BaseModel):
    list: List[FuelRateItem] = Field(
        default_factory=list, description="燃油费率信息列表"
    )
    total: int = Field(..., description="列表总数")


class FuelRateBase(BaseModel):
    fls_rate: Optional[str] = Field(None, max_length=20, description="燃油费率")
    fls_begin_time: Optional[str] = Field(
        None, max_length=30, description="开始有效时间"
    )
    fls_end_time: Optional[str] = Field(None, max_length=30, description="结束有效时间")
    sm_name: Optional[str] = Field(None, max_length=200, description="物流产品名称")
    sm_code: str = Field(..., max_length=50, description="物流产品代码")
    logistic_type: int = Field(..., description="物流类型: 0发货物流,1退货物流")

    class Config:
        from_attributes = True


class FuelRateOut(FuelRateBase):
    id: int = Field(..., description="燃油费率ID")
    created_at: datetime = Field(..., description="创建时间")
    updated_at: datetime = Field(..., description="更新时间")


class CostTypeListRequest(BaseModel):
    sign_business_type: int = Field(..., description="业务类型: 0海外仓储,1中转代发")


class FuelRateListRequest(BaseModel):
    logistic_type: int = Field(..., description="物流类型: 0发货物流,1退货物流")
    sm_code: str = Field(..., max_length=50, description="物流产品编码")
    begin_time: str = Field(..., description="起始生效时间")
    end_time: str = Field(..., description="结束生效时间")
    page: int = Field(default=1, ge=1, description="分页页码")
    page_size: int = Field(default=10, ge=1, le=200, description="分页数量")


class ShippingMethodListRequest(BaseModel):
    warehouse_code: Optional[str] = Field(
        None, max_length=32, description="尾程仓库代码"
    )
