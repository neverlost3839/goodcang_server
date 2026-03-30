from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    product_sku: str = Field(..., max_length=24, description="SKU")
    reference_no: Optional[str] = Field(
        None, max_length=255, description="客户参考代码"
    )
    thirdparty_sku_mapping: Optional[str] = Field(
        None, max_length=50, description="第三方映射编码"
    )

    product_name_cn: str = Field(..., max_length=255, description="中文商品名称")
    product_name_en: str = Field(..., max_length=255, description="英文商品名称")

    product_weight: float = Field(..., gt=0, description="重量 KG")
    product_length: float = Field(..., gt=0, description="长 CM")
    product_width: float = Field(..., gt=0, description="宽 CM")
    product_height: float = Field(..., gt=0, description="高 CM")

    sku_wrapper_type: int = Field(default=1, ge=0, le=10, description="包装属性")
    cat_lang: Optional[str] = Field(default="zh", max_length=2, description="品类语言")
    cat_id_level2: int = Field(..., gt=0, description="二级品类ID")

    contain_battery: int = Field(default=0, ge=0, le=1, description="货物属性")
    type_of_goods: int = Field(default=0, ge=0, le=10, description="包裹类型")

    branded: int = Field(default=0, ge=0, le=1, description="是否品牌")
    product_brand: Optional[str] = Field(None, max_length=100, description="商品品牌")
    product_model: Optional[str] = Field(
        default="无", max_length=100, description="商品型号"
    )

    product_link: str = Field(..., max_length=1000, description="商品售卖链接")
    unit: Optional[str] = Field(default="PCS", max_length=11, description="成交单位")

    return_auth: int = Field(default=1, ge=0, le=1, description="退件授权")
    return_replacement_sku: Optional[str] = Field(
        None, max_length=50, description="换标编码"
    )

    verify: int = Field(default=0, ge=0, le=1, description="审核状态")
    product_barcode: Optional[str] = Field(None, max_length=50, description="商品条码")


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    product_sku: Optional[str] = Field(None, max_length=24, description="SKU")
    reference_no: Optional[str] = Field(
        None, max_length=255, description="客户参考代码"
    )
    thirdparty_sku_mapping: Optional[str] = Field(
        None, max_length=50, description="第三方映射编码"
    )

    product_name_cn: Optional[str] = Field(
        None, max_length=255, description="中文商品名称"
    )
    product_name_en: Optional[str] = Field(
        None, max_length=255, description="英文商品名称"
    )

    product_weight: Optional[float] = Field(None, gt=0, description="重量 KG")
    product_length: Optional[float] = Field(None, gt=0, description="长 CM")
    product_width: Optional[float] = Field(None, gt=0, description="宽 CM")
    product_height: Optional[float] = Field(None, gt=0, description="高 CM")

    sku_wrapper_type: Optional[int] = Field(None, ge=0, le=10, description="包装属性")
    cat_lang: Optional[str] = Field(None, max_length=2, description="品类语言")
    cat_id_level2: Optional[int] = Field(None, gt=0, description="二级品类ID")

    contain_battery: Optional[int] = Field(None, ge=0, le=1, description="货物属性")
    type_of_goods: Optional[int] = Field(None, ge=0, le=10, description="包裹类型")

    branded: Optional[int] = Field(None, ge=0, le=1, description="是否品牌")
    product_brand: Optional[str] = Field(None, max_length=100, description="商品品牌")
    product_model: Optional[str] = Field(None, max_length=100, description="商品型号")

    product_link: Optional[str] = Field(
        None, max_length=1000, description="商品售卖链接"
    )
    unit: Optional[str] = Field(None, max_length=11, description="成交单位")

    return_auth: Optional[int] = Field(None, ge=0, le=1, description="退件授权")
    return_replacement_sku: Optional[str] = Field(
        None, max_length=50, description="换标编码"
    )

    verify: Optional[int] = Field(None, ge=0, le=1, description="审核状态")
    product_barcode: Optional[str] = Field(None, max_length=50, description="商品条码")


class ProductOut(ProductBase):
    id: int = Field(..., description="商品ID")
    is_deleted: int = Field(..., description="是否删除")
    created_at: datetime = Field(..., description="创建时间")
    updated_at: datetime = Field(..., description="更新时间")

    class Config:
        from_attributes = True


class ProductSimpleOut(BaseModel):
    id: int = Field(..., description="商品ID")
    product_sku: str = Field(..., description="SKU")
    product_name_cn: str = Field(..., description="中文商品名称")
    product_name_en: str = Field(..., description="英文商品名称")
    product_brand: Optional[str] = Field(None, description="商品品牌")

    class Config:
        from_attributes = True
