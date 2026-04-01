from typing import Any, Optional, List
from app.client.base import GoodCangBase


class GoodCangAssistant(GoodCangBase):
    """GoodCang 查件助手 API 客户端"""

    async def logistic_ticket_list(
        self,
        page: int,
        page_size: int,
        code_type: Optional[str] = None,
        code_value_list: Optional[List[str]] = None,
        io_status: Optional[int] = None,
        trail_status: Optional[str] = None,
        warehouse_code: Optional[str] = None,
        sm_code: Optional[str] = None,
        platform: Optional[str] = None,
        it_type_id: Optional[int] = None,
        time_type: Optional[str] = None,
        time_start: Optional[str] = None,
        time_end: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        获取查件列表

        API文档: https://oms.goodcang.net/public_open/assistant/logistic_ticket_list

        Args:
            page: 分页页码 (必填)
            page_size: 分页数量 (必填, 最大200)
            code_type: 查单类型 (可选)
                "io_code": 查件单号
                "order_code": 订单号
                "tracking_no": 追踪号
            code_value_list: 单号值数组 (可选, 最多200个)
            io_status: 查件状态 (可选)
                1: 草稿
                2: 待处理
                3: 处理中
                7: 已回复
                8: 完结
                10: 废弃
                11: 驳回
            trail_status: 轨迹状态 (可选, 参见TrackingCode类型)
            warehouse_code: 仓库编码 (可选)
            sm_code: 物流方式编码 (可选)
            platform: 销售平台 (可选, 大写字母)
            it_type_id: 查件类型ID (可选)
            time_type: 时间类型 (可选, 有时间区间时必填)
                "add_time": 创建时间
                "commit_time": 提交时间
                "reply_time": 回复时间
            time_start: 开始时间 (可选, 格式: YYYY-MM-DD HH:MM:SS, 186天跨度)
            time_end: 结束时间 (可选, 格式: YYYY-MM-DD HH:MM:SS, 186天跨度)

        Returns:
            dict: {
                "code": 0,
                "message": "success",
                "data": {
                    "total": 1,
                    "list": [...]
                }
            }
        """
        payload = {
            "page": page,
            "page_size": page_size,
        }
        if code_type:
            payload["code_type"] = code_type
        if code_value_list:
            payload["code_value_list"] = code_value_list
        if io_status is not None:
            payload["io_status"] = io_status
        if trail_status:
            payload["trail_status"] = trail_status
        if warehouse_code:
            payload["warehouse_code"] = warehouse_code
        if sm_code:
            payload["sm_code"] = sm_code
        if platform:
            payload["platform"] = platform
        if it_type_id is not None:
            payload["it_type_id"] = it_type_id
        if time_type:
            payload["time_type"] = time_type
        if time_start:
            payload["time_start"] = time_start
        if time_end:
            payload["time_end"] = time_end

        return await self._post("/assistant/logistic_ticket_list", data=payload)

    async def logistic_ticket_type_list(
        self,
        sm_code: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        获取查件单类型列表

        API文档: https://oms.goodcang.net/public_open/assistant/logistic_ticket_type_list

        Args:
            sm_code: 物流方式编码 (可选)

        Returns:
            dict: {
                "code": 0,
                "message": "success",
                "data": [
                    {"name": "无ASCAN", "value": 1},
                    {"name": "拦截/改派", "value": 2}
                ]
            }
        """
        payload = {}
        if sm_code:
            payload["sm_code"] = sm_code

        return await self._post("/assistant/logistic_ticket_type_list", data=payload)

    async def logistic_ticket_detail(
        self,
        io_code: str,
    ) -> dict[str, Any]:
        """
        获取查件单详情

        API文档: https://oms.goodcang.net/public_open/assistant/logistic_ticket_detail

        Args:
            io_code: 查件单号 (必填)

        Returns:
            dict: {
                "code": 0,
                "message": "success",
                "data": {
                    "base_info": {...},
                    "order_info": {...},
                    "recheck_info": null,
                    "appeal_info": null,
                    "log_info": {...}
                }
            }
        """
        payload = {
            "io_code": io_code,
        }

        return await self._post("/assistant/logistic_ticket_detail", data=payload)


goodcang_assistant = GoodCangAssistant()
