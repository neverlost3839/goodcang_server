
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class OrderBase(BaseModel):
    """订单基础字段"""
    code: str = Field(..., max_length=256, description="订单编号")
    description: str = Field(..., max_length=256, description="订单描述")
    product_id: int = Field(..., description="商品ID")
    username: str = Field(..., max_length=256, description="收件用户名")
    status: str = Field(default="scraped", max_length=20, description="订单状态")


class OrderCreate(OrderBase):
    """创建订单请求参数"""
    pass


class OrderUpdate(BaseModel):
    """更新订单请求参数（所有字段可选）"""
    code: Optional[str] = Field(None, max_length=256, description="订单编号")
    description: Optional[str] = Field(None, max_length=256, description="订单描述")
    product_id: Optional[int] = Field(None, description="商品ID")
    username: Optional[str] = Field(None, max_length=256, description="收件用户名")
    status: Optional[str] = Field(None, max_length=20, description="订单状态")


class OrderOut(BaseModel):
    """订单响应参数"""
    id: int = Field(..., description="订单ID")
    code: str = Field(..., description="订单编号")
    description: str = Field(..., description="订单描述")
    product_id: int = Field(..., description="商品ID")
    username: str = Field(..., description="收件用户名")
    status: str = Field(..., description="订单状态")
    created_at: datetime = Field(..., description="创建时间")
    updated_at: datetime = Field(..., description="更新时间")

    class Config:
        from_attributes = True


class OrderQuery(BaseModel):
    """订单查询参数"""
    code: Optional[str] = Field(None, description="订单编号")
    product_id: Optional[int] = Field(None, description="商品ID")
    username: Optional[str] = Field(None, max_length=256, description="收件用户名")
    status: Optional[str] = Field(None, max_length=20, description="订单状态")
    created_at_from: Optional[datetime] = Field(None, description="创建时间起始")
    created_at_to: Optional[datetime] = Field(None, description="创建时间截止")
    updated_at_from: Optional[datetime] = Field(None, description="更新时间起始")
    updated_at_to: Optional[datetime] = Field(None, description="更新时间截止")