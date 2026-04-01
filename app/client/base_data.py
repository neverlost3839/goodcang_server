from typing import Any, Optional, List
from app.client.base import GoodCangBase


class GoodCangBaseData(GoodCangBase):
    """GoodCang 基础数据 API 客户端"""

    async def get_country(self) -> dict[str, Any]:
        """
        获取国家/地区列表

        API文档: https://oms.goodcang.net/public_open/base_data/get_country

        Returns:
            dict: {
                "ask": "Success",
                "message": "success",
                "data": [
                    {
                        "country_code": "CN",
                        "country_name": "中国",
                        "country_name_en": "China"
                    }
                ]
            }
        """
        return await self._post("/base_data/get_country", data={})

    async def get_warehouse(self) -> dict[str, Any]:
        """
        获取系统仓库

        API文档: https://oms.goodcang.net/public_open/base_data/get_warehouse

        Returns:
            dict: {
                "ask": "Success",
                "message": "success",
                "data": [
                    {
                        "warehouse_code": "FRVI",
                        "warehouse_name": "法国仓库",
                        "country_code": "FR",
                        "wp_list": [
                            {
                                "code": "FRVI_1",
                                "name": "法国物理仓1",
                                "address": {
                                    "state": "Ile-de-France",
                                    "city": "Paris",
                                    "postcode": "75001",
                                    "contacter": "John Doe",
                                    "phone": "+33-123456789",
                                    "street_address1": "123 Rue de Rivoli",
                                    "street_address2": "",
                                    "street_number": "123"
                                }
                            }
                        ]
                    }
                ]
            }
        """
        return await self._post("/base_data/get_warehouse", data={})

    async def get_shipping_method(
        self,
        warehouse_code: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        获取物流产品

        API文档: https://oms.goodcang.net/public_open/base_data/get_shipping_method

        Args:
            warehouse_code: 尾程仓库代码 (可选, 最大32字符)

        Returns:
            dict: {
                "ask": "Success",
                "message": "success",
                "data": [
                    {
                        "code": "TRACKED_NS",
                        "name": "Tracked_NS挂号(包裹)",
                        "name_en": "",
                        "warehouse_code": "UK",
                        "type": "0",
                        "is_signature": 0,
                        "is_specify_arrival_time": 0
                    }
                ]
            }
        """
        payload = {}
        if warehouse_code:
            payload["warehouseCode"] = warehouse_code

        return await self._post("/base_data/get_shipping_method", data=payload)

    async def get_account_list(self) -> dict[str, Any]:
        """
        获取公司账户

        API文档: https://oms.goodcang.net/public_open/base_data/get_account_list

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "data": {
                    "customer_code": "G296",
                    "account_list": [
                        {
                            "firm_name": "企业名称1",
                            "firm_status": 3,
                            "server_firm_name": "ETARGET LIMITED",
                            "business_type_list": [0, 1],
                            "account_code": "AC123456",
                            "balance_list": [
                                {"currency_code": "AUD", "amount": "0"},
                                {"currency_code": "USD", "amount": "-21058639.794"}
                            ]
                        }
                    ]
                }
            }
        """
        return await self._post("/base_data/get_account_list", data={})

    async def cost_type_list(
        self,
        sign_business_type: int,
    ) -> dict[str, Any]:
        """
        获取费用类型

        API文档: https://oms.goodcang.net/public_open/base_data/cost_type_list

        Args:
            sign_business_type: 业务类型 (必填)
                0: 海外仓储
                1: 中转代发

        Returns:
            dict: {
                "code": 0,
                "message": "success",
                "data": [
                    {
                        "cost_name": "备用费用-2",
                        "cost_code": "SCF2"
                    }
                ]
            }
        """
        payload = {
            "sign_business_type": sign_business_type,
        }

        return await self._post("/base_data/cost_type_list", data=payload)

    async def fuel_rate_list(
        self,
        logistic_type: int,
        sm_code: str,
        begin_time: str,
        end_time: str,
        page: int = 1,
        page_size: int = 10,
    ) -> dict[str, Any]:
        """
        获取燃油费率

        API文档: https://oms.goodcang.net/public_open/base_data/fuel_rate_list

        Args:
            logistic_type: 物流产品 (必填)
                0: 发货物流
                1: 退货物流
            sm_code: 物流产品编码 (必填)
            begin_time: 起始生效时间 (必填, 格式: YYYY-MM-DD HH:MM:SS)
            end_time: 结束生效时间 (必填, 格式: YYYY-MM-DD HH:MM:SS)
                注意: 31天跨度, 时间区间参数必须成对出现
            page: 分页页码 (可选, 默认1)
            page_size: 分页数量 (可选, 默认10, 最大200)

        Returns:
            dict: {
                "code": 0,
                "message": "success",
                "data": {
                    "total": 1231,
                    "list": [
                        {
                            "fls_rate": "",
                            "fls_begin_time": "",
                            "fls_end_time": "",
                            "sm_name": "",
                            "sm_code": ""
                        }
                    ]
                }
            }
        """
        payload = {
            "logistic_type": logistic_type,
            "sm_code": sm_code,
            "begin_time": begin_time,
            "end_time": end_time,
            "page": page,
            "page_size": page_size,
        }

        return await self._post("/base_data/fuel_rate_list", data=payload)


goodcang_base_data = GoodCangBaseData()
