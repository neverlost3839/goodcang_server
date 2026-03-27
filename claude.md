Claude 辅助开发规范文档（商品管理系统）

一、文档概述

本文档用于规范 Claude 在本商品管理系统中的辅助开发行为，核心遵循 api层→services层→crud层 的开发流程，明确 models 层数据映射、schemas 层请求/响应/异常参数定义的规范，确保生成的代码符合项目架构、可直接复用，减少开发成本与后期维护难度。

本项目技术栈为 FastAPI（异步）+ SQLAlchemy（异步ORM）+ PostgreSQL，所有辅助开发内容需严格对齐此技术栈及以下架构规范，重点围绕核心 product 商品表展开。

二、核心架构规范（必遵循）

开发流程严格遵循：api层（接口暴露）→ services层（业务逻辑）→ crud层（数据操作），配套 models层（数据映射） 与 schemas层（参数定义），各层职责清晰、禁止跨层调用，确保代码解耦、可维护。

2.1 各层核心职责

- api层：对外暴露接口，接收前端请求、返回响应，仅做参数校验（依赖schemas层）和业务逻辑调用（依赖services层），不直接操作数据库。

- services层：封装核心业务逻辑，接收api层传递的参数，调用crud层完成数据操作，处理业务规则、异常流转，不直接操作数据库会话。

- crud层：专注于数据库操作，提供增删改查异步方法，接收services层的调用，仅负责数据读写，不包含任何业务逻辑。

- models层：完成数据库表与Python类的映射，严格对应PostgreSQL表结构，定义字段、约束、关联关系，是数据操作的基础。

- schemas层：基于Pydantic定义请求参数、响应参数、异常参数，实现参数校验、数据格式化，确保接口输入输出规范。

2.2 项目基础信息（供Claude参考）

2.2.1 核心技术栈

- 后端框架：FastAPI（异步模式，需兼容异步语法）

- ORM工具：SQLAlchemy（异步模式，避免同步操作）

- 数据库：PostgreSQL（严格适配其语法、字段类型）

- 迁移工具：Alembic（用于models层与数据库表结构同步）

- 代码规范：PEP 8 标准，统一使用下划线命名法（snake_case），禁止驼峰命名

2.2.2 核心数据库表（product表）

create table product
(
    id          bigserial
        primary key,
    name        varchar(255)   not null,
    sku         varchar(100)   not null
        unique,
    description text,
    price       numeric(10, 2) not null,
    category    varchar(100),
    brand       varchar(100),
    status      varchar(20) default 'active'::character varying
        constraint products_status_check
            check ((status)::text = ANY
                   ((ARRAY ['active'::character varying, 'inactive'::character varying, 'out_of_stock'::character varying])::text[])),
    created_at  timestamp   default CURRENT_TIMESTAMP,
    updated_at  timestamp   default CURRENT_TIMESTAMP
);

alter table product
    owner to postgres;

create index idx_category
    on product (category);

create index idx_status
    on product (status);

create trigger trigger_update_products_updated_at
    before update
    on product
    for each row
execute procedure update_modified_column();

2.2.3 核心目录结构

app/
├── api/                 # api层：接口暴露
│   └── v1/
│       ├── endpoints/  # 各模块接口（如product.py、category.py）
│       └── api.py      # 路由注册，统一管理所有接口
├── services/           # services层：业务逻辑封装
│   └── product_service.py  # 商品相关业务逻辑
├── crud/               # crud层：数据库操作
│   ├── base.py         # 基础CRUD模板（复用方法）
│   └── crud_product.py # 商品相关CRUD操作
├── models/             # models层：数据映射
│   └── product.py      # 商品表模型，对应数据库product表
├── schemas/            # schemas层：参数定义
│   └── product.py      # 商品相关请求、响应、异常参数
├── db/                 # 数据库配置
│   ├── session.py      # 数据库会话（异步）
│   └── base_class.py   # 模型基类
└── main.py             # 项目入口，启动FastAPI服务

三、各层开发规范（Claude生成代码必遵循）

3.1 models层（数据映射规范）

核心职责：实现数据库表与Python类的一一映射，严格对齐PostgreSQL表结构，不包含任何业务逻辑。

开发规范：

1. 所有模型类必须继承自 app.db.base_class.Base，确保统一的模型基础。

2. 通过 __tablename__ 指定表名，必须与数据库表名完全一致（如商品表对应 __tablename__ = "product"）。

