from typing import Any, Optional, List
from app.client.base import GoodCangBase


class GoodCangInventory(GoodCangBase):
    """GoodCang 库存 API 客户端"""

    async def get_product_inventory(
        self,
        page: int = 1,
        page_size: int = 10,
        product_sku: Optional[str] = None,
        product_sku_arr: Optional[List[str]] = None,
        warehouse_code: Optional[str] = None,
        warehouse_code_arr: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """
        获取商品库存

        API文档: https://oms.goodcang.net/public_open/inventory/get_product_inventory

        Args:
            page_size: 每页数据长度 (必填, 最大200)
            page: 当前页 (必填)
            product_sku: 商品编码 (可选, 精确匹配)
            product_sku_arr: 多个SKU数组 (可选, 最多200个)
            warehouse_code: 仓库代码 (可选)
            warehouse_code_arr: 多个仓库代码数组 (可选)

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "count": 137,
                "data": [
                    {
                        "product_barcode": "000011-TEST150810002",
                        "product_sku": "TEST150810002",
                        "warehouse_code": "USEA",
                        "onway": 1482,
                        "pending": 31,
                        "sellable": 10335,
                        "unsellable": 0,
                        "reserved": 10,
                        "shipped": 18,
                        "sold_shared": 0,
                        "tune_out": 2,
                        "tune_in": 1,
                        "product_sales_value": "0.00",
                        "warehouse_desc": "美东仓库",
                        "stocking": 10,
                        "pi_no_stock": 1,
                        "pi_freeze": 0
                    }
                ]
            }
        """
        payload = {
            "pageSize": page_size,
            "page": page,
        }
        if product_sku:
            payload["product_sku"] = product_sku
        if product_sku_arr:
            payload["product_sku_arr"] = product_sku_arr
        if warehouse_code:
            payload["warehouse_code"] = warehouse_code
        if warehouse_code_arr:
            payload["warehouse_code_arr"] = warehouse_code_arr

        return await self._post("/inventory/get_product_inventory", data=payload)


goodcang_inventory = GoodCangInventory()
