from typing import Any, Optional, List
from app.client.base import GoodCangBase


class GoodCangInventory(GoodCangBase):
    """GoodCang 库存 API 客户端"""

    async def get_product_inventory(
        self,
        page: int,
        page_size: int,
        product_sku: Optional[str] = None,
        product_sku_arr: Optional[List[str]] = None,
        warehouse_code: Optional[str] = None,
        warehouse_code_arr: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """
        获取库存

        API文档: https://oms.goodcang.net/public_open/inventory/get_product_inventory

        Args:
            page: 当前页 (必填)
            page_size: 每页数据长度 (必填, 最大200)
            product_sku: 商品编码 (可选, 精确匹配搜索)
            product_sku_arr: 多个SKU数组 (可选, 最多200个元素)
            warehouse_code: 仓库代码 (可选)
            warehouse_code_arr: 多个仓库代码数组 (可选)

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "count": 137,
                "data": [...]
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
        if warehouse_code:
            payload["warehouse_code"] = warehouse_code
        if warehouse_code_arr:
            payload["warehouse_code_arr"] = warehouse_code_arr

        return await self._post("/inventory/get_product_inventory", data=payload)

    async def get_inventory_log(
        self,
        page: int,
        page_size: int,
        warehouse_code: Optional[str] = None,
        application_code: Optional[str] = None,
        reference_no_list: Optional[List[str]] = None,
        product_sku_list: Optional[List[str]] = None,
        create_date_from: Optional[str] = None,
        create_date_end: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        获取库存动态列表

        API文档: https://oms.goodcang.net/public_open/inventory/get_inventory_log

        Args:
            page: 当前页 (必填)
            page_size: 每页数据长度 (必填, 最大200)
            warehouse_code: 仓库代码 (可选)
            application_code: 操作类型 (可选)
                1: 调出下架
                2: 调入上架
                3: 盘点
                4: 订单签出
                5: 库存调整
                6: 售后上架
                7: 入库上架
                8: 增值完成
            reference_no_list: 操作单号数组 (可选)
            product_sku_list: 多个SKU数组 (可选, 精确匹配)
            create_date_from: 操作开始时间 (必填, 格式: YYYY-MM-DD)
            create_date_end: 操作结束时间 (必填, 格式: YYYY-MM-DD, 最大31天跨度)

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "data": [...],
                "count": 1
            }
        """
        payload = {
            "page": page,
            "pageSize": page_size,
        }
        if warehouse_code:
            payload["warehouse_code"] = warehouse_code
        if application_code is not None:
            payload["application_code"] = application_code
        if reference_no_list:
            payload["reference_no_list"] = reference_no_list
        if product_sku_list:
            payload["product_sku_list"] = product_sku_list
        if create_date_from:
            payload["create_date_from"] = create_date_from
        if create_date_end:
            payload["create_date_end"] = create_date_end

        return await self._post("/inventory/get_inventory_log", data=payload)

    async def inventory_age_list(
        self,
        page: int,
        page_size: int,
        product_sku_list: Optional[List[str]] = None,
        product_title: Optional[str] = None,
        product_title_en: Optional[str] = None,
        fifo_time_from: Optional[str] = None,
        fifo_time_to: Optional[str] = None,
        age_from: Optional[int] = None,
        age_to: Optional[int] = None,
        quantity_from: Optional[int] = None,
        quantity_to: Optional[int] = None,
        warning_age_type: Optional[int] = None,
        warehouse_code: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        获取库龄列表

        API文档: https://oms.goodcang.net/public_open/inventory/inventory_age_list

        Args:
            page: 分页页码 (必填)
            page_size: 分页数量 (必填, 最大200)
            product_sku_list: 商品编码列表 (可选, 最多200个元素)
            product_title: 商品名称 (可选)
            product_title_en: 商品英文名称 (可选)
            fifo_time_from: 上架时间起始值 (可选)
            fifo_time_to: 上架时间末位值 (可选)
            age_from: 库龄起始值 (可选)
            age_to: 库龄末位值 (可选)
            quantity_from: 在库库存起始值 (可选)
            quantity_to: 在库库存末位值 (可选)
            warning_age_type: 库龄预警 (可选)
                1: 超出
                2: 未超出
            warehouse_code: 仓库代码 (可选)

        Returns:
            dict: {
                "code": 0,
                "message": "success",
                "data": {
                    "count": 476,
                    "list": [...]
                }
            }
        """
        payload = {
            "page": page,
            "page_size": page_size,
        }
        if product_sku_list:
            payload["product_sku_list"] = product_sku_list
        if product_title:
            payload["product_title"] = product_title
        if product_title_en:
            payload["product_title_en"] = product_title_en
        if fifo_time_from:
            payload["fifo_time_from"] = fifo_time_from
        if fifo_time_to:
            payload["fifo_time_to"] = fifo_time_to
        if age_from is not None:
            payload["age_from"] = age_from
        if age_to is not None:
            payload["age_to"] = age_to
        if quantity_from is not None:
            payload["quantity_from"] = quantity_from
        if quantity_to is not None:
            payload["quantity_to"] = quantity_to
        if warning_age_type is not None:
            payload["warning_age_type"] = warning_age_type
        if warehouse_code:
            payload["warehouse_code"] = warehouse_code

        return await self._post("/inventory/inventory_age_list", data=payload)


goodcang_inventory = GoodCangInventory()
