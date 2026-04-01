from typing import Any, Optional, List
from app.client.base import GoodCangBase


class GoodCangOrder(GoodCangBase):
    """GoodCang 订单 API 客户端"""

    async def create_order(
        self,
        shipping_method: str,
        warehouse_code: str,
        country_code: str,
        province: str,
        city: str,
        address1: str,
        zipcode: str,
        name: str,
        items: List[dict],
        reference_no: Optional[str] = None,
        platform: Optional[str] = "OTHER",
        company: Optional[str] = None,
        address2: Optional[str] = None,
        address3: Optional[str] = None,
        doorplate: Optional[str] = None,
        last_name: Optional[str] = None,
        cell_phone: Optional[str] = None,
        phone: Optional[str] = None,
        email: Optional[str] = None,
        order_desc: Optional[str] = None,
        customer_package_requirement: Optional[int] = None,
        verify: Optional[int] = 0,
        is_shipping_method_not_allow_update: Optional[int] = 1,
        is_signature: Optional[int] = 0,
        is_insurance: Optional[int] = 0,
        insurance_value: Optional[float] = None,
        fba_shipment_id: Optional[str] = None,
        fba_shipment_id_create_time: Optional[str] = None,
        property_label: Optional[str] = None,
        business_type: Optional[int] = 0,
        is_change_label: Optional[int] = 0,
        age_detection: Optional[int] = 0,
        is_liftgate: Optional[int] = 0,
        payment_time: Optional[str] = None,
        attachment_ids: Optional[List[int]] = None,
        estimated_arrival_date: Optional[str] = None,
        estimated_arrival_time: Optional[str] = None,
        sender_info: Optional[dict] = None,
        vat_change_info: Optional[dict] = None,
        is_euro_label: Optional[int] = None,
        vas: Optional[dict] = None,
        is_warehouse_packing: Optional[int] = 0,
        carton_info: Optional[dict] = None,
        truck_info: Optional[dict] = None,
    ) -> dict[str, Any]:
        """
        创建订单

        API文档: https://oms.goodcang.net/public_open/order/create_order

        Args:
            reference_no: 订单参考号 (可选, 最大50字符)
            platform: 平台 (可选, 默认OTHER)
            shipping_method: 物流产品代码 (必填)
            warehouse_code: 配送仓库代码 (必填)
            country_code: 收件人国家/地区 (必填, 2字符)
            province: 省 (必填, 最大20字符)
            city: 城市 (必填, 最大32字符)
            company: 公司名称 (可选, 最大50字符)
            address1: 地址1 (必填, 最大50字符)
            address2: 地址2 (可选, 最大50字符)
            address3: 地址3 (可选)
            zipcode: 邮编 (必填, 最大20字符)
            doorplate: 门牌号 (可选, 最大20字符)
            name: 收件人名 (必填, 最大48字符)
            last_name: 收件人姓 (可选, 最大48字符)
            cell_phone: 分机号 (可选)
            phone: 收件人联系方式 (可选, 最大20字符)
            email: 收件人邮箱 (可选, 最大100字符)
            order_desc: 订单备注 (可选, 最大500字符)
            customer_package_requirement: 包材要求 (可选, 1:纸箱 2:快递袋 3:气泡袋 4:环保袋)
            verify: 是否直接审核 (可选, 0:草稿 1:审核, 默认0)
            is_shipping_method_not_allow_update: 派送方式是否允许修改 (可选, 默认1不允许)
            is_signature: 签名服务 (可选, 0:不选择 1:选择, 默认0)
            is_insurance: 保险服务 (可选, 0:不需要 1:需要, 默认0)
            insurance_value: 保额 (可选, 最多3位小数)
            fba_shipment_id: FBA Shipment ID (可选, 12位数字+字母)
            fba_shipment_id_create_time: FBA Shipment ID创建时间 (可选)
            property_label: 平台模式 (可选, 最大50字符)
            business_type: 配送方式 (可选, 0:仓配一体 1:仓配分离)
            is_change_label: FBA换标服务 (可选, 0:不换标 1:换标, 默认0)
            age_detection: 年龄检测 (可选, 0:不检测 16:16岁 18:18岁)
            is_liftgate: LiftGate服务 (可选, 0:否 1:是)
            payment_time: 付款时间 (可选, 格式YYYY-MM-DD HH:MM:SS)
            attachment_ids: 订单附件id数组 (可选)
            estimated_arrival_date: 预计到货日期 (可选, 格式YYYY-MM-DD)
            estimated_arrival_time: 到货时间段 (可选)
            sender_info: 发件人信息 (可选, 日本仓库适用)
            vat_change_info: 欧盟税改资料 (可选)
            is_euro_label: 是否贴标 (可选, 1:是 0:否)
            vas: 增值服务选项 (可选)
            is_warehouse_packing: 是否仓库装箱商品 (可选, 0:否 1:是)
            carton_info: FBA转仓单信息 (可选, is_warehouse_packing=1时必填)
            truck_info: 卡派渠道物流信息 (可选, FBA卡派必填)
            items: 订单明细 (必填, 数组)

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "order_code": "000-160617-0001"
            }
        """
        payload = {
            "reference_no": reference_no,
            "platform": platform,
            "shipping_method": shipping_method,
            "warehouse_code": warehouse_code,
            "country_code": country_code,
            "province": province,
            "city": city,
            "address1": address1,
            "zipcode": zipcode,
            "name": name,
            "items": items,
        }
        if reference_no:
            payload["reference_no"] = reference_no
        if platform and platform != "OTHER":
            payload["platform"] = platform
        if company:
            payload["company"] = company
        if address2:
            payload["address2"] = address2
        if address3:
            payload["address3"] = address3
        if doorplate:
            payload["doorplate"] = doorplate
        if last_name:
            payload["last_name"] = last_name
        if cell_phone:
            payload["cell_phone"] = cell_phone
        if phone:
            payload["phone"] = phone
        if email:
            payload["email"] = email
        if order_desc:
            payload["order_desc"] = order_desc
        if customer_package_requirement:
            payload["customer_package_requirement"] = customer_package_requirement
        if verify:
            payload["verify"] = verify
        if is_shipping_method_not_allow_update != 1:
            payload["is_shipping_method_not_allow_update"] = (
                is_shipping_method_not_allow_update
            )
        if is_signature:
            payload["is_signature"] = is_signature
        if is_insurance:
            payload["is_insurance"] = is_insurance
        if insurance_value:
            payload["insurance_value"] = insurance_value
        if fba_shipment_id:
            payload["fba_shipment_id"] = fba_shipment_id
        if fba_shipment_id_create_time:
            payload["fba_shipment_id_create_time"] = fba_shipment_id_create_time
        if property_label:
            payload["property_label"] = property_label
        if business_type:
            payload["business_type"] = business_type
        if is_change_label:
            payload["is_change_label"] = is_change_label
        if age_detection:
            payload["age_detection"] = age_detection
        if is_liftgate:
            payload["is_liftgate"] = is_liftgate
        if payment_time:
            payload["payment_time"] = payment_time
        if attachment_ids:
            payload["attachment_ids"] = attachment_ids
        if estimated_arrival_date:
            payload["estimated_arrival_date"] = estimated_arrival_date
        if estimated_arrival_time:
            payload["estimated_arrival_time"] = estimated_arrival_time
        if sender_info:
            payload["sender_info"] = sender_info
        if vat_change_info:
            payload["vat_change_info"] = vat_change_info
        if is_euro_label:
            payload["is_euro_label"] = is_euro_label
        if vas:
            payload["vas"] = vas
        if is_warehouse_packing:
            payload["is_warehouse_packing"] = is_warehouse_packing
        if carton_info:
            payload["carton_info"] = carton_info
        if truck_info:
            payload["truck_info"] = truck_info

        return await self._post("/order/create_order", data=payload)


goodcang_order = GoodCangOrder()
