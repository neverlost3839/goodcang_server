from typing import Any, Optional, List
from app.client.base import GoodCangBase


class GoodCangFinance(GoodCangBase):
    """GoodCang 财务 API 客户端"""

    async def get_wh_inventory_storage(
        self,
        page: int,
        page_size: int,
        wis_code: Optional[str] = None,
        ow_id_charge: Optional[str] = None,
        dateFrom: Optional[str] = None,
        dateTo: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        获取仓租信息 (V1版本)

        API文档: https://oms.goodcang.net/public_open/finance/get_wh_inventory_storage

        Args:
            page: 查询页数 (必填, 默认1)
            page_size: 每页显示数量 (必填, 最大100)
            wis_code: 单号 (可选)
            ow_id_charge: 仓库代码 (可选)
            dateFrom: 开始时间 (可选, 格式: Y-m-d H:i:s)
            dateTo: 结束时间 (可选, 格式: Y-m-d H:i:s)

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "count": "1",
                "data": [...]
            }
        """
        payload = {
            "page": page,
            "pageSize": page_size,
        }
        if wis_code:
            payload["wis_code"] = wis_code
        if ow_id_charge:
            payload["ow_id_charge"] = ow_id_charge
        if dateFrom:
            payload["dateFrom"] = dateFrom
        if dateTo:
            payload["dateTo"] = dateTo

        return await self._post("/finance/get_wh_inventory_storage", data=payload)

    async def get_wh_inventory_storage_detail(
        self,
        wis_code: str,
    ) -> dict[str, Any]:
        """
        获取仓租明细 (V1版本)

        API文档: https://oms.goodcang.net/public_open/finance/get_wh_inventory_storage_detail

        Args:
            wis_code: 仓租单号 (必填)

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "data": [...],
                "count": 6
            }
        """
        payload = {
            "wis_code": wis_code,
        }

        return await self._post(
            "/finance/get_wh_inventory_storage_detail", data=payload
        )

    async def cost_flow_list(
        self,
        page: int,
        page_size: int,
        happen_start_time: str,
        happen_end_time: str,
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
    ) -> dict[str, Any]:
        """
        获取费用流水 (V2版本)

        API文档: https://oms.goodcang.net/public_open/finance/cost_flow_list

        Args:
            page: 当前分页 (必填)
            page_size: 分页数量 (必填, 最大200)
            happen_start_time: 发生开始时间 (必填, 格式: YYYY-MM-DD HH:MM:SS, 最大365天跨度)
            happen_end_time: 发生结束时间 (必填, 格式: YYYY-MM-DD HH:MM:SS)
            flow_type: 流水类型 (可选)
                "0": 入款
                "1": 扣款
                "2": 冻结
                "3": 解冻
            number_type: 单号类型 (可选, 需与order_number成对提交)
                "order_number": 单号
                "reference_number": 参考号
            order_number: 单号值 (可选)
            account_code: 账户编号 (可选)
            business_type: 业务类型 (可选)
                "0": 海外仓储
                "1": 中转代发
            types_of_fee: 费用类型 (可选)
            currency_code: 币种 (可选)
            charge_type: 出账状态 (可选)
                "0": 未出账
                "1": 已出账
                "2": 出账中
            next_page_token: 下一页token (可选, 超过5000条时必填)
            prev_page_token: 上一页token (可选, 超过5000条时必填)

        Returns:
            dict: {
                "code": 0,
                "message": "success",
                "data": {
                    "list": [...],
                    "next_page_token": "",
                    "prev_page_token": "",
                    "total": 999
                }
            }
        """
        payload = {
            "page": page,
            "page_size": page_size,
            "happen_start_time": happen_start_time,
            "happen_end_time": happen_end_time,
        }
        if flow_type:
            payload["flow_type"] = flow_type
        if number_type:
            payload["number_type"] = number_type
        if order_number:
            payload["order_number"] = order_number
        if account_code:
            payload["account_code"] = account_code
        if business_type is not None:
            payload["business_type"] = business_type
        if types_of_fee:
            payload["types_of_fee"] = types_of_fee
        if currency_code:
            payload["currency_code"] = currency_code
        if charge_type is not None:
            payload["charge_type"] = charge_type
        if next_page_token:
            payload["next_page_token"] = next_page_token
        if prev_page_token:
            payload["prev_page_token"] = prev_page_token

        return await self._post("/finance/cost_flow_list", data=payload)

    async def top_up_record(
        self,
        code_field: str,
        page: int,
        page_size: int,
        begin_add_time: Optional[str] = None,
        end_add_time: Optional[str] = None,
        code_value: Optional[str] = None,
        transaction_type: Optional[int] = None,
        transaction_gd_status: Optional[int] = None,
        bank_name: Optional[str] = None,
        account_code: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        获取充值明细 (V2版本)

        API文档: https://oms.goodcang.net/public_open/finance/top_up_record

        Args:
            code_field: 单号类型 (必填)
                "reference_number": 银行流水号
                "order_number": 充值单号
            page: 分页页码 (必填)
            page_size: 分页数量 (必填, 最大200)
            begin_add_time: 充值开始日期 (可选, 格式: YYYY-MM-DD HH:MM:SS, 186天跨度)
            end_add_time: 充值结束日期 (可选, 格式: YYYY-MM-DD HH:MM:SS)
            code_value: 字段值 (可选)
            transaction_type: 充值交易类型 (可选)
                0: 余额转汇（转入）
                1: 余额转汇（转出）
                2: 银行转账
                3: Payoneer
                4: 自动转汇（转入）
                5: 自动转汇（转出）
                6: 原件返利
                7: 退件返利
                8: 现金支付
                9: 主体余额转移（转入）
                10: 主体余额转移（转出）
                11: 调增充值
                12: 调减充值
            transaction_gd_status: 交易状态 (可选)
                0: 待处理
                1: 已到账
                2: 已废弃
                3: 草稿
                4: 审核异常
                5: 驳回
            bank_name: 付款银行名称 (可选)
            account_code: 账户编码 (可选)

        Returns:
            dict: {
                "code": 0,
                "message": "success",
                "data": {
                    "list": [...],
                    "total": 12132
                }
            }
        """
        payload = {
            "code_field": code_field,
            "page": page,
            "page_size": page_size,
        }
        if begin_add_time:
            payload["begin_add_time"] = begin_add_time
        if end_add_time:
            payload["end_add_time"] = end_add_time
        if code_value:
            payload["code_value"] = code_value
        if transaction_type is not None:
            payload["transaction_type"] = transaction_type
        if transaction_gd_status is not None:
            payload["transaction_gd_status"] = transaction_gd_status
        if bank_name:
            payload["bank_name"] = bank_name
        if account_code:
            payload["account_code"] = account_code

        return await self._post("/finance/top_up_record", data=payload)


goodcang_finance = GoodCangFinance()
