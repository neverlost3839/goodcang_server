from typing import Any, Optional, List
from app.client.base import GoodCangBase


class GoodCangProduct(GoodCangBase):
    """GoodCang 商品 API 客户端"""

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
            "reference_no": reference_no,
            "cat_lang": cat_lang,
            "cat_id_level2": cat_id_level2,
            "product_name_cn": product_name_cn,
            "product_name_en": product_name_en,
            "product_link": product_link,
            "branded": branded,
            "product_brand": product_brand,
            "product_model": product_model,
            "product_weight": product_weight,
            "product_length": product_length,
            "product_width": product_width,
            "product_height": product_height,
            "contain_battery": contain_battery,
            "type_of_goods": type_of_goods,
            "unit": unit,
            "image_link": image_link,
            "verify": verify,
            "product_declared_name_cn": product_declared_name_cn,
            "product_declared_name": product_declared_name,
            "product_material": product_material,
            "product_function": product_function,
            "export_country": export_country,
            "import_country": import_country,
            "certificate_url_list": certificate_url_list,
            "thirdparty_sku_mapping": thirdparty_sku_mapping,
            "sn_info": sn_info,
            "sku_wrapper_type": sku_wrapper_type,
            "return_auth": return_auth,
            "return_replacement_sku": return_replacement_sku,
            "batch_management_enabled": batch_management_enabled,
            "batch_info": batch_info,
            "battery_info": battery_info,
            "remark": remark,
        }

        return await self._post("/public_open/product/add_product", data=payload)


goodcang_product = GoodCangProduct()