3. 字段定义需与数据库表完全匹配：字段名、数据类型、约束（非空、唯一、默认值、检查约束）一致。
        

  - 示例：price 字段对应数据库 numeric(10,2)，模型中定义为 Column(Numeric(10, 2), nullable=False)；

  - status 字段需添加检查约束，匹配数据库中的 check 条件（仅允许 active、inactive、out_of_stock）。

4. 字段需添加清晰注释（comment），与数据库字段注释一致，便于维护。

5. 禁止在models层添加业务逻辑、数据校验逻辑，仅做数据映射。

示例（product模型）：

from sqlalchemy import Column, BigInteger, String, Text, Numeric, DateTime, CheckConstraint
from app.db.base_class import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "product"  # 与数据库表名一致

    id = Column(BigInteger, primary_key=True, index=True, comment="商品ID")
    name = Column(String(255), nullable=False, comment="商品名称")
    sku = Column(String(100), nullable=False, unique=True, comment="商品SKU（唯一）")
    description = Column(Text, nullable=True, comment="商品描述")
    price = Column(Numeric(10, 2), nullable=False, comment="商品价格")
    category = Column(String(100), nullable=True, comment="商品分类")
    brand = Column(String(100), nullable=True, comment="商品品牌")
    status = Column(
        String(20),
        default="active",
        nullable=False,
        comment="商品状态（active：正常，inactive：下架，out_of_stock：缺货）",
        CheckConstraint("status IN ('active', 'inactive', 'out_of_stock')", name="products_status_check")
    )
    created_at = Column(DateTime, default=datetime.utcnow, comment="创建时间")
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, comment="更新时间")

3.2 schemas层（请求/响应/异常参数规范）

核心职责：基于Pydantic定义接口的请求参数、响应参数、异常参数，实现参数校验、数据格式化，供api层使用。

开发规范：

1. 按功能拆分模型：请求参数（Create/Update）、响应参数（Out）、异常参数（Error），命名规范统一。
        

  - 请求参数：XXXCreate（创建）、XXXUpdate（更新），继承自BaseModel；

  - 响应参数：XXXOut（返回数据），继承自BaseModel，需包含数据库表核心字段，开启 orm_mode = True（兼容SQLAlchemy模型）；

  - 异常参数：统一定义异常响应格式，包含code（错误码）、detail（错误描述）。

2. 参数校验需严格：设置字段类型、必填项、长度限制、格式限制，与models层字段对应。
        

  - 示例：name 字段为必填项，定义为 name: str；sku 字段长度限制，定义为 sku: str = Field(max_length=100)。

3. 响应参数需包含核心字段，避免返回冗余数据，敏感字段需隐藏（如需）。

4. 异常参数需统一格式，便于前端统一处理，示例：{"code": 404, "detail": "商品不存在"}。

5. 禁止在schemas层添加业务逻辑，仅做参数定义与校验。

示例（product schemas）：

from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, Any
from datetime import datetime

# 基础参数（公共字段）
class ProductBase(BaseModel):
    name: str = Field(..., max_length=255, description="商品名称（必填）")
    sku: str = Field(..., max_length=100, description="商品SKU（必填，唯一）")
    description: Optional[str] = Field(None, description="商品描述")
    price: float = Field(..., gt=0, description="商品价格（必填，大于0）")
    category: Optional[str] = Field(None, max_length=100, description="商品分类")
    brand: Optional[str] = Field(None, max_length=100, description="商品品牌")
    status: Optional[str] = Field(
        "active",
        description="商品状态",
        pattern=r"^active|inactive|out_of_stock$"
    )

# 请求参数（创建商品）
class ProductCreate(ProductBase):
    pass  # 继承基础字段，无需额外添加

# 请求参数（更新商品）
class ProductUpdate(BaseModel):
    # 更新时所有字段可选，仅传递需要修改的字段
    name: Optional[str] = Field(None, max_length=255, description="商品名称")
    sku: Optional[str] = Field(None, max_length=100, description="商品SKU（唯一）")
    description: Optional[str] = Field(None, description="商品描述")
    price: Optional[float] = Field(None, gt=0, description="商品价格（大于0）")
    category: Optional[str] = Field(None, max_length=100, description="商品分类")
    brand: Optional[str] = Field(None, max_length=100, description="商品品牌")
    status: Optional[str] = Field(None, pattern=r"^active|inactive|out_of_stock$", description="商品状态")

