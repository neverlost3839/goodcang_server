from typing import Any, Optional, List
from app.client.base import GoodCangBase


class GoodCangProduct(GoodCangBase):
    """GoodCang 商品 API 客户端"""

    async def get_category(self) -> dict[str, Any]:
        """
        获取系统品类

        API文档: https://oms.goodcang.net/public_open/product/get_category

        Returns:
            dict: {
                "ask": "Success",
                "data": [
                    {
                        "category_id": 1,
                        "category_level": 0,
                        "category_name": "机械设备/测量检测设备及其零配件(NEW)",
                        "category_name_en": "Mechanical, Testing Equipment & Accessories",
                        "parent_category_id": 0
                    }
                ],
                "message": "Success"
            }
        """
        return await self._post("/product/get_category", data={})

    async def get_declare_commodity_name_list(self) -> dict[str, Any]:
        """
        获取建议中文申报品名

        API文档: https://oms.goodcang.net/public_open/product/get_declare_commodity_name_list

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "data": {
                    "declare_list": ["一次成像照相机", "18英寸越野自行车"]
                }
            }
        """
        return await self._post("/product/get_declare_commodity_name_list", data={})

    async def get_material_list(self) -> dict[str, Any]:
        """
        获取建议材质

        API文档: https://oms.goodcang.net/public_open/product/get_material_list

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "data": {
                    "material_list": ["金属", "金属+复合木+塑料"]
                }
            }
        """
        return await self._post("/product/get_material_list", data={})

    async def get_product_sku_list(
        self,
        page: int,
        page_size: int,
        product_sku: Optional[str] = None,
        product_sku_arr: Optional[List[str]] = None,
        product_update_time_from: Optional[str] = None,
        product_update_time_to: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        获取商品列表

        API文档: https://oms.goodcang.net/public_open/product/get_product_sku_list

        Args:
            page: 查询页数 (必填)
            page_size: 每页显示的SKU数量 (必填, 最大200)
            product_sku: SKU (可选, 精确搜索匹配)
            product_sku_arr: 多个SKU数组 (可选, 精确搜索匹配)
            product_update_time_from: 修改开始时间 (可选, 格式: Y-m-d H:i:s)
            product_update_time_to: 修改结束时间 (可选, 格式: Y-m-d H:i:s)

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "data": [...],
                "count": 13967
            }
        """
        payload = {
            "page": page,
            "pageSize": page_size,
        }
        if product_sku:
            payload["product_sku"] = product_sku
        if product_sku_arr:
            payload["product_sku_arr"] = product_sku_arr
        if product_update_time_from:
            payload["product_update_time_from"] = product_update_time_from
        if product_update_time_to:
            payload["product_update_time_to"] = product_update_time_to

        return await self._post("/product/get_product_sku_list", data=payload)

    async def serial_number_list(
        self,
        code_type: int = 1,
        status: Optional[int] = None,
        code_value: Optional[str] = None,
        time_type: int = 1,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        page: int = 1,
        page_size: int = 100,
    ) -> dict[str, Any]:
        """
        获取序列号列表

        API文档: https://oms.goodcang.net/public_open/product/serial_number_list

        Args:
            code_type: 查询类型 (可选, 默认1)
                1: 序列号
                2: 商品编码
                3: 订单号
                4: 序列号集成码
                5: 入库单号
            status: 状态 (可选)
                0: 待收货
                1: 待出库
                2: 已出库
                3: 已废弃
            code_value: 查询值 (可选)
            time_type: 查询时间类型 (可选, 默认1)
                1: 创建时间
                3: 出库时间
                4: 废弃时间
            start_time: 开始时间 (可选)
            end_time: 结束时间 (可选)
            page: 分页页码 (可选, 默认1)
            page_size: 分页数量 (可选, 默认100)

        Returns:
            dict: {
                "code": 0,
                "message": "success",
                "data": {
                    "list": [...],
                    "total": 33
                }
            }
        """
        payload = {
            "code_type": code_type,
            "time_type": time_type,
            "page": page,
            "pageSize": page_size,
        }
        if status is not None:
            payload["status"] = status
        if code_value:
            payload["code_value"] = code_value
        if start_time:
            payload["start_time"] = start_time
        if end_time:
            payload["end_time"] = end_time

        return await self._post("/product/serial_number_list", data=payload)


goodcang_product = GoodCangProduct()
