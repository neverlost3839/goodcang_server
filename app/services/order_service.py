from datetime import datetime
from typing import Optional

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.crud_order import crud_order
from app.models.order import Order
from app.schemas.common import PaginatedData
from app.schemas.order import OrderCreate, OrderOut, OrderUpdate


class OrderService:
    """订单服务层 - 处理订单相关业务逻辑"""

    async def list(
        self,
        db: AsyncSession,
        *,
        page: int = 1,
        page_size: int = 20,
        code: Optional[str] = None,
        product_id: Optional[int] = None,
        username: Optional[str] = None,
        status: Optional[str] = None,
        updated_at_from: Optional[datetime] = None,
        updated_at_to: Optional[datetime] = None,
    ) -> PaginatedData[OrderOut]:
        """
        获取订单列表（分页、筛选）
        
        Args:
            db: 数据库会话
            page: 当前页码
            page_size: 每页条数
            code: 订单编号筛选
            product_id: 商品ID筛选
            username: 收件用户名筛选
            status: 订单状态筛选
            created_at_from: 创建时间起始
            created_at_to: 创建时间截止
            updated_at_from: 更新时间起始
            updated_at_to: 更新时间截止
            
        Returns:
            PaginatedData[OrderOut]: 分页订单数据
        """
        # 构建筛选条件
        filters = []
        
        if code:
            filters.append(Order.code.contains(code))
        if product_id:
            filters.append(Order.product_id.contains(product_id))
        if username:
            filters.append(Order.username.contains(username))
        if status:
            filters.append(Order.status == status)
        if updated_at_from:
            filters.append(Order.updated_at >= updated_at_from)
        if updated_at_to:
            filters.append(Order.updated_at <= updated_at_to)
        
        # 计算分页偏移量
        skip = (page - 1) * page_size
        
        # 获取订单列表
        items = await crud_order.get_multi(
            db,
            skip=skip,
            limit=page_size,
            filters=filters if filters else None
        )
        
        # 获取总数
        total = await crud_order.count(
            db,
            filters=filters if filters else None
        )
        
        # 计算总页数
        total_pages = (total + page_size - 1) // page_size
        
        # 组装分页响应
        return PaginatedData(
            items=[OrderOut.model_validate(item) for item in items],
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages
        )

    async def get(
        self,
        db: AsyncSession,
        *,
        id: int
    ) -> OrderOut:
        """
        根据ID获取订单详情
        
        Args:
            db: 数据库会话
            id: 订单ID
            
        Returns:
            OrderOut: 订单详情
            
        Raises:
            HTTPException: 订单不存在时抛出404
        """
        db_obj = await crud_order.get(db, id=id)
        if not db_obj:
            raise HTTPException(status_code=404, detail=f"订单ID {id} 不存在")
        return OrderOut.model_validate(db_obj)

    async def create(
        self,
        db: AsyncSession,
        *,
        obj_in: OrderCreate
    ) -> OrderOut:
        """
        创建订单
        
        Args:
            db: 数据库会话
            obj_in: 订单创建参数
            
        Returns:
            OrderOut: 创建的订单
        """
        db_obj = await crud_order.create(db=db, obj_in=obj_in)
        return OrderOut.model_validate(db_obj)

    async def update(
        self,
        db: AsyncSession,
        *,
        id: int,
        obj_in: OrderUpdate
    ) -> OrderOut:
        """
        更新订单
        
        Args:
            db: 数据库会话
            id: 订单ID
            obj_in: 订单更新参数
            
        Returns:
            OrderOut: 更新后的订单
            
        Raises:
            HTTPException: 订单不存在时抛出404
        """
        db_obj = await crud_order.get(db, id=id)
        if not db_obj:
            raise HTTPException(status_code=404, detail=f"订单ID {id} 不存在")
        updated_obj = await crud_order.update(db=db, db_obj=db_obj, obj_in=obj_in)
        return OrderOut.model_validate(updated_obj)

    async def delete(
        self,
        db: AsyncSession,
        *,
        id: int
    ) -> bool:
        """
        删除订单
        
        Args:
            db: 数据库会话
            id: 订单ID
            
        Returns:
            bool: 是否删除成功
            
        Raises:
            HTTPException: 订单不存在时抛出404
        """
        db_obj = await crud_order.get(db, id=id)
        if not db_obj:
            raise HTTPException(status_code=404, detail=f"订单ID {id} 不存在")
        await crud_order.delete(db, id=id)
        return True


# 实例化，供api层调用
order_service = OrderService()