# 响应参数（商品详情/列表）
class ProductOut(ProductBase):
    id: int = Field(..., description="商品ID")
    created_at: datetime = Field(..., description="创建时间")
    updated_at: datetime = Field(..., description="更新时间")

    class Config:
        orm_mode = True  # 允许直接将SQLAlchemy模型转换为响应参数

# 异常参数（统一格式）
class ProductError(BaseModel):
    code: int = Field(..., description="错误码")
    detail: str = Field(..., description="错误描述")

# 分页响应参数（商品列表专用）
class ProductPageOut(BaseModel):
    items: list[ProductOut] = Field(..., description="商品列表")
    total: int = Field(..., description="商品总数")
    page: int = Field(..., description="当前页码")
    page_size: int = Field(..., description="每页条数")
    total_pages: int = Field(..., description="总页数")

3.3 crud层（数据操作规范）

核心职责：封装数据库增删改查异步操作，供services层调用，不包含任何业务逻辑，仅专注于数据读写。

开发规范：

1. 继承基础CRUD模板（crud/base.py），复用通用方法（如get、get_multi、create等），避免重复代码。

2. 命名规范：
        

  - 类名：CRUDXXX（如CRUDProduct）；

  - 实例化对象：crud_xxx（如crud_product）；

  - 方法名：create（创建）、get（查询单个）、get_multi（查询多个）、update（更新）、remove（删除），统一命名。

3. 所有方法均为异步方法（添加async），使用SQLAlchemy异步语法：
        

  - 查询：使用 await db.execute(select(...))，通过 scalar_one_or_none()（单个结果）、scalars().all()（多个结果）获取数据；

  - 新增/更新/删除：需调用 await db.commit() 提交事务，新增/更新后需调用 await db.refresh(db_obj) 刷新数据。

4. 方法参数：接收数据库会话（db: AsyncSession）、模型对象/参数，返回值为SQLAlchemy模型对象（供services层转换为响应参数）。

5. 禁止在crud层添加业务逻辑（如状态判断、数据过滤等），仅做纯数据操作；如需过滤，通过参数传递筛选条件。

示例（crud_product）：

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate

