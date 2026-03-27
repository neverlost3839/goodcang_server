# API 接口文档

## 基础信息

- **Base URL**: `http://localhost:8000/api/v1`
- **数据格式**: JSON
- **认证方式**: 暂无（当前版本未实现）

---

## 通用响应结构

### 通用响应 Response

```json
{
  "code": 200,
  "message": "success",
  "data": {}
}
```

### 分页响应 PaginatedResponse

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "items": [],
    "total": 0,
    "page": 1,
    "page_size": 20,
    "total_pages": 0
  }
}
```

### 响应状态码说明

| code | 说明 |
|------|------|
| 200 | 成功 |
| 400 | 请求参数错误 |
| 404 | 资源不存在 |
| 500 | 服务器内部错误 |

---

## 商品管理接口

### 1. 获取商品列表

**接口地址**: `GET /product/get_list`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 | 默认值 |
|--------|------|------|------|--------|
| page | integer | 否 | 页码，从1开始 | 1 |
| page_size | integer | 否 | 每页条数(1-100) | 20 |
| sku | string | 否 | 商品SKU（精确匹配） | - |
| name | string | 否 | 商品名称（模糊匹配） | - |
| category | string | 否 | 商品分类 | - |
| brand | string | 否 | 商品品牌 | - |
| status | string | 否 | 商品状态 | - |
| updated_at_from | datetime | 否 | 更新时间起始（ISO 8601格式） | - |
| updated_at_to | datetime | 否 | 更新时间截止（ISO 8601格式） | - |

**请求示例**:
```
GET /api/v1/product/get_list?page=1&page_size=20&name=手机
```

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "items": [
      {
        "sku": "SKU001",
        "name": "iPhone 15 Pro",
        "description": "苹果最新款手机",
        "price": 8999.0,
        "category": "电子产品",
        "brand": "Apple",
        "status": "active",
        "id": 1,
        "created_at": "2024-01-01T00:00:00",
        "updated_at": "2024-01-01T00:00:00"
      }
    ],
    "total": 1,
    "page": 1,
    "page_size": 20,
    "total_pages": 1
  }
}
```

---

### 2. 获取商品详情

**接口地址**: `GET /product/get_detail`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | integer | 是 | 商品ID |

**请求示例**:
```
GET /api/v1/product/get_detail?id=1
```

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "sku": "SKU001",
    "name": "iPhone 15 Pro",
    "description": "苹果最新款手机",
    "price": 8999.0,
    "category": "电子产品",
    "brand": "Apple",
    "status": "active",
    "id": 1,
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00"
  }
}
```

---

### 3. 创建商品

**接口地址**: `POST /product/create`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| sku | string | 是 | 商品SKU |
| name | string | 是 | 商品名称 |
| description | string | 是 | 商品描述 |
| price | float | 是 | 商品价格 |
| category | string | 是 | 商品分类 |
| brand | string | 是 | 商品品牌 |
| status | string | 是 | 商品状态 |

**请求示例**:
```json
POST /api/v1/product/create
{
  "sku": "SKU002",
  "name": "MacBook Pro",
  "description": "苹果笔记本电脑",
  "price": 14999.0,
  "category": "电子产品",
  "brand": "Apple",
  "status": "active"
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "sku": "SKU002",
    "name": "MacBook Pro",
    "description": "苹果笔记本电脑",
    "price": 14999.0,
    "category": "电子产品",
    "brand": "Apple",
    "status": "active",
    "id": 2,
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00"
  }
}
```

---

### 4. 更新商品

**接口地址**: `POST /product/update`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | integer | 是 | 商品ID（Query参数） |
| sku | string | 否 | 商品SKU |
| name | string | 否 | 商品名称 |
| description | string | 否 | 商品描述 |
| price | float | 否 | 商品价格 |
| category | string | 否 | 商品分类 |
| brand | string | 否 | 商品品牌 |
| status | string | 否 | 商品状态 |

**请求示例**:
```
POST /api/v1/product/update?id=1
{
  "name": "iPhone 15 Pro Max",
  "price": 9999.0
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "sku": "SKU001",
    "name": "iPhone 15 Pro Max",
    "description": "苹果最新款手机",
    "price": 9999.0,
    "category": "电子产品",
    "brand": "Apple",
    "status": "active",
    "id": 1,
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00"
  }
}
```

---

### 5. 删除商品

**接口地址**: `POST /product/delete`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | integer | 是 | 商品ID（Query参数） |

**请求示例**:
```
POST /api/v1/product/delete?id=1
```

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": true
}
```

---

**商品对象 ProductOut 字段说明**:

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | integer | 商品ID |
| sku | string | 商品SKU |
| name | string | 商品名称 |
| description | string | 商品描述 |
| price | float | 商品价格 |
| category | string | 商品分类 |
| brand | string | 商品品牌 |
| status | string | 商品状态 |
| created_at | datetime | 创建时间 |
| updated_at | datetime | 更新时间 |

---

## 订单管理接口

### 6. 获取订单列表

