from typing import Any, Optional

from app.client.finance import goodcang_finance


class FinanceService:
    async def get_wh_inventory_storage(
        self,
        page: int = 1,
        page_size: int = 10,
        wis_code: Optional[str] = None,
        ow_id_charge: Optional[str] = None,
        dateFrom: Optional[str] = None,
        dateTo: Optional[str] = None,
    ) -> Any:
        """获取仓租信息 (V1版本)"""
        return await goodcang_finance.get_wh_inventory_storage(
            page=page,
            page_size=page_size,
            wis_code=wis_code,
            ow_id_charge=ow_id_charge,
            dateFrom=dateFrom,
            dateTo=dateTo,
        )

    async def get_wh_inventory_storage_detail(
        self,
        wis_code: str,
    ) -> Any:
        """获取仓租明细 (V1版本)"""
        return await goodcang_finance.get_wh_inventory_storage_detail(
            wis_code=wis_code,
        )

    async def cost_flow_list(
        self,
        page: int = 1,
        page_size: int = 20,
        happen_start_time: str = "",
        happen_end_time: str = "",
        flow_type: Optional[str] = None,
        number_type: Optional[str] = None,
        order_number: Optional[str] = None,
        account_code: Optional[str] = None,
        business_type: Optional[int] = None,
        types_of_fee: Optional[str] = None,
        currency_code: Optional[str] = None,
        charge_type: Optional[int] = None,
        next_page_token: Optional[str] = None,
        prev_page_token: Optional[str] = None,
    ) -> Any:
        """获取费用流水 (V2版本)"""
        return await goodcang_finance.cost_flow_list(
            page=page,
            page_size=page_size,
            happen_start_time=happen_start_time,
            happen_end_time=happen_end_time,
            flow_type=flow_type,
            number_type=number_type,
            order_number=order_number,
            account_code=account_code,
            business_type=business_type,
            types_of_fee=types_of_fee,
            currency_code=currency_code,
            charge_type=charge_type,
            next_page_token=next_page_token,
            prev_page_token=prev_page_token,
        )

    async def top_up_record(
        self,
        code_field: str,
        page: int = 1,
        page_size: int = 20,
        begin_add_time: Optional[str] = None,
        end_add_time: Optional[str] = None,
        code_value: Optional[str] = None,
        transaction_type: Optional[int] = None,
        transaction_gd_status: Optional[int] = None,
        bank_name: Optional[str] = None,
        account_code: Optional[str] = None,
    ) -> Any:
        """获取充值明细 (V2版本)"""
        return await goodcang_finance.top_up_record(
            code_field=code_field,
            page=page,
            page_size=page_size,
            begin_add_time=begin_add_time,
            end_add_time=end_add_time,
            code_value=code_value,
            transaction_type=transaction_type,
            transaction_gd_status=transaction_gd_status,
            bank_name=bank_name,
            account_code=account_code,
        )


finance_service = FinanceService()
