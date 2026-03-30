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
| 502 | 第三方API调用失败 |
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
| product_sku | string | 否 | 商品SKU（模糊匹配） | - |
| product_name_cn | string | 否 | 中文商品名称（模糊匹配） | - |
| product_name_en | string | 否 | 英文商品名称（模糊匹配） | - |
| product_brand | string | 否 | 商品品牌（模糊匹配） | - |
| verify | integer | 否 | 审核状态（0:草稿 1:审核） | - |
| updated_at_from | datetime | 否 | 更新时间起始（ISO 8601格式） | - |
| updated_at_to | datetime | 否 | 更新时间截止（ISO 8601格式） | - |

**请求示例**:
```
GET /api/v1/product/get_list?page=1&page_size=20&product_name_cn=手机
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
        "product_sku": "SKU001",
        "reference_no": "REF001",
        "thirdparty_sku_mapping": "THIRD001",
        "product_name_cn": "iPhone 15 Pro",
        "product_name_en": "iPhone 15 Pro",
        "product_weight": 0.5,
        "product_length": 20.0,
        "product_width": 10.0,
        "product_height": 5.0,
        "sku_wrapper_type": 1,
        "cat_lang": "zh",
        "cat_id_level2": 100,
        "contain_battery": 0,
        "type_of_goods": 0,
        "branded": 1,
        "product_brand": "Apple",
        "product_model": "A3101",
        "product_link": "https://example.com/product",
        "unit": "PCS",
        "return_auth": 1,
        "return_replacement_sku": null,
        "verify": 0,
        "product_barcode": null,
        "is_deleted": 0,
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
    "id": 1,
    "product_sku": "SKU001",
    "reference_no": "REF001",
    "thirdparty_sku_mapping": "THIRD001",
    "product_name_cn": "iPhone 15 Pro",
    "product_name_en": "iPhone 15 Pro",
    "product_weight": 0.5,
    "product_length": 20.0,
    "product_width": 10.0,
    "product_height": 5.0,
    "sku_wrapper_type": 1,
    "cat_lang": "zh",
    "cat_id_level2": 100,
    "contain_battery": 0,
    "type_of_goods": 0,
    "branded": 1,
    "product_brand": "Apple",
    "product_model": "A3101",
    "product_link": "https://example.com/product",
    "unit": "PCS",
    "return_auth": 1,
    "return_replacement_sku": null,
    "verify": 0,
    "product_barcode": null,
    "is_deleted": 0,
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00"
  }
}
```

---

### 3. 创建商品

**接口地址**: `POST /product/create`

**功能说明**: 
- 先调用第三方GoodCang API创建商品
- 第三方API创建成功后再写入本地数据库
- 需要配置 GOODCANG_API_KEY 和 GOODCANG_CLIENT_CODE

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| product_sku | string | 是 | SKU（最大24字符） |
| reference_no | string | 否 | 客户参考代码（最大255字符） |
| thirdparty_sku_mapping | string | 否 | 第三方映射编码（最大50字符） |
| product_name_cn | string | 是 | 中文商品名称（最大255字符） |
| product_name_en | string | 是 | 英文商品名称（最大255字符） |
| product_weight | float | 是 | 重量KG（大于0） |
| product_length | float | 是 | 长CM（大于0） |
| product_width | float | 是 | 宽CM（大于0） |
| product_height | float | 是 | 高CM（大于0） |
| sku_wrapper_type | integer | 否 | 包装属性（默认1） |
| cat_lang | string | 否 | 品类语言（默认zh） |
| cat_id_level2 | integer | 是 | 二级品类ID（大于0） |
| contain_battery | integer | 否 | 货物属性（默认0:普货） |
| type_of_goods | integer | 否 | 包裹类型（默认0:包裹） |
| branded | integer | 否 | 是否品牌（默认0:否） |
| product_brand | string | 否 | 商品品牌（branded=1时必填） |
| product_model | string | 否 | 商品型号 |
| product_link | string | 是 | 商品售卖链接（最大1000字符） |
| unit | string | 否 | 成交单位（默认PCS） |
| return_auth | integer | 否 | 退件授权（默认1:已授权） |
| return_replacement_sku | string | 否 | 换标编码 |
| verify | integer | 否 | 审核状态（默认0:草稿，1:审核） |

**货物属性说明 (contain_battery)**:
- 0: 普货
- 1: 含电池
- 2: 纯电池
- 3: 纺织品
- 4: 易碎品
- 6: 超标纯电池
- 7: 超标含电池

**包裹类型说明 (type_of_goods)**:
- 0: 包裹
- 1: 信封

**请求示例**:
```json
POST /api/v1/product/create
{
  "product_sku": "SKU002",
  "reference_no": "REF002",
  "product_name_cn": "MacBook Pro",
  "product_name_en": "MacBook Pro",
  "product_weight": 2.0,
  "product_length": 35.0,
  "product_width": 25.0,
  "product_height": 1.5,
  "cat_id_level2": 101,
  "contain_battery": 0,
  "type_of_goods": 0,
  "branded": 1,
  "product_brand": "Apple",
  "product_model": "MacBook Pro 14",
  "product_link": "https://example.com/macbook",
  "verify": 0
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "id": 2,
    "product_sku": "SKU002",
    "reference_no": "REF002",
    "thirdparty_sku_mapping": null,
    "product_name_cn": "MacBook Pro",
    "product_name_en": "MacBook Pro",
    "product_weight": 2.0,
    "product_length": 35.0,
    "product_width": 25.0,
    "product_height": 1.5,
    "sku_wrapper_type": 1,
    "cat_lang": "zh",
    "cat_id_level2": 101,
    "contain_battery": 0,
    "type_of_goods": 0,
    "branded": 1,
    "product_brand": "Apple",
    "product_model": "MacBook Pro 14",
    "product_link": "https://example.com/macbook",
    "unit": "PCS",
    "return_auth": 1,
    "return_replacement_sku": null,
    "verify": 0,
    "product_barcode": null,
    "is_deleted": 0,
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00"
  }
}
```

