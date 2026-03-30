from datetime import datetime
from typing import Optional

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.client.product import goodcang_product
from app.config.settings import settings
from app.crud import crud_product
from app.models.product import Product
from app.schemas.common import PaginatedData
from app.schemas.product import ProductCreate, ProductOut, ProductUpdate


class ProductService:
    async def list(
        self,
        db: AsyncSession,
        *,
        page: int = 1,
        page_size: int = 20,
        product_sku: Optional[str] = None,
        product_name_cn: Optional[str] = None,
        product_name_en: Optional[str] = None,
        product_brand: Optional[str] = None,
        verify: Optional[int] = None,
        updated_at_from: Optional[datetime] = None,
        updated_at_to: Optional[datetime] = None,
    ) -> PaginatedData[ProductOut]:
        skip = (page - 1) * page_size
        filters = []

        if product_sku:
            filters.append(Product.product_sku.ilike(f"%{product_sku}%"))
        if product_name_cn:
            filters.append(Product.product_name_cn.ilike(f"%{product_name_cn}%"))
        if product_name_en:
            filters.append(Product.product_name_en.ilike(f"%{product_name_en}%"))
        if product_brand:
            filters.append(Product.product_brand.ilike(f"%{product_brand}%"))
        if verify is not None:
            filters.append(Product.verify == verify)
        if updated_at_from:
            filters.append(Product.updated_at >= updated_at_from)
        if updated_at_to:
            filters.append(Product.updated_at <= updated_at_to)

        items = await crud_product.get_multi(
            db, skip=skip, limit=page_size, filters=filters if filters else None
        )
        total = await crud_product.count(db, filters=filters if filters else None)

        return PaginatedData(
            items=[ProductOut.model_validate(item) for item in items],
            total=total,
            page=page,
            page_size=page_size,
            total_pages=(total + page_size - 1) // page_size,
        )

    async def get(self, db: AsyncSession, *, id: int) -> ProductOut:
        db_obj = await crud_product.get(db, id=id)
        if not db_obj:
            raise HTTPException(status_code=404, detail=f"商品ID {id} 不存在")
        return ProductOut.model_validate(db_obj)

    async def create(self, db: AsyncSession, *, obj_in: ProductCreate) -> ProductOut:
        if not settings.GOODCANG_API_KEY:
            raise HTTPException(
                status_code=400, detail="APIKey不能为空，请配置GOODCANG_API_KEY"
            )
        if not settings.GOODCANG_CLIENT_CODE:
            raise HTTPException(
                status_code=400, detail="ClientCode不能为空，请配置GOODCANG_CLIENT_CODE"
            )

        try:
            goodcang_response = await goodcang_product.add_product(
                product_sku=obj_in.product_sku,
                product_name_cn=obj_in.product_name_cn,
                product_name_en=obj_in.product_name_en,
                product_weight=obj_in.product_weight,
                product_length=obj_in.product_length,
                product_width=obj_in.product_width,
                product_height=obj_in.product_height,
                contain_battery=obj_in.contain_battery,
                type_of_goods=obj_in.type_of_goods,
                cat_id_level2=obj_in.cat_id_level2,
                product_declared_name_cn=obj_in.product_name_cn,
                product_material="无",
                branded=obj_in.branded,
                product_link=obj_in.product_link,
                export_country=[{"country_code": "CN", "country_name": "中国"}],
                import_country=[{"country_code": "US", "country_name": "美国"}],
                reference_no=obj_in.reference_no,
                product_brand=obj_in.product_brand,
                product_model=obj_in.product_model,
                product_declared_name=obj_in.product_name_en,
                product_function=None,
                cat_lang=obj_in.cat_lang,
                verify=obj_in.verify,
                unit=obj_in.unit,
                image_link=None,
                certificate_url_list=None,
                thirdparty_sku_mapping=[obj_in.thirdparty_sku_mapping]
                if obj_in.thirdparty_sku_mapping
                else None,
                sn_info=None,
                sku_wrapper_type=obj_in.sku_wrapper_type,
                return_auth=obj_in.return_auth,
                return_replacement_sku=obj_in.return_replacement_sku,
                batch_management_enabled=0,
                batch_info=None,
                battery_info=None,
                remark=None,
            )
        except Exception as e:
            raise HTTPException(status_code=502, detail=f"调用第三方API失败: {str(e)}")

        if goodcang_response.get("ask") != "Success":
            error_message = goodcang_response.get("message", "第三方API调用失败")
            raise HTTPException(status_code=400, detail=error_message)

        db_obj = await crud_product.create(db=db, obj_in=obj_in)
        return ProductOut.model_validate(db_obj)

    async def update(
        self, db: AsyncSession, *, id: int, obj_in: ProductUpdate
    ) -> ProductOut:
        db_obj = await crud_product.get(db, id=id)
        if not db_obj:
            raise HTTPException(status_code=404, detail=f"商品ID {id} 不存在")
        updated_obj = await crud_product.update(db=db, db_obj=db_obj, obj_in=obj_in)
        return ProductOut.model_validate(updated_obj)

    async def delete(self, db: AsyncSession, *, id: int) -> bool:
        db_obj = await crud_product.get(db, id=id)
        if not db_obj:
            raise HTTPException(status_code=404, detail=f"商品ID {id} 不存在")
        await crud_product.delete(db, id=id)
        return True


product_service = ProductService()
