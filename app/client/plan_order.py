from typing import Any, Optional, List
from app.client.base import GoodCangBase


class GoodCangPlanOrder(GoodCangBase):
    """GoodCang 计划单 API 客户端"""

    async def list(
        self,
        page: int,
        page_size: int,
        order_status: Optional[int] = None,
        code_type: Optional[int] = None,
        code_value_list: Optional[List[str]] = None,
        warehouse_code: Optional[str] = None,
        is_change_label: Optional[int] = None,
        label_replacement_option: Optional[int] = None,
        is_stick_label: Optional[int] = None,
        dest_warehouse_type: Optional[int] = None,
        time_type: Optional[int] = None,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        获取计划单列表

        API文档: https://oms.goodcang.net/public_open/plan_order/list

        Args:
            page: 分页页码 (必填)
            page_size: 分页数量 (必填, 最大200)
            order_status: 计划单状态 (可选)
                0: 废弃
                1: 草稿
                2: 异常
                3: 待配货
                4: 已完成
            code_type: 单号类型 (可选)
                1: 计划单号（默认）
                2: 参考号
                3: 商品编码
                4: 箱唛号
            code_value_list: 单号值数组 (可选, 最多100个)
            warehouse_code: 发货仓库 (可选)
            is_change_label: 换标服务 (可选)
                0: 否
                1: 是
            label_replacement_option: 换标要求 (可选)
                1: 外箱
                2: 内箱
            is_stick_label: 贴标服务 (可选)
                0: 否
                1: 是
            dest_warehouse_type: 目的仓类型 (可选)
                1: FBA
                2: 第三方
            time_type: 时间类型 (可选)
                0: 创建时间
                1: 提交时间
                2: 配货时间
            start_time: 起始时间 (可选, 格式: YYYY-MM-DD HH:MM:SS)
            end_time: 截止时间 (可选, 格式: YYYY-MM-DD HH:MM:SS)

        Returns:
            dict: {
                "code": 0,
                "message": "success",
                "data": {
                    "list": [...],
                    "total": 1
                }
            }
        """
        payload = {
            "page": page,
            "page_size": page_size,
        }
        if order_status is not None:
            payload["order_status"] = order_status
        if code_type is not None:
            payload["code_type"] = code_type
        if code_value_list:
            payload["code_value_list"] = code_value_list
        if warehouse_code:
            payload["warehouse_code"] = warehouse_code
        if is_change_label is not None:
            payload["is_change_label"] = is_change_label
        if label_replacement_option is not None:
            payload["label_replacement_option"] = label_replacement_option
        if is_stick_label is not None:
            payload["is_stick_label"] = is_stick_label
        if dest_warehouse_type is not None:
            payload["dest_warehouse_type"] = dest_warehouse_type
        if time_type is not None:
            payload["time_type"] = time_type
        if start_time:
            payload["start_time"] = start_time
        if end_time:
            payload["end_time"] = end_time

        return await self._post("/plan_order/list", data=payload)

    async def box_list(
        self,
        page: int,
        page_size: int,
        box_status: Optional[int] = None,
        code_type: Optional[int] = None,
        code_value_list: Optional[List[str]] = None,
        warehouse_code: Optional[str] = None,
        is_change_label: Optional[int] = None,
        label_replacement_option: Optional[int] = None,
        is_stick_label: Optional[int] = None,
        time_type: Optional[int] = None,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        获取装箱列表

        API文档: https://oms.goodcang.net/public_open/plan_order/box_list

        Args:
            page: 分页页码 (必填)
            page_size: 分页数量 (必填, 最大200)
            box_status: 箱状态 (可选)
                0: 可用
                1: 已用
            code_type: 单号类型 (可选)
                1: 箱唛号（默认）
                2: 计划单号
                3: 关联单号
                4: 商品编码
            code_value_list: 单号值数组 (可选, 最多100个)
            warehouse_code: 发货仓库 (可选)
            is_change_label: 换标服务 (可选)
                0: 否
                1: 是
            label_replacement_option: 换标要求 (可选)
                1: 外箱
                2: 内箱
            is_stick_label: 贴标服务 (可选)
                0: 否
                1: 是
            time_type: 时间类型 (可选)
                1: 装箱时间
            start_time: 起始时间 (可选, 格式: YYYY-MM-DD HH:MM:SS)
            end_time: 截止时间 (可选, 格式: YYYY-MM-DD HH:MM:SS)

        Returns:
            dict: {
                "code": 0,
                "message": "success",
                "data": {
                    "list": [...],
                    "total": 1
                }
            }
        """
        payload = {
            "page": page,
            "page_size": page_size,
        }
        if box_status is not None:
            payload["box_status"] = box_status
        if code_type is not None:
            payload["code_type"] = code_type
        if code_value_list:
            payload["code_value_list"] = code_value_list
        if warehouse_code:
            payload["warehouse_code"] = warehouse_code
        if is_change_label is not None:
            payload["is_change_label"] = is_change_label
        if label_replacement_option is not None:
            payload["label_replacement_option"] = label_replacement_option
        if is_stick_label is not None:
            payload["is_stick_label"] = is_stick_label
        if time_type is not None:
            payload["time_type"] = time_type
        if start_time:
            payload["start_time"] = start_time
        if end_time:
            payload["end_time"] = end_time

        return await self._post("/plan_order/box_list", data=payload)


goodcang_plan_order = GoodCangPlanOrder()