**错误响应示例**:

- 配置错误（400）:
```json
{
  "code": 400,
  "message": "APIKey不能为空，请配置GOODCANG_API_KEY",
  "data": null
}
```

- 第三方API调用失败（502）:
```json
{
  "code": 502,
  "message": "调用第三方API失败: ...",
  "data": null
}
```

- 第三方API返回错误（400）:
```json
{
  "code": 400,
  "message": "第三方API返回的错误信息",
  "data": null
}
```

---

### 4. 更新商品

**接口地址**: `PUT /product/update/{id}`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | integer | 是 | 商品ID（Path参数） |
| product_sku | string | 否 | SKU（最大24字符） |
| reference_no | string | 否 | 客户参考代码 |
| thirdparty_sku_mapping | string | 否 | 第三方映射编码 |
| product_name_cn | string | 否 | 中文商品名称 |
| product_name_en | string | 否 | 英文商品名称 |
| product_weight | float | 否 | 重量KG |
| product_length | float | 否 | 长CM |
| product_width | float | 否 | 宽CM |
| product_height | float | 否 | 高CM |
| sku_wrapper_type | integer | 否 | 包装属性 |
| cat_lang | string | 否 | 品类语言 |
| cat_id_level2 | integer | 否 | 二级品类ID |
| contain_battery | integer | 否 | 货物属性 |
| type_of_goods | integer | 否 | 包裹类型 |
| branded | integer | 否 | 是否品牌 |
| product_brand | string | 否 | 商品品牌 |
| product_model | string | 否 | 商品型号 |
| product_link | string | 否 | 商品售卖链接 |
| unit | string | 否 | 成交单位 |
| return_auth | integer | 否 | 退件授权 |
| return_replacement_sku | string | 否 | 换标编码 |
| verify | integer | 否 | 审核状态 |
| product_barcode | string | 否 | 商品条码 |

**请求示例**:
```
PUT /api/v1/product/update/1
```
```json
{
  "product_name_cn": "iPhone 15 Pro Max",
  "product_brand": "Apple",
  "verify": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "id": 1,
    "product_sku": "SKU001",
    "reference_no": "REF001",
    "product_name_cn": "iPhone 15 Pro Max",
    "product_name_en": "iPhone 15 Pro Max",
    "product_weight": 0.5,
    "product_length": 20.0,
    "product_width": 10.0,
    "product_height": 5.0,
    "sku_wrapper_type": 1,
    "cat_lang": "zh",
    "cat_id_level2": 100,
    "contain_battery": 0,
    "type_of_goods": 0,
    "branded": 1,
    "product_brand": "Apple",
    "product_model": "A3101",
    "product_link": "https://example.com/product",
    "unit": "PCS",
    "return_auth": 1,
    "return_replacement_sku": null,
    "verify": 1,
    "product_barcode": null,
    "is_deleted": 0,
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-02T00:00:00"
  }
}
```

---

### 5. 删除商品

**接口地址**: `DELETE /product/delete`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | integer | 是 | 商品ID（Query参数） |

**请求示例**:
```
DELETE /api/v1/product/delete?id=1
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
| product_sku | string | SKU |
| reference_no | string | 客户参考代码 |
| thirdparty_sku_mapping | string | 第三方映射编码 |
| product_name_cn | string | 中文商品名称 |
| product_name_en | string | 英文商品名称 |
| product_weight | float | 重量KG |
| product_length | float | 长CM |
| product_width | float | 宽CM |
| product_height | float | 高CM |
| sku_wrapper_type | integer | 包装属性 |
| cat_lang | string | 品类语言 |
| cat_id_level2 | integer | 二级品类ID |
| contain_battery | integer | 货物属性 |
| type_of_goods | integer | 包裹类型 |
| branded | integer | 是否品牌 |
| product_brand | string | 商品品牌 |
| product_model | string | 商品型号 |
| product_link | string | 商品售卖链接 |
| unit | string | 成交单位 |
| return_auth | integer | 退件授权 |
| return_replacement_sku | string | 换标编码 |
| verify | integer | 审核状态 |
| product_barcode | string | 商品条码 |
| is_deleted | integer | 是否删除 |
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

### 502 错误（第三方API调用失败）

```json
{
  "code": 502,
  "message": "调用第三方API失败: ...",
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

### 商品相关枚举说明

**审核状态 (verify)**:
- 0: 草稿
- 1: 审核

**包装属性 (sku_wrapper_type)**:
- 1: 预包装
- 2: 销售包装
- 3: 原包彩盒

**货物属性 (contain_battery)**:
- 0: 普货
- 1: 含电池
- 2: 纯电池
- 3: 纺织品
- 4: 易碎品
- 6: 超标纯电池
- 7: 超标含电池

**包裹类型 (type_of_goods)**:
- 0: 包裹
- 1: 信封

**退件授权 (return_auth)**:
- 0: 未授权
- 1: 已授权
