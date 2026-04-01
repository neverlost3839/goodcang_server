from collections import defaultdict
from datetime import datetime
from typing import Any, Dict, List, Optional

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.client.inventory import goodcang_inventory
from app.client.order import goodcang_order
from app.crud.crud_order import crud_order
from app.models.order import Order
from app.models.order_item import OrderItem
from app.schemas.common import PaginatedData
from app.schemas.order import (
    OrderCreate,
    OrderItemCreate,
    OrderOut,
    OrderUpdate,
)


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
        warehouse_code = obj_in.warehouse_code or ""
        if not warehouse_code:
            raise HTTPException(status_code=400, detail="发货仓库代码不能为空")

        unique_skus = set(item.product_sku for item in obj_in.items)
        product_sku_arr = list(unique_skus)

        api_result = await goodcang_inventory.get_product_inventory(
            page=1,
            page_size=200,
            product_sku_arr=product_sku_arr,
            warehouse_code=warehouse_code,
        )

        if api_result.get("ask") != "Success":
            raise HTTPException(
                status_code=400, detail=api_result.get("message", "库存查询API调用失败")
            )

        api_data = api_result.get("data", [])
        inventory_map: Dict[str, Dict[str, Any]] = {
            item.get("product_sku"): item for item in api_data
        }

        required_quantities: Dict[str, int] = defaultdict(int)
        for item in obj_in.items:
            required_quantities[item.product_sku] += item.quantity

        insufficient_items = []
        for product_sku, required_qty in required_quantities.items():
            inventory_item = inventory_map.get(product_sku, {})
            sellable = inventory_item.get("sellable", 0)
            if sellable < required_qty:
                insufficient_items.append(
                    f"SKU {product_sku}: 需求{required_qty}, 可售{sellable}"
                )

        if insufficient_items:
            raise HTTPException(
                status_code=400,
                detail=f"库存不足: {'; '.join(insufficient_items)}",
            )

        order_data = obj_in.model_dump(exclude={"items"})
        items_data = obj_in.items

        api_order_result = await goodcang_order.create_order(
            shipping_method=obj_in.shipping_method or "",
            warehouse_code=warehouse_code,
            country_code=obj_in.country_code,
            province=obj_in.province,
            city=obj_in.city,
            address1=obj_in.address1,
            zipcode=obj_in.zipcode,
            name=obj_in.name,
            reference_no=obj_in.reference_no,
            platform=obj_in.platform,
            company=obj_in.company,
            address2=obj_in.address2,
            doorplate=obj_in.doorplate,
            last_name=obj_in.last_name,
            cell_phone=obj_in.cell_phone,
            phone=obj_in.phone,
            email=obj_in.email,
            order_desc=obj_in.order_desc,
            customer_package_requirement=obj_in.customer_package_requirement,
            verify=obj_in.verify,
            is_shipping_method_not_allow_update=obj_in.is_shipping_method_not_allow_update,
            is_signature=obj_in.is_signature,
            is_insurance=obj_in.is_insurance,
            insurance_value=obj_in.insurance_value,
            fba_shipment_id=obj_in.fba_shipment_id,
            property_label=obj_in.property_label,
            business_type=obj_in.business_type,
            is_change_label=obj_in.is_change_label,
            age_detection=obj_in.age_detection,
            is_liftgate=obj_in.lift_gate,
            attachment_ids=obj_in.attachment_ids,
            estimated_arrival_date=obj_in.estimated_arrival_date.strftime("%Y-%m-%d")
            if obj_in.estimated_arrival_date
            else None,
            estimated_arrival_time=obj_in.estimated_arrival_time,
            sender_info=obj_in.sender_info,
            vat_change_info=obj_in.vat_change_info,
            is_euro_label=obj_in.is_euro_label,
            vas=obj_in.vas,
            is_warehouse_packing=obj_in.is_warehouse_packing,
            carton_info=obj_in.carton_info,
            truck_info=obj_in.truck_info,
            items=[
                {
                    "product_sku": item.product_sku,
                    "quantity": item.quantity,
                    "transaction_id": item.transaction_id,
                    "item_id": item.item_id,
                    "fba_product_code": item.fba_product_code,
                    "euro_terms_code": item.euro_terms_code,
                    "label_replacement_qty": item.label_replacement_qty,
                    "product_declared_value": item.product_declared_value,
                    "hs_code": item.hs_code,
                }
                for item in items_data
            ],
        )

        if api_order_result.get("ask") != "Success":
            raise HTTPException(
                status_code=400,
                detail=api_order_result.get("message", "创建订单API调用失败"),
            )

        order_code = api_order_result.get("order_code")
        order_data["order_code"] = order_code

        db_obj = Order(**order_data)
        db.add(db_obj)
        await db.flush()
        await db.refresh(db_obj)

        for item in items_data:
            order_item = OrderItem(
                order_id=db_obj.id,
                product_sku=item.product_sku,
                quantity=item.quantity,
                transaction_id=item.transaction_id,
                item_id=item.item_id,
                fba_product_code=item.fba_product_code,
                euro_terms_code=item.euro_terms_code,
                label_replacement_qty=item.label_replacement_qty,
                product_declared_value=item.product_declared_value,
                hs_code=item.hs_code,
            )
            db.add(order_item)

        await db.commit()
        await db.refresh(db_obj)

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
