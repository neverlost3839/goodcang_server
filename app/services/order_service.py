from datetime import datetime
from typing import Optional

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.crud_order import crud_order
from app.models.order import Order
from app.schemas.common import PaginatedData
from app.schemas.order import OrderCreate, OrderOut, OrderUpdate


class OrderService:
    async def list(
        self,
        db: AsyncSession,
        *,
        page: int = 1,
        page_size: int = 20,
        reference_no: Optional[str] = None,
        platform: Optional[str] = None,
        warehouse_code: Optional[str] = None,
        country_code: Optional[str] = None,
        name: Optional[str] = None,
        phone: Optional[str] = None,
        email: Optional[str] = None,
        verify: Optional[int] = None,
        order_code: Optional[str] = None,
        updated_at_from: Optional[datetime] = None,
        updated_at_to: Optional[datetime] = None,
    ) -> PaginatedData[OrderOut]:
        filters = []

        if reference_no:
            filters.append(Order.reference_no.ilike(f"%{reference_no}%"))
        if platform:
            filters.append(Order.platform == platform)
        if warehouse_code:
            filters.append(Order.warehouse_code == warehouse_code)
        if country_code:
            filters.append(Order.country_code == country_code)
        if name:
            filters.append(Order.name.ilike(f"%{name}%"))
        if phone:
            filters.append(Order.phone == phone)
        if email:
            filters.append(Order.email.ilike(f"%{email}%"))
        if verify is not None:
            filters.append(Order.verify == verify)
        if order_code:
            filters.append(Order.order_code == order_code)
        if updated_at_from:
            filters.append(Order.updated_at >= updated_at_from)
        if updated_at_to:
            filters.append(Order.updated_at <= updated_at_to)

        skip = (page - 1) * page_size

        items = await crud_order.get_multi(
            db, skip=skip, limit=page_size, filters=filters if filters else None
        )

        total = await crud_order.count(db, filters=filters if filters else None)

        total_pages = (total + page_size - 1) // page_size

        return PaginatedData(
            items=[OrderOut.model_validate(item) for item in items],
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages,
        )

    async def get(self, db: AsyncSession, *, id: int) -> OrderOut:
        db_obj = await crud_order.get(db, id=id)
        if not db_obj:
            raise HTTPException(status_code=404, detail=f"订单ID {id} 不存在")
        return OrderOut.model_validate(db_obj)

    async def create(self, db: AsyncSession, *, obj_in: OrderCreate) -> OrderOut:
        db_obj = await crud_order.create(db=db, obj_in=obj_in)
        return OrderOut.model_validate(db_obj)

    async def update(
        self, db: AsyncSession, *, id: int, obj_in: OrderUpdate
    ) -> OrderOut:
        db_obj = await crud_order.get(db, id=id)
        if not db_obj:
            raise HTTPException(status_code=404, detail=f"订单ID {id} 不存在")
        updated_obj = await crud_order.update(db=db, db_obj=db_obj, obj_in=obj_in)
        return OrderOut.model_validate(updated_obj)

    async def delete(self, db: AsyncSession, *, id: int) -> bool:
        db_obj = await crud_order.get(db, id=id)
        if not db_obj:
            raise HTTPException(status_code=404, detail=f"订单ID {id} 不存在")
        await crud_order.delete(db, id=id)
        return True


order_service = OrderService()