class CRUDProduct:
    # 创建商品
    async def create(self, db: AsyncSession, obj_in: ProductCreate) -> Product:
        db_obj = Product(
            name=obj_in.name,
            sku=obj_in.sku,
            description=obj_in.description,
            price=obj_in.price,
            category=obj_in.category,
            brand=obj_in.brand,
            status=obj_in.status
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    # 根据ID查询单个商品
    async def get(self, db: AsyncSession, id: int) -> Optional[Product]:
        result = await db.execute(select(Product).where(Product.id == id))
        return result.scalar_one_or_none()

    # 查询多个商品（分页）
    async def get_multi(
        self,
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100,
        category: Optional[str] = None,
        status: Optional[str] = None
    ) -> List[Product]:
        query = select(Product)
        # 筛选条件（由services层传递，crud层仅执行）
        if category:
            query = query.where(Product.category == category)
        if status:
            query = query.where(Product.status == status)
        result = await db.execute(query.offset(skip).limit(limit))
        return result.scalars().all()

    # 更新商品
    async def update(
        self,
        db: AsyncSession,
        db_obj: Product,
        obj_in: ProductUpdate
    ) -> Product:
        # 仅更新传递的字段（exclude_unset=True：排除未传递的字段）
        update_data = obj_in.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    # 删除商品
    async def remove(self, db: AsyncSession, id: int) -> Product:
        db_obj = await self.get(db, id)
        await db.delete(db_obj)
        await db.commit()
        return db_obj

# 实例化，供services层调用
crud_product = CRUDProduct()

3.4 services层（业务逻辑规范）

核心职责：封装商品相关业务逻辑，作为api层与crud层的中间层，接收api层参数，调用crud层操作数据，处理业务规则、异常判断。

开发规范：

1. 命名规范：
        

  - 类名：XXXService（如ProductService）；

  - 实例化对象：xxx_service（如product_service）；

  - 方法名：与api层接口对应（如create、get、list、update、delete），清晰体现业务功能。

2. 所有方法均为异步方法（添加async），参数与api层接口参数对齐，调用crud层方法完成数据操作。

3. 核心职责：
        

  - 业务规则校验（如：判断SKU是否重复、商品状态是否合法）；

  - 异常处理（如：商品不存在、SKU重复，抛出对应异常，供api层捕获）；

  - 数据组装（如：将crud层返回的模型对象，转换为schemas层的响应参数）；

  - 分页逻辑处理（如：计算总页数、处理skip和limit参数）。

4. 禁止直接操作数据库会话（db），所有数据操作必须通过crud层完成；禁止跨层调用（如直接调用api层、models层）。

5. 异常需明确，抛出FastAPI的HTTPException，便于api层统一返回异常响应。

示例（product_service）：

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, List, Dict
from app.crud.crud_product import crud_product
from app.schemas.product import ProductCreate, ProductUpdate, ProductOut, ProductPageOut

class ProductService:
    # 创建商品（业务逻辑：校验SKU唯一性）
    async def create(
        self,
        db: AsyncSession,
        *,
        obj_in: ProductCreate
    ) -> ProductOut:
        # 业务校验：SKU是否已存在
        existing_product = await crud_product.get_multi(db, sku=obj_in.sku)
        if existing_product:
            raise HTTPException(status_code=400, detail=f"SKU {obj_in.sku} 已存在，无法重复创建")
        # 调用crud层创建商品
        db_obj = await crud_product.create(db=db, obj_in=obj_in)
        # 转换为响应参数
        return ProductOut.model_validate(db_obj)

    # 根据ID获取商品（业务逻辑：判断商品是否存在）
    async def get(
        self,
        db: AsyncSession,
        *,
        id: int
    ) -> ProductOut:
        db_obj = await crud_product.get(db=db, id=id)
        if not db_obj:
            raise HTTPException(status_code=404, detail=f"商品ID {id} 不存在")
        return ProductOut.model_validate(db_obj)

    # 获取商品列表（业务逻辑：分页、筛选）
    async def list(
        self,
        db: AsyncSession,
        *,
        page: int = 1,
        page_size: int = 20,
        category: Optional[str] = None,
        status: Optional[str] = None
    ) -> ProductPageOut:
        # 分页逻辑：计算skip
        skip = (page - 1) * page_size
        # 调用crud层查询商品列表
        items = await crud_product.get_multi(
            db=db,
            skip=skip,
            limit=page_size,
            category=category,
            status=status
        )
        # 计算总数、总页数
        total = len(items)
        total_pages = (total + page_size - 1) // page_size
        # 组装分页响应
        return ProductPageOut(
            items=[ProductOut.model_validate(item) for item in items],
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages
        )

    # 更新商品（业务逻辑：校验商品存在、SKU唯一性）
    async def update(
        self,
        db: AsyncSession,
        *,
        id: int,
        obj_in: ProductUpdate
    ) -> ProductOut:
        # 校验商品是否存在
        db_obj = await crud_product.get(db=db, id=id)
        if not db_obj:
            raise HTTPException(status_code=404, detail=f"商品ID {id} 不存在")
        # 校验SKU唯一性（若修改SKU）
        if obj_in.sku and obj_in.sku != db_obj.sku:
            existing_product = await crud_product.get_multi(db, sku=obj_in.sku)
            if existing_product:
                raise HTTPException(status_code=400, detail=f"SKU {obj_in.sku} 已存在，无法修改")
        # 调用crud层更新商品
        updated_obj = await crud_product.update(db=db, db_obj=db_obj, obj_in=obj_in)
        return ProductOut.model_validate(updated_obj)

    # 删除商品（业务逻辑：校验商品存在）
    async def delete(
        self,
        db: AsyncSession,
        *,
        id: int
    ) -> ProductOut:
        db_obj = await crud_product.get(db=db, id=id)
        if not db_obj:
            raise HTTPException(status_code=404, detail=f"商品ID {id} 不存在")
        # 调用crud层删除商品
        deleted_obj = await crud_product.remove(db=db, id=id)
        return ProductOut.model_validate(deleted_obj)

# 实例化，供api层调用
product_service = ProductService()

3.5 api层（接口暴露规范）

核心职责：对外暴露HTTP接口，接收前端请求，校验请求参数（依赖schemas层），调用services层业务逻辑，返回响应参数/异常。

开发规范：

1. 使用FastAPI的APIRouter注册路由，前缀、标签与业务模块对应：
        

  - 前缀：/product（商品接口）；

  - 标签：["商品"]（便于Swagger文档分类）。

2. 接口方法与HTTP请求方式对应：

  - 创建商品：POST /product/；

  - 获取商品详情：GET /product/{id}；

  - 获取商品列表：GET /product/；

  - 更新商品：PUT /product/{id}；

  - 删除商品：DELETE /product/{id}。

3. 参数校验：
        

  - 路径参数（如id）：直接定义在路由中，指定类型（如int）；

  - 查询参数（如page、page_size、category）：定义在方法参数中，可设置默认值；

  - 请求体（如创建/更新商品参数）：使用schemas层的请求模型（ProductCreate、ProductUpdate），通过Depends接收。

4. 响应定义：通过response_model指定响应参数（如ProductOut、ProductPageOut），统一响应格式。

5. 异常处理：无需手动捕获services层抛出的HTTPException，FastAPI会自动捕获并返回对应状态码和异常信息。

6. 禁止在api层添加业务逻辑、数据库操作，仅做参数校验和services层调用。

示例（product接口）：

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional

from app.db.session import get_db
from app.schemas.product import ProductCreate, ProductUpdate, ProductOut, ProductPageOut, ProductError
from app.services.product_service import product_service

# 注册路由
router = APIRouter(prefix="/product", tags=["商品"])

# 创建商品接口
@router.post("/", response_model=ProductOut, responses={400: {"model": ProductError}})
async def create_product(
    obj_in: ProductCreate,
    db: AsyncSession = Depends(get_db)
):
    return await product_service.create(db=db, obj_in=obj_in)

# 获取商品详情接口
@router.get("/{id}", response_model=ProductOut, responses={404: {"model": ProductError}})
async def get_product(
    id: int,
    db: AsyncSession = Depends(get_db)
):
    return await product_service.get(db=db, id=id)

# 获取商品列表接口（分页、筛选）
@router.get("/", response_model=ProductPageOut)
async def get_product_list(
    page: int = Query(1, ge=1, description="当前页码，最小为1"),
    page_size: int = Query(20, ge=1, le=100, description="每页条数，1-100之间"),
    category: Optional[str] = Query(None, description="商品分类筛选"),
    status: Optional[str] = Query(None, description="商品状态筛选"),
    db: AsyncSession = Depends(get_db)
):
    return await product_service.list(
        db=db,
        page=page,
        page_size=page_size,
        category=category,
        status=status
    )

# 更新商品接口
@router.put("/{id}", response_model=ProductOut, responses={400: {"model": ProductError}, 404: {"model": ProductError}})
async def update_product(
    id: int,
    obj_in: ProductUpdate,
    db: AsyncSession = Depends(get_db)
):
    return await product_service.update(db=db, id=id, obj_in=obj_in)

# 删除商品接口
@router.delete("/{id}", response_model=ProductOut, responses={404: {"model": ProductError}})
async def delete_product(
    id: int,
    db: AsyncSession = Depends(get_db)
):
    return await product_service.delete(db=db, id=id)

四、Claude 辅助开发注意事项

1. 所有生成的代码必须严格遵循上述各层规范，对齐项目技术栈、目录结构、命名规范，避免出现语法错误、跨层调用。

2. 生成代码时，需结合核心 product 表结构，确保models层、schemas层、crud层字段完全匹配，不遗漏、不冗余。

3. 生成SQL语句时，需适配PostgreSQL语法，避免使用其他数据库特有语法（如MySQL的limit语法、SQL Server的top语法）。

4. 生成异常处理逻辑时，需与schemas层的异常参数格式统一，便于前端统一处理。

5. 生成代码后，需添加清晰注释（类注释、方法注释、字段注释），符合PEP 8规范，提升代码可读性。

6. 若需扩展其他模块（如category分类），需遵循相同的架构规范，保持代码风格统一。

五、补充说明

1. 数据库迁移：models层修改后，需通过Alembic生成迁移文件并执行，确保数据库表结构与模型一致，命令如下：
      alembic revision --autogenerate -m "描述信息（如：add product description）"
alembic upgrade head

2. 接口测试：启动项目后，访问 http://127.0.0.1:8000/docs，通过Swagger文档测试所有接口，验证参数校验、业务逻辑、响应格式是否符合规范。

3. 代码复用：优先复用项目现有模板（如crud/base.py），避免重复开发，确保代码一致性。
