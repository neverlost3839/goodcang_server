from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class InventoryBase(BaseModel):
    product_sku: str = Field(..., max_length=24, description="商品SKU")
    product_barcode: Optional[str] = Field(
        None, max_length=100, description="商品编码(客户代码-商品编码)"
    )

    warehouse_code: str = Field(..., max_length=32, description="仓库代码")
    warehouse_desc: Optional[str] = Field(
        None, max_length=100, description="仓库描述/名称"
    )

    onway: int = Field(default=0, ge=0, description="在途数量")
    pending: int = Field(default=0, ge=0, description="待上架数量")
    sellable: int = Field(default=0, ge=0, description="可售库存")
    unsellable: int = Field(default=0, ge=0, description="不可售/不合格数量")
    reserved: int = Field(default=0, ge=0, description="预占/待出库数量")
    shipped: int = Field(default=0, ge=0, description="历史出库数量")

    stocking: int = Field(default=0, ge=0, description="备货数量")
    pi_no_stock: int = Field(default=0, ge=0, description="缺货数量")
    pi_freeze: int = Field(default=0, ge=0, description="冻结数量")

    product_sales_value: float = Field(default=0.00, ge=0, description="商品销售价值")


class InventoryCreate(InventoryBase):
    pass


class InventoryUpdate(BaseModel):
    product_sku: Optional[str] = Field(None, max_length=24, description="商品SKU")
    product_barcode: Optional[str] = Field(
        None, max_length=100, description="商品编码(客户代码-商品编码)"
    )

    warehouse_code: Optional[str] = Field(None, max_length=32, description="仓库代码")
    warehouse_desc: Optional[str] = Field(
        None, max_length=100, description="仓库描述/名称"
    )

    onway: Optional[int] = Field(None, ge=0, description="在途数量")
    pending: Optional[int] = Field(None, ge=0, description="待上架数量")
    sellable: Optional[int] = Field(None, ge=0, description="可售库存")
    unsellable: Optional[int] = Field(None, ge=0, description="不可售/不合格数量")
    reserved: Optional[int] = Field(None, ge=0, description="预占/待出库数量")
    shipped: Optional[int] = Field(None, ge=0, description="历史出库数量")

    stocking: Optional[int] = Field(None, ge=0, description="备货数量")
    pi_no_stock: Optional[int] = Field(None, ge=0, description="缺货数量")
    pi_freeze: Optional[int] = Field(None, ge=0, description="冻结数量")

    product_sales_value: Optional[float] = Field(None, ge=0, description="商品销售价值")


class InventoryOut(InventoryBase):
    id: int = Field(..., description="库存ID")
    is_deleted: int = Field(..., description="0未删除 1已删除")
    created_at: datetime = Field(..., description="创建时间")
    updated_at: datetime = Field(..., description="更新时间")

    class Config:
        from_attributes = True
