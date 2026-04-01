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
                "data": [
                    {
                        "asro_code": "RG296-170914-0013",
                        "order_code": "G296-170914-0002",
                        "reference_no": "fdzxcv4654132",
                        "asro_status": "4",
                        "cass_type": "1",
                        "asro_add_time": "2017-09-14 17:07:41",
                        "asro_audit_time": "2017-09-14 17:08:08",
                        "asro_putaway_time": "0000-00-00 00:00:00",
                        "warehouse_code": "USEA",
                        "sm_type": "0",
                        "collect_warehouse_code": "",
                        "service_type": 1,
                        "is_transit": 2,
                        "tracking_no": "787722279346",
                        "asro_reason": "xzv",
                        "product_detail": [
                            {
                                "product_barcode": "G296-SKU8945421522",
                                "product_sku": "SKU8945421522",
                                "sellable_qty": 1,
                                "unsellable_qty": 0,
                                "destruction_qty": 0,
                                "sellable_detail": [],
                                "unsellable_detail": [],
                                "destruction_detail": [],
                                "return_auth": 1,
                                "return_replacement_sku": None,
                                "photo_list": None
                            }
                        ],
                        "sm_code": "TJDX-XF",
                        "as_length": "0.00",
                        "as_width": "0.00",
                        "as_height": "0.00",
                        "charge_weight": "0.000",
                        "asro_note": "我要留言",
                        "fee_details": {
                            "shipping_fee": 8.307,
                            "fuel_surcharge": 4.886,
                            "other_fee": 0.489,
                            "currency_code": "USD"
                        }
                    }
                ]
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


goodcang_return_order = GoodCangReturnOrder()
