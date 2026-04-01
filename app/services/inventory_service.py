from datetime import datetime
from typing import Any, Dict, List, Optional

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.client.inventory import goodcang_inventory
from app.crud.crud_inventory import crud_inventory
from app.models.inventory import Inventory
from app.schemas.common import PaginatedData
from app.schemas.inventory import InventoryCreate, InventoryOut, InventoryUpdate


class InventoryService:
    async def list(
        self,
        db: AsyncSession,
        *,
        page: int = 1,
        page_size: int = 20,
        product_sku: Optional[str] = None,
        product_sku_arr: Optional[List[str]] = None,
        warehouse_code: Optional[str] = None,
        warehouse_code_arr: Optional[List[str]] = None,
    ) -> PaginatedData[InventoryOut]:
        skip = (page - 1) * page_size

        items = await crud_inventory.get_multi(
            db,
            skip=skip,
            limit=page_size,
            product_sku=product_sku,
            product_sku_arr=product_sku_arr,
            warehouse_code=warehouse_code,
            warehouse_code_arr=warehouse_code_arr,
        )

        total = await crud_inventory.count(
            db,
            product_sku=product_sku,
            product_sku_arr=product_sku_arr,
            warehouse_code=warehouse_code,
            warehouse_code_arr=warehouse_code_arr,
        )

        total_pages = (total + page_size - 1) // page_size

        return PaginatedData(
            items=[InventoryOut.model_validate(item) for item in items],
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages,
        )

    async def _fetch_all_inventory_by_warehouse(
        self,
        warehouse_code: str,
        page_size: int = 200,
    ) -> List[Dict[str, Any]]:
        all_data = []
        page = 1

        while True:
            api_result = await goodcang_inventory.get_product_inventory(
                page=page,
                page_size=page_size,
                warehouse_code=warehouse_code,
            )

            if api_result.get("ask") != "Success":
                raise HTTPException(
                    status_code=400,
                    detail=f"仓库 {warehouse_code}: {api_result.get('message', 'API调用失败')}",
                )

            data = api_result.get("data", [])
            all_data.extend(data)

            if len(data) < page_size:
                break
            page += 1

        return all_data

    async def sync(
        self,
        db: AsyncSession,
        *,
        product_sku: Optional[str] = None,
        product_sku_arr: Optional[List[str]] = None,
        warehouse_code: Optional[str] = None,
        warehouse_code_arr: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        warehouses = []
        if warehouse_code_arr:
            warehouses = warehouse_code_arr
        elif warehouse_code:
            warehouses = [warehouse_code]
        else:
            raise HTTPException(status_code=400, detail="请指定仓库代码或仓库代码数组")

        all_api_data: List[Dict[str, Any]] = []

        for warehouse in warehouses:
            warehouse_data = await self._fetch_all_inventory_by_warehouse(
                warehouse_code=warehouse
            )
            all_api_data.extend(warehouse_data)

        total_count = len(all_api_data)

        api_inventory_map: Dict[str, Dict[str, Any]] = {}
        for item in all_api_data:
            key = f"{item.get('product_sku')}_{item.get('warehouse_code')}"
            api_inventory_map[key] = item

        db_inventories = await crud_inventory.get_multi(
            db,
            skip=0,
            limit=999999,
            warehouse_code_arr=warehouses if warehouses else None,
        )

        db_inventory_map: Dict[str, Inventory] = {
            f"{inv.product_sku}_{inv.warehouse_code}": inv for inv in db_inventories
        }

        deleted_count = 0
        updated_count = 0
        created_count = 0

        for db_key, db_inv in db_inventory_map.items():
            if db_key not in api_inventory_map:
                await crud_inventory.soft_delete(
                    db,
                    product_sku=db_inv.product_sku,
                    warehouse_code=db_inv.warehouse_code,
                )
                deleted_count += 1

        for api_key, api_item in api_inventory_map.items():
            product_sku = api_item.get("product_sku")
            warehouse_code = api_item.get("warehouse_code")

            if product_sku and warehouse_code:
                if api_key in db_inventory_map:
                    db_inv = db_inventory_map[api_key]
                    await crud_inventory.update(
                        db,
                        db_obj=db_inv,
                        obj_in=InventoryUpdate(
                            product_barcode=api_item.get("product_barcode"),
                            warehouse_desc=api_item.get("warehouse_desc"),
                            onway=api_item.get("onway", 0),
                            pending=api_item.get("pending", 0),
                            sellable=api_item.get("sellable", 0),
                            unsellable=api_item.get("unsellable", 0),
                            reserved=api_item.get("reserved", 0),
                            shipped=api_item.get("shipped", 0),
                            stocking=api_item.get("stocking", 0),
                            pi_no_stock=api_item.get("pi_no_stock", 0),
                            pi_freeze=api_item.get("pi_freeze", 0),
                            product_sales_value=float(
                                api_item.get("product_sales_value", "0")
                            ),
                        ),
                    )
                    updated_count += 1
                else:
                    await crud_inventory.upsert(
                        db,
                        obj_in=InventoryCreate(
                            product_sku=product_sku,
                            product_barcode=api_item.get("product_barcode"),
                            warehouse_code=warehouse_code,
                            warehouse_desc=api_item.get("warehouse_desc"),
                            onway=api_item.get("onway", 0),
                            pending=api_item.get("pending", 0),
                            sellable=api_item.get("sellable", 0),
                            unsellable=api_item.get("unsellable", 0),
                            reserved=api_item.get("reserved", 0),
                            shipped=api_item.get("shipped", 0),
                            stocking=api_item.get("stocking", 0),
                            pi_no_stock=api_item.get("pi_no_stock", 0),
                            pi_freeze=api_item.get("pi_freeze", 0),
                            product_sales_value=float(
                                api_item.get("product_sales_value", "0")
                            ),
                        ),
                    )
                    created_count += 1

        await db.commit()

        return {
            "total_count": total_count,
            "deleted_count": deleted_count,
            "updated_count": updated_count,
            "created_count": created_count,
            "warehouses": warehouses,
        }


inventory_service = InventoryService()
