from typing import Any, Optional, List
from app.client.base import GoodCangBase


class GoodCangReturnOrder(GoodCangBase):
    """GoodCang 退货单 API 客户端"""

    async def search(
        self,
        reference_no: Optional[str] = None,
        asro_codes: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        退货单查询

        API文档: https://oms.goodcang.net/public_open/return_order/search

        Args:
            reference_no: 参考号 (可选, 最大50字符)
            asro_codes: 退件单号 (可选, 最大32字符)
            参数二选一或者2个都填

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "data": [...]
            }
        """
        if not reference_no and not asro_codes:
            raise ValueError("reference_no 和 asro_codes 至少填写一个")

        payload = {}
        if reference_no:
            payload["reference_no"] = reference_no
        if asro_codes:
            payload["asroCodes"] = asro_codes

        return await self._post("/return_order/search", data=payload)

    async def list(
        self,
        current_page: int = 1,
        page_size: int = 10,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        start_update_time: Optional[str] = None,
        end_update_time: Optional[str] = None,
        asro_status: Optional[str] = None,
        cass_type: Optional[str] = None,
        asro_codes: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        退货单列表

        API文档: https://oms.goodcang.net/public_open/return_order/list

        Args:
            current_page: 当前页 (可选, 默认1)
            page_size: 每页数据长度 (可选, 默认10)
            start_time: 创建开始时间 (可选, 格式: YYYY-MM-DD HH:MM:SS)
            end_time: 创建结束时间 (可选, 格式: YYYY-MM-DD HH:MM:SS)
            start_update_time: 修改开始时间 (可选)
            end_update_time: 修改结束时间 (可选)
            asro_status: 退件状态 (可选)
                0: 草稿
                1: 已提交
                4: 收货完成
                5: 处理完成
                6: 废弃
                7: 处理中
            cass_type: 退件类型 (可选)
                0: 服务商退件
                1: 客户退件
                2: 未预报退件
            asro_codes: 退件单号 (可选)

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "data": [...]
            }
        """
        payload = {
            "currentPage": str(current_page),
            "pageSize": str(page_size),
        }
        if start_time:
            payload["startTime"] = start_time
        if end_time:
            payload["endTime"] = end_time
        if start_update_time:
            payload["startUpdateTime"] = start_update_time
        if end_update_time:
            payload["endUpdateTime"] = end_update_time
        if asro_status:
            payload["asroStatus"] = asro_status
        if cass_type:
            payload["cassType"] = cass_type
        if asro_codes:
            payload["asroCodes"] = asro_codes

        return await self._post("/return_order/list", data=payload)

    async def unauthorized_list(
        self,
        current_page: int = 1,
        page_size: int = 10,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        未预报退件列表

        API文档: https://oms.goodcang.net/public_open/return_order/unauthorized_list

        Args:
            current_page: 当前页 (可选, 默认1)
            page_size: 每页数据长度 (可选, 默认10)
            start_time: 创建开始时间 (可选)
            end_time: 创建结束时间 (可选)

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "data": [...]
            }
        """
        payload = {
            "currentPage": str(current_page),
            "pageSize": str(page_size),
        }
        if start_time:
            payload["startTime"] = start_time
        if end_time:
            payload["endTime"] = end_time

        return await self._post("/return_order/unauthorized_list", data=payload)

    async def claim_order_list(
        self,
        current_page: int = 1,
        page_size: int = 10,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        claim_status: Optional[int] = None,
    ) -> dict[str, Any]:
        """
        索赔单列表

        API文档: https://oms.goodcang.net/public_open/return_order/claim_order_list

        Args:
            current_page: 当前页 (可选, 默认1)
            page_size: 每页数据长度 (可选, 默认10)
            start_time: 创建开始时间 (可选)
            end_time: 创建结束时间 (可选)
            claim_status: 索赔状态 (可选)

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "data": [...]
            }
        """
        payload = {
            "currentPage": str(current_page),
            "pageSize": str(page_size),
        }
        if start_time:
            payload["startTime"] = start_time
        if end_time:
            payload["endTime"] = end_time
        if claim_status is not None:
            payload["claimStatus"] = claim_status

        return await self._post("/return_order/claim_order_list", data=payload)

    async def get_service_config(self) -> dict[str, Any]:
        """
        获取退件服务配置

        API文档: https://oms.goodcang.net/public_open/return_order/get_service_config

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "data": {...}
            }
        """
        return await self._post("/return_order/get_service_config", data={})

    async def claim_order_details(
        self,
        claim_code: str,
    ) -> dict[str, Any]:
        """
        索赔单详情

        API文档: https://oms.goodcang.net/public_open/return_order/claim_order_details

        Args:
            claim_code: 索赔单号 (必填)

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "data": {...}
            }
        """
        payload = {
            "claim_code": claim_code,
        }
        return await self._post("/return_order/claim_order_details", data=payload)


goodcang_return_order = GoodCangReturnOrder()
