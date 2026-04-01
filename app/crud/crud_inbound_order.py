from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.inbound_order import InboundOrder, InboundOrderItem
from app.schemas.inbound_order import InboundOrderCreate, InboundOrderUpdate


class CRUDInboundOrder(CRUDBase[InboundOrder, InboundOrderCreate, InboundOrderUpdate]):
    async def get_by_receiving_code(
        self, db: AsyncSession, receiving_code: str
    ) -> Optional[InboundOrder]:
        result = await db.execute(
            select(InboundOrder).where(
                InboundOrder.receiving_code == receiving_code,
                InboundOrder.is_deleted == 0,
            )
        )
        return result.scalar_one_or_none()

    async def get_by_reference_no(
        self, db: AsyncSession, reference_no: str
    ) -> Optional[InboundOrder]:
        result = await db.execute(
            select(InboundOrder).where(
                InboundOrder.reference_no == reference_no,
                InboundOrder.is_deleted == 0,
            )
        )
        return result.scalar_one_or_none()


class CRUDInboundOrderItem(CRUDBase[InboundOrderItem, dict, dict]):
    async def get_multi_by_order_id(
        self, db: AsyncSession, inbound_order_id: int
    ) -> List[InboundOrderItem]:
        result = await db.execute(
            select(InboundOrderItem).where(
                InboundOrderItem.inbound_order_id == inbound_order_id,
                InboundOrderItem.is_deleted == 0,
            )
        )
        return list(result.scalars().all())


crud_inbound_order = CRUDInboundOrder(InboundOrder)
crud_inbound_order_item = CRUDInboundOrderItem(InboundOrderItem)
