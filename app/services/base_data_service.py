from typing import Any, Optional

from app.client.base_data import goodcang_base_data


class BaseDataService:
    async def get_country(self) -> Any:
        """获取国家/地区列表"""
        return await goodcang_base_data.get_country()

    async def get_warehouse(self) -> Any:
        """获取系统仓库"""
        return await goodcang_base_data.get_warehouse()

    async def get_shipping_method(
        self,
        warehouse_code: Optional[str] = None,
    ) -> Any:
        """获取物流产品"""
        return await goodcang_base_data.get_shipping_method(
            warehouse_code=warehouse_code
        )

    async def get_account_list(self) -> Any:
        """获取公司账户"""
        return await goodcang_base_data.get_account_list()

    async def cost_type_list(
        self,
        sign_business_type: int,
    ) -> Any:
        """获取费用类型"""
        return await goodcang_base_data.cost_type_list(
            sign_business_type=sign_business_type
        )

    async def fuel_rate_list(
        self,
        logistic_type: int,
        sm_code: str,
        begin_time: str,
        end_time: str,
        page: int = 1,
        page_size: int = 10,
    ) -> Any:
        """获取燃油费率"""
        return await goodcang_base_data.fuel_rate_list(
            logistic_type=logistic_type,
            sm_code=sm_code,
            begin_time=begin_time,
            end_time=end_time,
            page=page,
            page_size=page_size,
        )


base_data_service = BaseDataService()
