from typing import Any, List, Optional

from app.client.inbound_order import goodcang_inbound_order


class InboundOrderService:
    async def get_vat_list(
        self,
        page: int = 1,
        page_size: int = 10,
    ) -> Any:
        """获取进出口商列表"""
        return await goodcang_inbound_order.get_vat_list(
            page=page,
            page_size=page_size,
        )

    async def get_smcode_twc_to_warehouse(self) -> Any:
        """获取物流产品与目的仓中转仓"""
        return await goodcang_inbound_order.get_smcode_twc_to_warehouse()

    async def get_grn_list(
        self,
        page: int = 1,
        page_size: int = 10,
        receiving_code_arr: Optional[List[str]] = None,
        create_date_from: Optional[str] = None,
        create_date_to: Optional[str] = None,
        modify_date_from: Optional[str] = None,
        modify_date_to: Optional[str] = None,
        is_rollover: Optional[int] = None,
    ) -> Any:
        """获取入库单列表"""
        return await goodcang_inbound_order.get_grn_list(
            page=page,
            page_size=page_size,
            receiving_code_arr=receiving_code_arr,
            create_date_from=create_date_from,
            create_date_to=create_date_to,
            modify_date_from=modify_date_from,
            modify_date_to=modify_date_to,
            is_rollover=is_rollover,
        )

    async def get_grn_detail(
        self,
        receiving_code: str,
    ) -> Any:
        """获取入库单明细"""
        return await goodcang_inbound_order.get_grn_detail(
            receiving_code=receiving_code,
        )

    async def get_batch(
        self,
        receiving_code: str,
    ) -> Any:
        """获取上架批次"""
        return await goodcang_inbound_order.get_batch(
            receiving_code=receiving_code,
        )

    async def get_receipt_batch(
        self,
        receiving_code: str,
    ) -> Any:
        """获取收货批次"""
        return await goodcang_inbound_order.get_receipt_batch(
            receiving_code=receiving_code,
        )

    async def cars_model(self) -> Any:
        """获取车型"""
        return await goodcang_inbound_order.cars_model()

    async def get_clearance_document(
        self,
        receiving_list: List[str],
    ) -> Any:
        """获取清关文件上传状态"""
        return await goodcang_inbound_order.get_clearance_document(
            receiving_list=receiving_list,
        )


inbound_order_service = InboundOrderService()
