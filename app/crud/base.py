

from typing import Any, Generic, List, Optional, Type, TypeVar

from pydantic import BaseModel

from sqlalchemy import delete, func, select
from sqlalchemy.ext.asyncio import AsyncSession


ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get(self, db: AsyncSession, id: int) -> Optional[ModelType]:
        result = await db.execute(select(self.model).where(self.model.id == id))
        return result.scalar_one_or_none()
    
    async def get_multi(
            self,
            db: AsyncSession,
            *,
            skip: int = 0,
            limit: int = 20,
            filters: Optional[List[Any]] = None
    ) -> List[ModelType]:
        query = select(self.model)
        if filters:
            for f in filters:
                query = query.where(f)
        query = query.offset(skip).limit(limit)
        result = await db.execute(query)
        return list(result.scalars().all())
    
    async def count(
            self,
            db: AsyncSession,
            *,
            filters: Optional[List[Any]] = None
    ) -> int:
        query = select(func.count()).select_from(self.model)
        if filters:
            for f in filters:
                query = query.where(f)
        result = await db.execute(query)
        return result.scalar() or 0
    
    async def create(self, db: AsyncSession, *, obj_in: CreateSchemaType) -> ModelType:
        """创建记录"""
        obj_data = obj_in.model_dump(exclude_unset=True)
        db_obj = self.model(**obj_data)
        db.add(db_obj)
        await db.flush()
        await db.refresh(db_obj)
        return db_obj

    async def update(
        self,
        db: AsyncSession,
        *,
        db_obj: ModelType,
        obj_in: UpdateSchemaType
    ) -> ModelType:
        """更新记录"""
        obj_data = obj_in.model_dump(exclude_unset=True)
        for field, value in obj_data.items():
            setattr(db_obj, field, value)
        await db.flush()
        await db.refresh(db_obj)
        return db_obj

    async def delete(self, db: AsyncSession, *, id: int) -> bool:
        """删除记录"""
        result = await db.execute(
            delete(self.model).where(self.model.id == id)
        )
        return result.rowcount > 0
                