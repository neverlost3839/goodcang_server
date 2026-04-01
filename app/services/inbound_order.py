from datetime import datetime
from typing import Any, Dict, List, Optional

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.client.inbound_order import goodcang_inbound_order
from app.crud.crud_inbound_order import crud_inbound_order, crud_inbound_order_item
from app.models.inbound_order import InboundOrder, InboundOrderItem
from app.schemas.inbound_order import (
    InboundOrderCreate,
    InboundOrderItemOut,
    InboundOrderOut,
    InboundOrderUpdate,
)


class InboundOrderService:
    async def create(
        self, db: AsyncSession, *, obj_in: InboundOrderCreate
    ) -> InboundOrderOut:
        items_data = obj_in.items

        items_payload = []
        for item in items_data:
            for box_detail in item.box_details:
                items_payload.append(
                    {
                        "box_no": item.box_no,
                        "reference_box_no": item.reference_box_no,
                        "product_sku": box_detail.product_sku,
                        "quantity": box_detail.quantity,
                        "fba_product_code": box_detail.fba_product_code,
                        "data_code": box_detail.data_code,
                        "serial_number": box_detail.serial_number,
                    }
                )

        api_payload: Dict[str, Any] = {
            "transit_type": obj_in.transit_type,
            "receiving_shipping_type": obj_in.receiving_shipping_type,
            "warehouse_code": obj_in.warehouse_code,
            "items": items_payload,
            "reference_no": obj_in.reference_no,
            "sm_code": obj_in.sm_code,
            "transit_warehouse_code": obj_in.transit_warehouse_code,
            "customs_type": obj_in.customs_type,
            "collecting_service": obj_in.collecting_service,
            "collecting_time": obj_in.collecting_time.strftime("%Y-%m-%d %H:%M:%S")
            if obj_in.collecting_time
            else None,
            "value_add_service": obj_in.value_add_service,
            "clearance_service": obj_in.clearance_service,
            "import_company": obj_in.import_company,
            "export_company": obj_in.export_company,
            "car_model_code": obj_in.car_model_code,
            "tracking_number": obj_in.tracking_number,
            "eta_date": obj_in.eta_date.strftime("%Y-%m-%d")
            if obj_in.eta_date
            else None,
            "receiving_desc": obj_in.receiving_desc,
            "verify": obj_in.verify,
            "weight": obj_in.weight,
            "volume": obj_in.volume,
            "wp_code": obj_in.wp_code,
            "is_delay": obj_in.is_delay,
            "is_rollover": obj_in.is_rollover,
        }

        if obj_in.shiper_address:
            api_payload["shiper_address"] = {
                "sa_contacter": obj_in.shiper_address.sa_contacter,
                "sa_contact_phone": obj_in.shiper_address.sa_contact_phone,
                "sa_country_code": obj_in.shiper_address.sa_country_code,
                "sa_state": obj_in.shiper_address.sa_state,
                "sa_city": obj_in.shiper_address.sa_city,
                "sa_region": obj_in.shiper_address.sa_region,
                "sa_address1": obj_in.shiper_address.sa_address1,
                "sa_address2": obj_in.shiper_address.sa_address2,
            }

        if obj_in.collecting_address:
            api_payload["collecting_address"] = [
                {
                    "ca_first_name": addr.ca_first_name,
                    "ca_last_name": addr.ca_last_name,
                    "ca_contact_phone": addr.ca_contact_phone,
                    "ca_state": addr.ca_state,
                    "ca_city": addr.ca_city,
                    "ca_country_code": addr.ca_country_code,
                    "ca_zipcode": addr.ca_zipcode,
                    "ca_address1": addr.ca_address1,
                    "ca_address2": addr.ca_address2,
                }
                for addr in obj_in.collecting_address
            ]

        if obj_in.customers_send_info:
            api_payload["customers_send_info"] = {
                "arrive_transfer_warehouse_time": obj_in.customers_send_info.arrive_transfer_warehouse_time.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                if obj_in.customers_send_info.arrive_transfer_warehouse_time
                else None,
                "company_name": obj_in.customers_send_info.company_name,
                "delivery_code": obj_in.customers_send_info.delivery_code,
                "plate_no": obj_in.customers_send_info.plate_no,
                "driver_name": obj_in.customers_send_info.driver_name,
                "driver_phone": obj_in.customers_send_info.driver_phone,
            }

        api_result = await goodcang_inbound_order.create_grn(**api_payload)

        if api_result.get("ask") != "Success":
            raise HTTPException(
                status_code=400,
                detail=api_result.get("message", "创建入库单API调用失败"),
            )

        receiving_code = api_result.get("data", {}).get("receiving_code")

        order_data = obj_in.model_dump(exclude={"items"})

        if obj_in.shiper_address:
            order_data["sa_contacter"] = obj_in.shiper_address.sa_contacter
            order_data["sa_contact_phone"] = obj_in.shiper_address.sa_contact_phone
            order_data["sa_country_code"] = obj_in.shiper_address.sa_country_code
            order_data["sa_state"] = obj_in.shiper_address.sa_state
            order_data["sa_city"] = obj_in.shiper_address.sa_city
            order_data["sa_region"] = obj_in.shiper_address.sa_region
            order_data["sa_address1"] = obj_in.shiper_address.sa_address1
            order_data["sa_address2"] = obj_in.shiper_address.sa_address2

        if obj_in.collecting_address and obj_in.collecting_address[0]:
            ca = obj_in.collecting_address[0]
            order_data["ca_first_name"] = ca.ca_first_name
            order_data["ca_last_name"] = ca.ca_last_name
            order_data["ca_contact_phone"] = ca.ca_contact_phone
            order_data["ca_state"] = ca.ca_state
            order_data["ca_city"] = ca.ca_city
            order_data["ca_country_code"] = ca.ca_country_code
            order_data["ca_zipcode"] = ca.ca_zipcode
            order_data["ca_address1"] = ca.ca_address1
            order_data["ca_address2"] = ca.ca_address2

        if obj_in.customers_send_info:
            order_data["arrive_transfer_warehouse_time"] = (
                obj_in.customers_send_info.arrive_transfer_warehouse_time
            )
            order_data["company_name"] = obj_in.customers_send_info.company_name
            order_data["delivery_code"] = obj_in.customers_send_info.delivery_code
            order_data["plate_no"] = obj_in.customers_send_info.plate_no
            order_data["driver_name"] = obj_in.customers_send_info.driver_name
            order_data["driver_phone"] = obj_in.customers_send_info.driver_phone

        order_data["receiving_code"] = receiving_code

        db_obj = InboundOrder(**order_data)
        db.add(db_obj)
        await db.flush()
        await db.refresh(db_obj)

        for item in items_data:
            for box_detail in item.box_details:
                order_item = InboundOrderItem(
                    inbound_order_id=db_obj.id,
                    box_no=item.box_no,
                    reference_box_no=item.reference_box_no,
                    product_sku=box_detail.product_sku,
                    quantity=box_detail.quantity,
                    fba_product_code=box_detail.fba_product_code,
                    data_code=box_detail.data_code,
                    serial_number=box_detail.serial_number,
                )
                db.add(order_item)

        await db.commit()
        await db.refresh(db_obj)

        return InboundOrderOut.model_validate(db_obj)

    async def get(self, db: AsyncSession, *, id: int) -> InboundOrderOut:
        db_obj = await crud_inbound_order.get(db, id=id)
        if not db_obj or db_obj.is_deleted == 1:
            raise HTTPException(status_code=404, detail=f"入库单ID {id} 不存在")
        return InboundOrderOut.model_validate(db_obj)

    async def list(
        self,
        db: AsyncSession,
        *,
        page: int = 1,
        page_size: int = 20,
        receiving_code: Optional[str] = None,
        reference_no: Optional[str] = None,
        warehouse_code: Optional[str] = None,
    ) -> Dict[str, Any]:
        from app.models.inbound_order import InboundOrder

        filters = [InboundOrder.is_deleted == 0]

        if receiving_code:
            filters.append(InboundOrder.receiving_code == receiving_code)
        if reference_no:
            filters.append(InboundOrder.reference_no.ilike(f"%{reference_no}%"))
        if warehouse_code:
            filters.append(InboundOrder.warehouse_code == warehouse_code)

        skip = (page - 1) * page_size

        items = await crud_inbound_order.get_multi(
            db, skip=skip, limit=page_size, filters=filters
        )

        total = await crud_inbound_order.count(db, filters=filters)

        total_pages = (total + page_size - 1) // page_size

        return {
            "items": [InboundOrderOut.model_validate(item) for item in items],
            "total": total,
            "page": page,
            "page_size": page_size,
            "total_pages": total_pages,
        }

    async def update(
        self, db: AsyncSession, *, id: int, obj_in: InboundOrderUpdate
    ) -> InboundOrderOut:
        db_obj = await crud_inbound_order.get(db, id=id)
        if not db_obj or db_obj.is_deleted == 1:
            raise HTTPException(status_code=404, detail=f"入库单ID {id} 不存在")
        updated_obj = await crud_inbound_order.update(
            db=db, db_obj=db_obj, obj_in=obj_in
        )
        return InboundOrderOut.model_validate(updated_obj)


inbound_order_service = InboundOrderService()
