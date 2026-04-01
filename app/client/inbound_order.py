from typing import Any, Optional, List
from app.client.base import GoodCangBase


class GoodCangInboundOrder(GoodCangBase):
    """GoodCang 入库单 API 客户端"""

    async def get_vat_list(
        self,
        page: int = 1,
        page_size: int = 10,
    ) -> dict[str, Any]:
        """
        获取进出口商列表

        API文档: https://oms.goodcang.net/public_open/inbound_order/get_vat_list

        Args:
            page: 当前页 (可选, 默认1)
            page_size: 每页数据长度 (可选, 最大200, 默认10)

        Returns:
            dict: {
                "ask": "Success",
                "message": "",
                "data": [...]
            }
        """
        payload = {
            "page": page,
            "page_size": page_size,
        }
        return await self._post("/inbound_order/get_vat_list", data=payload)

    async def get_smcode_twc_to_warehouse(self) -> dict[str, Any]:
        """
        获取物流产品与目的仓中转仓

        API文档: https://oms.goodcang.net/public_open/inbound_order/get_smcode_twc_to_warehouse

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "data": {
                    "AIR": [...],
                    "LCL": [...],
                    "EXPRESS": [...],
                    "FCL": [...]
                }
            }
        """
        return await self._post("/inbound_order/get_smcode_twc_to_warehouse", data={})

    async def get_grn_list(
        self,
        page: int,
        page_size: int,
        receiving_code_arr: Optional[List[str]] = None,
        create_date_from: Optional[str] = None,
        create_date_to: Optional[str] = None,
        modify_date_from: Optional[str] = None,
        modify_date_to: Optional[str] = None,
        is_rollover: Optional[int] = None,
    ) -> dict[str, Any]:
        """
        获取入库单列表

        API文档: https://oms.goodcang.net/public_open/inbound_order/get_grn_list

        Args:
            page: 当前页 (必填)
            page_size: 每页数据长度 (必填, 最大100)
            receiving_code_arr: 多个入库单号数组 (可选, 最多100)
            create_date_from: 创建开始日期 (可选, 格式: YYYY-MM-DD HH:MM:SS)
            create_date_to: 创建结束日期 (可选, 格式: YYYY-MM-DD HH:MM:SS)
            modify_date_from: 修改开始时间 (可选)
            modify_date_to: 修改结束时间 (可选)
            is_rollover: 是否仓库装箱商品 (可选, 0否, 1是)

        Returns:
            dict: {
                "ask": "Success",
                "count": 2,
                "data": [...],
                "message": "Success"
            }
        """
        payload = {
            "page": page,
            "page_size": page_size,
        }
        if receiving_code_arr:
            payload["receiving_code_arr"] = receiving_code_arr
        if create_date_from:
            payload["create_date_from"] = create_date_from
        if create_date_to:
            payload["create_date_to"] = create_date_to
        if modify_date_from:
            payload["modify_date_from"] = modify_date_from
        if modify_date_to:
            payload["modify_date_to"] = modify_date_to
        if is_rollover is not None:
            payload["is_rollover"] = is_rollover

        return await self._post("/inbound_order/get_grn_list", data=payload)

    async def get_grn_detail(
        self,
        receiving_code: str,
    ) -> dict[str, Any]:
        """
        获取入库单明细

        API文档: https://oms.goodcang.net/public_open/inbound_order/get_grn_detail

        Args:
            receiving_code: 入库单号 (必填)

        Returns:
            dict: {
                "ask": "Success",
                "message": "",
                "data": {
                    "receiving_code": "RV000012-150716-0001",
                    ...
                }
            }
        """
        payload = {
            "receiving_code": receiving_code,
        }
        return await self._post("/inbound_order/get_grn_detail", data=payload)

    async def get_batch(
        self,
        receiving_code: str,
    ) -> dict[str, Any]:
        """
        获取上架批次

        API文档: https://oms.goodcang.net/public_open/inbound_order/get_batch

        Args:
            receiving_code: 入库单号 (必填)

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "data": [...]
            }
        """
        payload = {
            "receiving_code": receiving_code,
        }
        return await self._post("/inbound_order/get_batch", data=payload)

    async def get_receipt_batch(
        self,
        receiving_code: str,
    ) -> dict[str, Any]:
        """
        获取收货批次

        API文档: https://oms.goodcang.net/public_open/inbound_order/get_receipt_batch

        Args:
            receiving_code: 入库单号 (必填)

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "data": {...}
            }
        """
        payload = {
            "receiving_code": receiving_code,
        }
        return await self._post("/inbound_order/get_receipt_batch", data=payload)

    async def cars_model(self) -> dict[str, Any]:
        """
        获取车型

        API文档: https://oms.goodcang.net/public_open/inbound_order/cars_model

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "data": {...}
            }
        """
        return await self._post("/inbound_order/cars_model", data={})

    async def get_clearance_document(
        self,
        receiving_list: List[str],
    ) -> dict[str, Any]:
        """
        获取清关文件上传状态

        API文档: https://oms.goodcang.net/public_open/inbound_order/get_clearance_document

        Args:
            receiving_list: 入库单号数组 (必填)

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "data": [...]
            }
        """
        payload = {
            "receiving_list": receiving_list,
        }
        return await self._post("/inbound_order/get_clearance_document", data=payload)


goodcang_inbound_order = GoodCangInboundOrder()
