from typing import Any, List, Optional

from sqlalchemy import and_, delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.inventory import Inventory
from app.schemas.inventory import InventoryCreate, InventoryUpdate


class CRUDInventory(CRUDBase[Inventory, InventoryCreate, InventoryUpdate]):
    async def get_by_sku_warehouse(
        self, db: AsyncSession, product_sku: str, warehouse_code: str
    ) -> Optional[Inventory]:
        result = await db.execute(
            select(Inventory).where(
                and_(
                    Inventory.product_sku == product_sku,
                    Inventory.warehouse_code == warehouse_code,
                    Inventory.is_deleted == 0,
                )
            )
        )
        return result.scalar_one_or_none()

    async def get_multi(
        self,
        db: AsyncSession,
        *,
        skip: int = 0,
        limit: int = 20,
        filters: Optional[List[Any]] = None,
        product_sku: Optional[str] = None,
        product_sku_arr: Optional[List[str]] = None,
        warehouse_code: Optional[str] = None,
        warehouse_code_arr: Optional[List[str]] = None,
    ) -> List[Inventory]:
        query = select(Inventory).where(Inventory.is_deleted == 0)

        if product_sku:
            query = query.where(Inventory.product_sku == product_sku)
        if product_sku_arr:
            query = query.where(Inventory.product_sku.in_(product_sku_arr))
        if warehouse_code:
            query = query.where(Inventory.warehouse_code == warehouse_code)
        if warehouse_code_arr:
            query = query.where(Inventory.warehouse_code.in_(warehouse_code_arr))

        if filters:
            for f in filters:
                query = query.where(f)

        query = query.offset(skip).limit(limit)
        result = await db.execute(query)
        return list(result.scalars().all())

    async def count(
        self,
        db: AsyncSession,
        *,
        product_sku: Optional[str] = None,
        product_sku_arr: Optional[List[str]] = None,
        warehouse_code: Optional[str] = None,
        warehouse_code_arr: Optional[List[str]] = None,
        filters: Optional[List[Any]] = None,
    ) -> int:
        from sqlalchemy import func

        query = (
            select(func.count()).select_from(Inventory).where(Inventory.is_deleted == 0)
        )

        if product_sku:
            query = query.where(Inventory.product_sku == product_sku)
        if product_sku_arr:
            query = query.where(Inventory.product_sku.in_(product_sku_arr))
        if warehouse_code:
            query = query.where(Inventory.warehouse_code == warehouse_code)
        if warehouse_code_arr:
            query = query.where(Inventory.warehouse_code.in_(warehouse_code_arr))

        if filters:
            for f in filters:
                query = query.where(f)

        result = await db.execute(query)
        return result.scalar() or 0

    async def upsert(self, db: AsyncSession, *, obj_in: InventoryCreate) -> Inventory:
        existing = await self.get_by_sku_warehouse(
            db, obj_in.product_sku, obj_in.warehouse_code
        )
        if existing:
            update_data = obj_in.model_dump(exclude_unset=True)
            for field, value in update_data.items():
                setattr(existing, field, value)
            await db.flush()
            await db.refresh(existing)
            return existing
        else:
            db_obj = Inventory(**obj_in.model_dump(exclude_unset=True))
            db.add(db_obj)
            await db.flush()
            await db.refresh(db_obj)
            return db_obj

    async def soft_delete(
        self, db: AsyncSession, *, product_sku: str, warehouse_code: str
    ) -> bool:
        result = await db.execute(
            update(Inventory)
            .where(
                and_(
                    Inventory.product_sku == product_sku,
                    Inventory.warehouse_code == warehouse_code,
                )
            )
            .values(is_deleted=1)
        )
        return result.rowcount > 0


crud_inventory = CRUDInventory(Inventory)
