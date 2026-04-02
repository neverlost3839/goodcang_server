from typing import Any, Optional

from app.client.return_order import goodcang_return_order


class ReturnOrderService:
    async def search(
        self,
        reference_no: Optional[str] = None,
        asro_codes: Optional[str] = None,
    ) -> Any:
        """退货单查询"""
        return await goodcang_return_order.search(
            reference_no=reference_no,
            asro_codes=asro_codes,
        )

    async def get_list(
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
    ) -> Any:
        """退货单列表"""
        return await goodcang_return_order.list(
            current_page=current_page,
            page_size=page_size,
            start_time=start_time,
            end_time=end_time,
            start_update_time=start_update_time,
            end_update_time=end_update_time,
            asro_status=asro_status,
            cass_type=cass_type,
            asro_codes=asro_codes,
        )

    async def unauthorized_list(
        self,
        current_page: int = 1,
        page_size: int = 10,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
    ) -> Any:
        """未预报退件列表"""
        return await goodcang_return_order.unauthorized_list(
            current_page=current_page,
            page_size=page_size,
            start_time=start_time,
            end_time=end_time,
        )

    async def claim_order_list(
        self,
        current_page: int = 1,
        page_size: int = 10,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        claim_status: Optional[int] = None,
    ) -> Any:
        """索赔单列表"""
        return await goodcang_return_order.claim_order_list(
            current_page=current_page,
            page_size=page_size,
            start_time=start_time,
            end_time=end_time,
            claim_status=claim_status,
        )

    async def get_service_config(self) -> Any:
        """获取退件服务配置"""
        return await goodcang_return_order.get_service_config()

    async def claim_order_details(
        self,
        claim_code: str,
    ) -> Any:
        """索赔单详情"""
        return await goodcang_return_order.claim_order_details(
            claim_code=claim_code,
        )


return_order_service = ReturnOrderService()
