# GoodCang Server

开发中心服务 - 站点池、产品池、调研、项目、开发产品全流程管理

## 技术栈

- **后端框架**: FastAPI (异步模式)
- **ORM**: SQLAlchemy (异步模式)
- **数据库**: PostgreSQL
- **缓存**: Redis
- **迁移工具**: Alembic

## 项目结构

```
goodcang_server/
├── app/
│   ├── api/              # API 接口层
│   │   └── v1/
│   │       └── endpoints # 各模块接口
│   ├── client/           # 外部 API 客户端
│   ├── config/          # 配置
│   ├── crud/            # 数据库操作
│   ├── models/          # 数据模型
│   ├── schemas/         # 请求/响应参数
│   ├── services/        # 业务逻辑
│   └── main.py          # 应用入口
├── docs/                # API 文档
└── pyproject.toml       # 项目配置
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

或使用 uv：

```bash
uv sync
```

### 2. 配置环境变量

创建 `.env` 文件：

```env
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=goodcang

REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=6
```

### 3. 数据库迁移

```bash
alembic upgrade head
```

### 4. 启动服务

开发模式：

```bash
uvicorn app.main:app --reload --port 8000
```

或：

```bash
python -m app.main
```

## API 文档

服务启动后访问: http://127.0.0.1:8000/docs

## 主要功能模块

- **Product**: 产品管理
- **Inventory**: 库存管理
- **Order**: 订单管理
- **InboundOrder**: 入库单管理
- **ReturnOrder**: 退货单管理
- **BaseData**: 基础数据

## 运行测试

```bash
pytest
```