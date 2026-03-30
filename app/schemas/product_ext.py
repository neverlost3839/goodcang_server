from datetime import datetime
from typing import Optional, List, Dict, Any

from pydantic import BaseModel, Field


class ProductExtBase(BaseModel):
    product_id: int = Field(..., description="关联 product.id")

    product_declared_name_cn: str = Field(
        ..., max_length=255, description="中文申报品名"
    )
    product_declared_name: Optional[str] = Field(
        None, max_length=255, description="英文申报品名"
    )
    product_material: str = Field(..., max_length=255, description="材质")
    product_function: Optional[str] = Field(None, max_length=100, description="用途")

    image_link: Optional[List[str]] = Field(None, description="商品图片")
    certificate_url_list: Optional[List[str]] = Field(None, description="证书链接")

    batch_management_enabled: int = Field(default=0, ge=0, le=1, description="批次管理")
    batch_info: Optional[Dict[str, Any]] = Field(None, description="批次信息")

    sn_info: Optional[Dict[str, Any]] = Field(None, description="序列号采集")

    battery_info: Optional[Dict[str, Any]] = Field(None, description="电池信息")

    export_country: Dict[str, Any] = Field(..., description="出口国信息")
    import_country: Dict[str, Any] = Field(..., description="进口国信息")

    remark: Optional[str] = Field(None, max_length=500, description="备注")


class ProductExtCreate(ProductExtBase):
    pass


class ProductExtUpdate(BaseModel):
    product_id: Optional[int] = Field(None, description="关联 product.id")

    product_declared_name_cn: Optional[str] = Field(
        None, max_length=255, description="中文申报品名"
    )
    product_declared_name: Optional[str] = Field(
        None, max_length=255, description="英文申报品名"
    )
    product_material: Optional[str] = Field(None, max_length=255, description="材质")
    product_function: Optional[str] = Field(None, max_length=100, description="用途")

    image_link: Optional[List[str]] = Field(None, description="商品图片")
    certificate_url_list: Optional[List[str]] = Field(None, description="证书链接")

    batch_management_enabled: Optional[int] = Field(
        None, ge=0, le=1, description="批次管理"
    )
    batch_info: Optional[Dict[str, Any]] = Field(None, description="批次信息")

    sn_info: Optional[Dict[str, Any]] = Field(None, description="序列号采集")

    battery_info: Optional[Dict[str, Any]] = Field(None, description="电池信息")

    export_country: Optional[Dict[str, Any]] = Field(None, description="出口国信息")
    import_country: Optional[Dict[str, Any]] = Field(None, description="进口国信息")

    remark: Optional[str] = Field(None, max_length=500, description="备注")


class ProductExtOut(ProductExtBase):
    id: int = Field(..., description="商品扩展信息ID")
    is_deleted: int = Field(..., description="是否删除")
    created_at: datetime = Field(..., description="创建时间")
    updated_at: datetime = Field(..., description="更新时间")

    class Config:
        from_attributes = True
