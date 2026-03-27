
from datetime import datetime
from typing import Optional

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import crud_product
from app.schemas.common import PaginatedData
from app.schemas.product import ProductCreate, ProductOut, ProductUpdate


class ProductService:
    """商品服务层 - 处理商品相关业务逻辑"""

    async def list(
        self,
        db: AsyncSession,
        *,
        page: int = 1,
        page_size: int = 20,
        sku: Optional[str] = None,
        name: Optional[str] = None,
        category: Optional[str] = None,
        brand: Optional[str] = None,
        status: Optional[str] = None,
        updated_at_from: Optional[datetime] = None,
        updated_at_to: Optional[datetime] = None,
    ) -> PaginatedData[ProductOut]:
        """
        获取商品列表（分页、筛选）

        Args:
            db: 数据库会话
            page: 当前页码
            page_size: 每页条数
            sku: SKU筛选
            name: 商品名称筛选（模糊匹配）
            category: 分类筛选
            brand: 品牌筛选
            status: 状态筛选
            updated_at_from: 更新时间起始
            updated_at_to: 更新时间截止

        Returns:
            PaginatedData[ProductOut]: 分页商品数据
        """
        skip = (page - 1) * page_size
        filters = []

        if sku:
            filters.append(crud_product.model.sku.ilike(f"%{sku}%"))
        if name:
            filters.append(crud_product.model.name.ilike(f"%{name}%"))
        if category:
            filters.append(crud_product.model.category.ilike(f"%{category}%"))
        if brand:
            filters.append(crud_product.model.brand.ilike(f"%{brand}%"))
        if status:
            filters.append(crud_product.model.status == status)
        if updated_at_from:
            filters.append(crud_product.model.updated_at >= updated_at_from)
        if updated_at_to:
            filters.append(crud_product.model.updated_at <= updated_at_to)

        items = await crud_product.get_multi(db, skip=skip, limit=page_size, filters=filters if filters else None)
        total = await crud_product.count(db, filters=filters if filters else None)

        return PaginatedData(
            items=[ProductOut.model_validate(item) for item in items],
            total=total,
            page=page,
            page_size=page_size,
            total_pages=(total + page_size - 1) // page_size
        )

    async def get(
        self,
        db: AsyncSession,
        *,
        id: int
    ) -> ProductOut:
        """
        根据ID获取商品详情

        Args:
            db: 数据库会话
            id: 商品ID

        Returns:
            ProductOut: 商品详情

        Raises:
            HTTPException: 商品不存在时抛出404
        """
        db_obj = await crud_product.get(db, id=id)
        if not db_obj:
            raise HTTPException(status_code=404, detail=f"商品ID {id} 不存在")
        return ProductOut.model_validate(db_obj)

    async def create(
        self,
        db: AsyncSession,
        *,
        obj_in: ProductCreate
    ) -> ProductOut:
        """
        创建商品

        Args:
            db: 数据库会话
            obj_in: 商品创建参数

        Returns:
            ProductOut: 创建的商品
        """
        db_obj = await crud_product.create(db=db, obj_in=obj_in)
        return ProductOut.model_validate(db_obj)

    async def update(
        self,
        db: AsyncSession,
        *,
        id: int,
        obj_in: ProductUpdate
    ) -> ProductOut:
        """
        更新商品

        Args:
            db: 数据库会话
            id: 商品ID
            obj_in: 商品更新参数

        Returns:
            ProductOut: 更新后的商品

        Raises:
            HTTPException: 商品不存在时抛出404
        """
        db_obj = await crud_product.get(db, id=id)
        if not db_obj:
            raise HTTPException(status_code=404, detail=f"商品ID {id} 不存在")
        updated_obj = await crud_product.update(db=db, db_obj=db_obj, obj_in=obj_in)
        return ProductOut.model_validate(updated_obj)

    async def delete(
        self,
        db: AsyncSession,
        *,
        id: int
    ) -> bool:
        """
        删除商品

        Args:
            db: 数据库会话
            id: 商品ID

        Returns:
            bool: 是否删除成功

        Raises:
            HTTPException: 商品不存在时抛出404
        """
        db_obj = await crud_product.get(db, id=id)
        if not db_obj:
            raise HTTPException(status_code=404, detail=f"商品ID {id} 不存在")
        await crud_product.delete(db, id=id)
        return True


product_service = ProductService()
