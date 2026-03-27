
from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class ProductBase(BaseModel):
    sku: str
    name: str
    description: str
    price: float
    category: str
    brand: str
    status: str


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    sku: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None
    brand: Optional[str] = None
    status: Optional[str] = None


class ProductOut(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
