from typing import Any, Optional, List
from app.client.base import GoodCangBase


class GoodCangProduct(GoodCangBase):
    """GoodCang 商品 API 客户端"""

    # 获取商品列表
    async def get_product_sku_list(
            self,
            pageSize: str,
            page: str,
            product_sku: Optional[str] = None,
            product_update_time_from: Optional[str] = None,
            product_update_time_to: Optional[str] = None,
    ):
        
        payload = {
            pageSize: str,
            page: str,
        }

        if product_sku:
            payload["product_sku"] = product_sku
        if product_update_time_from:
            payload["product_update_time_from"] = product_update_time_from
        if product_update_time_to:
            payload["product_update_time_to"] = product_update_time_to
        
        return await self._post("/product/get_product_sku_list", data=payload)

    # 新建商品
    async def add_product(
        self,
        product_sku: str,
        product_name_cn: str,
        product_name_en: str,
        product_weight: float,
        product_length: float,
        product_width: float,
        product_height: float,
        contain_battery: int,
        type_of_goods: int,
        cat_id_level2: int,
        product_declared_name_cn: str,
        product_material: str,
        branded: int,
        product_link: str,
        export_country: List[dict],
        import_country: List[dict],
        reference_no: Optional[str] = None,
        product_brand: Optional[str] = None,
        product_model: Optional[str] = None,
        product_declared_name: Optional[str] = None,
        product_function: Optional[str] = None,
        cat_lang: Optional[str] = "zh",
        verify: Optional[int] = 0,
        unit: Optional[str] = "PCS",
        image_link: Optional[List[str]] = None,
        certificate_url_list: Optional[List[str]] = None,
        thirdparty_sku_mapping: Optional[List[str]] = None,
        sn_info: Optional[dict] = None,
        sku_wrapper_type: Optional[int] = None,
        return_auth: Optional[int] = 1,
        return_replacement_sku: Optional[str] = None,
        batch_management_enabled: Optional[int] = 0,
        batch_info: Optional[dict] = None,
        battery_info: Optional[dict] = None,
        remark: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        新建商品

        API文档: https://oms.goodcang.net/public_open/product/add_product

        Args:
            product_sku: SKU (必填, 最大24字符)
            reference_no: 客户参考代码 (可选, 最大50字符)
            cat_lang: 品类语言，默认zh
            cat_id_level2: 二级品类ID (必填)
            product_name_cn: 商品中文名称 (必填, 最大255字符)
            product_name_en: 商品英文名称 (必填, 最大255字符)
            product_link: 商品链接 (必填, 最大1000字符)
            branded: 是否品牌 (必填, 0:否 1:是)
            product_brand: 商品品牌 (branded=1时必填)
            product_model: 商品型号 (可选)
            product_weight: 重量KG (必填)
            product_length: 长CM (必填)
            product_width: 宽CM (必填)
            product_height: 高CM (必填)
            contain_battery: 货物属性 (必填, 0:普货 1:含电池 2:纯电池 3:纺织品 4:易碎品 6:超标纯电池 7:超标含电池)
            type_of_goods: 包裹类型 (必填, 0:包裹 1:信封)
            unit: 单位 (可选, 默认PCS)
            image_link: 商品图片链接数组 (可选, 最多10张)
            verify: 是否自动提交审核 (可选, 0:草稿 1:审核, 默认0)
            product_declared_name_cn: 中文申报品名 (必填)
            product_declared_name: 英文申报品名 (可选)
            product_material: 材质 (必填)
            product_function: 用途 (可选)
            export_country: 出口国信息 (必填)
            import_country: 进口国信息 (必填)
            certificate_url_list: 证书URL数组 (可选, 最多30个)
            thirdparty_sku_mapping: 第三方映射编码数组 (可选, 最多1个)
            sn_info: 序列号采集信息 (可选)
            sku_wrapper_type: 包装属性 (可选, 1:预包装 2:销售包装 3:原包彩盒)
            return_auth: 退件授权 (可选, 0:未授权 1:已授权, 默认1)
            return_replacement_sku: 换标编码 (可选)
            batch_management_enabled: 是否批次管理 (可选, 0:否 1:是)
            batch_info: 批次信息 (可选)
            battery_info: 电池信息 (可选, contain_battery为6或7时必填)
            remark: 备注 (可选, 最大500字符)

        Returns:
            dict: {
                "ask": "Success",
                "message": "Success",
                "product_sku": "EA140512114042",
                "product_barcode": "G562-EA140512114640"
            }
        """
        payload = {
            "product_sku": product_sku,
            "cat_lang": cat_lang,
            "cat_id_level2": cat_id_level2,
            "product_name_cn": product_name_cn,
            "product_name_en": product_name_en,
            "product_link": product_link,
            "branded": branded,
            "product_weight": product_weight,
            "product_length": product_length,
            "product_width": product_width,
            "product_height": product_height,
            "contain_battery": contain_battery,
            "type_of_goods": type_of_goods,
            "product_declared_name_cn": product_declared_name_cn,
            "product_material": product_material,
            "export_country": export_country,
            "import_country": import_country,
        }
        if reference_no:
            payload["reference_no"] = reference_no
        if product_brand:
            payload["product_brand"] = product_brand
        if product_model:
            payload["product_model"] = product_model
        if product_declared_name:
            payload["product_declared_name"] = product_declared_name
        if product_function:
            payload["product_function"] = product_function
        if verify:
            payload["verify"] = verify
        if unit and unit != "PCS":
            payload["unit"] = unit
        if image_link:
            payload["image_link"] = image_link
        if certificate_url_list:
            payload["certificate_url_list"] = certificate_url_list
        if thirdparty_sku_mapping:
            payload["thirdparty_sku_mapping"] = thirdparty_sku_mapping
        if sn_info:
            payload["sn_info"] = sn_info
        if sku_wrapper_type:
            payload["sku_wrapper_type"] = sku_wrapper_type
        if return_auth != 1:
            payload["return_auth"] = return_auth
        if return_replacement_sku:
            payload["return_replacement_sku"] = return_replacement_sku
        if batch_management_enabled:
            payload["batch_management_enabled"] = batch_management_enabled
        if batch_info:
            payload["batch_info"] = batch_info
        if battery_info:
            payload["battery_info"] = battery_info
        if remark:
            payload["remark"] = remark

        return await self._post("/product/add_product", data=payload)
    
    # 获取系统品类
    async def get_category(self):
        return await self._post("/product/get_category")
    
    # 获取建议中文申报品名
    async def get_declare_commodity_name_list(self):
        return await self._post("/product/get_declare_commodity_name_list")
    
    # 获取建议材质
    async def get_material_list(self):
        return await self._post("/product/get_material_list")
    
    # 获取序列号列表
    async def get_serial_number_list(
        self,
        status: Optional[int] = 1,
        code_type: Optional[int] = 1,
        code_value: Optional[str] = None,
        time_type: Optional[int] = 1,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        ):
        
        payload = {}

        if status:
            payload["status"] = status
        if code_type:
            payload["code_type"] = code_type
        if code_value:
            payload["code_value"] = code_value
        if time_type:
            payload["time_type"] = time_type
        if start_time:
            payload["start_time"] = start_time
        if end_time:
            payload["end_time"] = end_time
        
        return await self._post("product/serial_number_list", data = payload)



goodcang_product = GoodCangProduct()
