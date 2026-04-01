from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.inbound_order import (
    InboundOrderCreate,
    InboundOrderOut,
    InboundOrderUpdate,
)
from app.services.inbound_order import inbound_order_service

router = APIRouter(prefix="/inbound_order", tags=["入库单"])


@router.post("/create", response_model=InboundOrderOut)
async def create_inbound_order(
    obj_in: InboundOrderCreate,
    db: AsyncSession = Depends(get_db),
):
    return await inbound_order_service.create(db=db, obj_in=obj_in)


@router.get("/{id}", response_model=InboundOrderOut)
async def get_inbound_order(
    id: int,
    db: AsyncSession = Depends(get_db),
):
    return await inbound_order_service.get(db=db, id=id)


@router.get("/", response_model=dict)
async def get_inbound_order_list(
    page: int = Query(1, ge=1, description="当前页码"),
    page_size: int = Query(20, ge=1, le=100, description="每页条数"),
    receiving_code: Optional[str] = Query(None, description="入库单号"),
    reference_no: Optional[str] = Query(None, description="参考号"),
    warehouse_code: Optional[str] = Query(None, description="仓库编码"),
    db: AsyncSession = Depends(get_db),
):
    return await inbound_order_service.list(
        db=db,
        page=page,
        page_size=page_size,
        receiving_code=receiving_code,
        reference_no=reference_no,
        warehouse_code=warehouse_code,
    )


@router.put("/{id}", response_model=InboundOrderOut)
async def update_inbound_order(
    id: int,
    obj_in: InboundOrderUpdate,
    db: AsyncSession = Depends(get_db),
):
    return await inbound_order_service.update(db=db, id=id, obj_in=obj_in)
