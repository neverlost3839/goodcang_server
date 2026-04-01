from typing import Any, Optional, List
from datetime import datetime
from app.client.base import GoodCangBase


class GoodCangInboundOrder(GoodCangBase):
    """GoodCang 入库单 API 客户端"""

    async def create_grn(
        self,
        transit_type: int,
        receiving_shipping_type: int,
        warehouse_code: str,
        items: List[dict],
        reference_no: Optional[str] = None,
        sm_code: Optional[str] = None,
        transit_warehouse_code: Optional[str] = None,
        customs_type: Optional[int] = None,
        collecting_service: Optional[int] = None,
        collecting_time: Optional[datetime] = None,
        value_add_service: Optional[str] = None,
        clearance_service: Optional[int] = None,
        import_company: Optional[int] = None,
        export_company: Optional[int] = None,
        car_model_code: Optional[str] = None,
        tracking_number: Optional[str] = None,
        eta_date: Optional[datetime] = None,
        receiving_desc: Optional[str] = None,
        verify: int = 0,
        weight: Optional[float] = None,
        volume: Optional[float] = None,
        wp_code: Optional[str] = None,
        is_delay: int = 0,
        is_rollover: int = 0,
        shiper_address: Optional[dict] = None,
        collecting_address: Optional[List[dict]] = None,
        customers_send_info: Optional[dict] = None,
    ) -> dict[str, Any]:
        """
        创建入库单

        API文档: https://oms.goodcang.net/public_open/inbound_order/create_grn

        Args:
            transit_type: 入库单类型 (必填, 0-自发入库单, 3-中转入库单, 5-FBA入库单)
            receiving_shipping_type: 运输方式 (必填, 0-空运, 1-海运散货, 2-快递, 3-铁运整柜, 4-海运整柜, 5-铁运散货)
            warehouse_code: 海外仓仓库编码 (必填, 最大32字符)
            items: 入库单明细 (必填, 数组)
            reference_no: 参考号 (可选, 最大50字符)
            sm_code: 物流产品 (中转特有, 最大255字符)
            transit_warehouse_code: 中转仓仓库编码 (中转特有, 最大255字符)
            customs_type: 报关方式 (中转特有, 0-EDI报关 1-委托报关 2-报关自理)
            collecting_service: 揽收服务 (中转特有, 0-自送货物 1-上门提货)
            collecting_time: 揽收时间 (中转特有)
            value_add_service: 增值服务 (中转特有, world_ease-woordease服务, origin_crt-产地证, fumigation-熏蒸)
            clearance_service: 是否自有税号清关 (中转特有, 0-否 1-是)
            import_company: 进口商编码 (中转特有)
            export_company: 出口商编码 (中转特有)
            car_model_code: 车型 (中转特有, 最大255字符)
            tracking_number: 跟踪号/海柜号 (可选, 最大35字符)
            eta_date: 预计到达时间 (自发/FBA必填, 格式YYYY-MM-DD)
            receiving_desc: 备注 (可选, 最大255字符)
            verify: 是否审核 (可选, 0-新建不审核 1-新建并审核, 默认0)
            weight: 重量(kg) (可选, 0.01-999999.99)
            volume: 体积(立方米) (可选, 0.01-99999.99)
            wp_code: 物理仓仓库代码 (可选)
            is_delay: 是否递延 (可选, 0-否 1-是, 默认0)
            is_rollover: 是否仓库装箱商品 (可选, 0-否 1-是, 默认0)
            shiper_address: 发件人地址 (自发入库单)
            collecting_address: 揽收地址 (中转特有,上门揽收时必填)
            customers_send_info: 客户自送信息 (中转特有,自送货物时必填)

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "data": {
                    "receiving_code": "RVG296-190703-0001"
                }
            }
        """
        payload = {
            "transit_type": transit_type,
            "receiving_shipping_type": receiving_shipping_type,
            "warehouse_code": warehouse_code,
            "items": items,
            "reference_no": reference_no,
            "sm_code": sm_code,
            "transit_warehouse_code": transit_warehouse_code,
            "customs_type": customs_type,
            "collecting_service": collecting_service,
            "collecting_time": collecting_time.strftime("%Y-%m-%d %H:%M:%S")
            if collecting_time
            else None,
            "value_add_service": value_add_service,
            "clearance_service": clearance_service,
            "import_company": import_company,
            "export_company": export_company,
            "car_model_code": car_model_code,
            "tracking_number": tracking_number,
            "eta_date": eta_date.strftime("%Y-%m-%d") if eta_date else None,
            "receiving_desc": receiving_desc,
            "verify": verify,
            "weight": weight,
            "volume": volume,
            "wp_code": wp_code,
            "is_delay": is_delay,
            "is_rollover": is_rollover,
            "shiper_address": shiper_address,
            "collecting_address": collecting_address,
            "customers_send_info": customers_send_info,
        }

        return await self._post("/inbound_order/create_grn", data=payload)


goodcang_inbound_order = GoodCangInboundOrder()
