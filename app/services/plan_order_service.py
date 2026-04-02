from typing import Any, List, Optional

from app.client.plan_order import goodcang_plan_order


class PlanOrderService:
    async def list(
        self,
        page: int = 1,
        page_size: int = 20,
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
    ) -> Any:
        """获取计划单列表"""
        return await goodcang_plan_order.list(
            page=page,
            page_size=page_size,
            order_status=order_status,
            code_type=code_type,
            code_value_list=code_value_list,
            warehouse_code=warehouse_code,
            is_change_label=is_change_label,
            label_replacement_option=label_replacement_option,
            is_stick_label=is_stick_label,
            dest_warehouse_type=dest_warehouse_type,
            time_type=time_type,
            start_time=start_time,
            end_time=end_time,
        )

    async def box_list(
        self,
        page: int = 1,
        page_size: int = 20,
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
    ) -> Any:
        """获取装箱列表"""
        return await goodcang_plan_order.box_list(
            page=page,
            page_size=page_size,
            box_status=box_status,
            code_type=code_type,
            code_value_list=code_value_list,
            warehouse_code=warehouse_code,
            is_change_label=is_change_label,
            label_replacement_option=label_replacement_option,
            is_stick_label=is_stick_label,
            time_type=time_type,
            start_time=start_time,
            end_time=end_time,
        )


plan_order_service = PlanOrderService()
