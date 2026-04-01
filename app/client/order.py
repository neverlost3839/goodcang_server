from typing import Any, Optional, List
from app.client.base import GoodCangBase


class GoodCangOrder(GoodCangBase):
    """GoodCang 订单 API 客户端"""

    async def get_order_by_code(
        self,
        order_code: str,
    ) -> dict[str, Any]:
        """
        根据订单号获取单票订单信息

        API文档: https://oms.goodcang.net/public_open/order/get_order_by_code

        Args:
            order_code: 订单号 (必填)

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "data": {...}
            }
        """
        payload = {
            "order_code": order_code,
        }
        return await self._post("/order/get_order_by_code", data=payload)

    async def get_order_list(
        self,
        page: int,
        page_size: int,
        order_status: Optional[str] = None,
        warehouse_code: Optional[str] = None,
        shipping_method: Optional[str] = None,
        country_code: Optional[str] = None,
        reference_no: Optional[str] = None,
        order_code: Optional[str] = None,
        date_type: Optional[int] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        获取订单列表

        API文档: https://oms.goodcang.net/public_open/order/get_order_list

        Args:
            page: 当前页 (必填)
            page_size: 每页数据长度 (必填, 最大100)
            order_status: 订单状态 (可选)
                C: 待发货审核
                W: 待发货
                D: 已发货
                H: 暂存
            warehouse_code: 仓库代码 (可选)
            shipping_method: 物流产品代码 (可选)
            country_code: 收件人国家 (可选)
            reference_no: 客户参考号 (可选)
            order_code: 订单号 (可选)
            date_type: 日期类型 (可选)
                1: 创建时间
                2: 发货时间
            date_from: 开始日期 (可选)
            date_to: 结束日期 (可选)

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
        if order_status:
            payload["order_status"] = order_status
        if warehouse_code:
            payload["warehouse_code"] = warehouse_code
        if shipping_method:
            payload["shipping_method"] = shipping_method
        if country_code:
            payload["country_code"] = country_code
        if reference_no:
            payload["reference_no"] = reference_no
        if order_code:
            payload["order_code"] = order_code
        if date_type is not None:
            payload["date_type"] = date_type
        if date_from:
            payload["date_from"] = date_from
        if date_to:
            payload["date_to"] = date_to

        return await self._post("/order/get_order_list", data=payload)

    async def get_draft_order_list(
        self,
        page: int,
        page_size: int,
        warehouse_code: Optional[str] = None,
        reference_no: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        获取草稿订单列表

        API文档: https://oms.goodcang.net/public_open/order/get_draft_order_list

        Args:
            page: 当前页 (必填)
            page_size: 每页数据长度 (必填, 最大100)
            warehouse_code: 仓库代码 (可选)
            reference_no: 客户参考号 (可选)

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
        if reference_no:
            payload["reference_no"] = reference_no

        return await self._post("/order/get_draft_order_list", data=payload)

    async def batch_query_tracking_status(
        self,
        tracking_numbers: List[str],
    ) -> dict[str, Any]:
        """
        批量查询物流追踪状态

        API文档: https://oms.goodcang.net/public_open/order/batch_query_tracking_status

        Args:
            tracking_numbers: 物流追踪号数组 (必填)

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "data": [...]
            }
        """
        payload = {
            "tracking_numbers": tracking_numbers,
        }
        return await self._post("/order/batch_query_tracking_status", data=payload)


goodcang_order = GoodCangOrder()