**接口地址**: `GET /order/get_list`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 | 默认值 |
|--------|------|------|------|--------|
| page | integer | 否 | 页码，从1开始 | 1 |
| page_size | integer | 否 | 每页条数(1-100) | 20 |
| code | string | 否 | 订单编号（模糊匹配） | - |
| product_id | integer | 否 | 商品ID | - |
| username | string | 否 | 收件用户名（模糊匹配） | - |
| status | string | 否 | 订单状态 | - |
| updated_at_from | datetime | 否 | 更新时间起始（ISO 8601格式） | - |
| updated_at_to | datetime | 否 | 更新时间截止（ISO 8601格式） | - |

**请求示例**:
```
GET /api/v1/order/get_list?page=1&page_size=20&status=scraped
```

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "items": [
      {
        "id": 1,
        "code": "ORDER001",
        "description": "测试订单",
        "product_id": 1,
        "username": "张三",
        "status": "scraped",
        "created_at": "2024-01-01T00:00:00",
        "updated_at": "2024-01-01T00:00:00"
      }
    ],
    "total": 1,
    "page": 1,
    "page_size": 20,
    "total_pages": 1
  }
}
```

---

### 7. 获取订单详情

**接口地址**: `GET /order/get_detail`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | integer | 是 | 订单ID |

**请求示例**:
```
GET /api/v1/order/get_detail?id=1
```

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "id": 1,
    "code": "ORDER001",
    "description": "测试订单",
    "product_id": 1,
    "username": "张三",
    "status": "scraped",
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00"
  }
}
```

---

### 8. 创建订单

**接口地址**: `POST /order/create`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| code | string | 是 | 订单编号 |
| description | string | 是 | 订单描述 |
| product_id | integer | 是 | 商品ID |
| username | string | 是 | 收件用户名 |
| status | string | 否 | 订单状态，默认"scraped" |

**请求示例**:
```json
POST /api/v1/order/create
{
  "code": "ORDER002",
  "description": "新订单",
  "product_id": 1,
  "username": "李四",
  "status": "scraped"
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "id": 2,
    "code": "ORDER002",
    "description": "新订单",
    "product_id": 1,
    "username": "李四",
    "status": "scraped",
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00"
  }
}
```

---

### 9. 更新订单

**接口地址**: `POST /order/update`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | integer | 是 | 订单ID（Query参数） |
| code | string | 否 | 订单编号 |
| description | string | 否 | 订单描述 |
| product_id | integer | 否 | 商品ID |
| username | string | 否 | 收件用户名 |
| status | string | 否 | 订单状态 |

**请求示例**:
```
POST /api/v1/order/update?id=1
{
  "status": "processing"
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "id": 1,
    "code": "ORDER001",
    "description": "测试订单",
    "product_id": 1,
    "username": "张三",
    "status": "processing",
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00"
  }
}
```

---

### 10. 删除订单

**接口地址**: `POST /order/delete`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | integer | 是 | 订单ID（Query参数） |

**请求示例**:
```
POST /api/v1/order/delete?id=1
```

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": true
}
```

---

**订单对象 OrderOut 字段说明**:

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | integer | 订单ID |
| code | string | 订单编号 |
| description | string | 订单描述 |
| product_id | integer | 关联的商品ID |
| username | string | 收件用户名 |
| status | string | 订单状态 |
| created_at | datetime | 创建时间 |
| updated_at | datetime | 更新时间 |

---

## 错误响应示例

### 400 错误（参数错误）

```json
{
  "code": 400,
  "message": "Validation error",
  "data": null
}
```

### 404 错误（资源不存在）

```json
{
  "code": 404,
  "message": "商品ID 1 不存在",
  "data": null
}
```

### 500 错误（服务器错误）

```json
{
  "code": 500,
  "message": "Internal server error",
  "data": null
}
```

---

## 附录

### 日期时间格式

所有日期时间字段使用 ISO 8601 格式：

- `2024-01-01T00:00:00` - 带时分秒
- `2024-01-01` - 仅日期

### 分页说明

- `page`: 当前页码，从1开始
- `page_size`: 每页显示的记录数，最大100
- `total`: 总记录数
- `total_pages`: 总页数

### 状态说明

**商品状态 (status)**:
- `active` - 活跃
- `inactive` - 未激活
- `archived` - 已归档

**订单状态 (status)**:
- `scraped` - 已爬取
- `processing` - 处理中
- `completed` - 已完成
- `cancelled` - 已取消

---

## 用户认证与个人信息接口

### 1. 注册

**接口地址**: `POST /auth/register`

**请求示例**:
```json
POST /api/v1/auth/register
{
  "username": "test_user",
  "password": "123456",
  "nickname": "测试用户",
  "email": "test@example.com",
  "phone": "13800000000",
  "avatar": "",
  "gender": "unknown",
  "bio": "hello"
}
```

### 2. 登录

**接口地址**: `POST /auth/login`

**请求示例**:
```json
POST /api/v1/auth/login
{
  "username": "test_user",
  "password": "123456"
}
```

### 3. 获取个人信息

**接口地址**: `GET /auth/get_profile`

**请求示例**:
```
GET /api/v1/auth/get_profile?user_id=1
```

### 4. 更新个人信息

**接口地址**: `POST /auth/update_profile`

**请求示例**:
```json
POST /api/v1/auth/update_profile?user_id=1
{
  "nickname": "新昵称",
  "email": "new@example.com",
  "bio": "updated"
}
```
