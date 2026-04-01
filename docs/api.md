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

## 订单管理接口

### 1. 获取订单列表

**接口地址**: `GET /order/get_list`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 | 默认值 |
|--------|------|------|------|--------|
| page | integer | 否 | 页码，从1开始 | 1 |
| page_size | integer | 否 | 每页条数(1-100) | 20 |
| reference_no | string | 否 | 订单参考号（模糊匹配） | - |
| platform | string | 否 | 平台代码 | - |
| warehouse_code | string | 否 | 发货仓库代码 | - |
| country_code | string | 否 | 国家二字码 | - |
| name | string | 否 | 收件人名（模糊匹配） | - |
| phone | string | 否 | 联系电话（模糊匹配） | - |
| email | string | 否 | 邮箱（模糊匹配） | - |
| verify | integer | 否 | 审核状态（0:草稿 1:审核） | - |
| order_code | string | 否 | 谷仓订单号（模糊匹配） | - |
| updated_at_from | datetime | 否 | 更新时间起始 | - |
| updated_at_to | datetime | 否 | 更新时间截止 | - |

**请求示例**:
```
GET /api/v1/order/get_list?page=1&page_size=20&platform=AMAZON
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
        "reference_no": "ORDER001",
        "platform": "AMAZON",
        "shipping_method": "DHL",
        "warehouse_code": "US01",
        "country_code": "US",
        "province": "California",
        "city": "Los Angeles",
        "company": null,
        "address1": "123 Main St",
        "address2": "Apt 4B",
        "zipcode": "90001",
        "doorplate": null,
        "name": "John Doe",
        "last_name": "Doe",
        "cell_phone": null,
        "phone": "+1-555-123-4567",
        "email": "john@example.com",
        "order_desc": "Please handle with care",
        "customer_package_requirement": 1,
        "verify": 1,
        "is_shipping_method_not_allow_update": 1,
        "is_signature": 0,
        "is_insurance": 0,
        "insurance_value": 0.0,
        "fba_shipment_id": null,
        "property_label": null,
        "business_type": 0,
        "is_change_label": 1,
        "age_detection": 0,
        "lift_gate": 0,
        "attachment_ids": null,
        "estimated_arrival_date": null,
        "estimated_arrival_time": null,
        "is_euro_label": null,
        "is_warehouse_packing": 0,
        "sender_info": null,
        "vat_change_info": null,
        "vas": null,
        "carton_info": null,
        "truck_info": null,
        "order_code": "GC20240101001",
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

### 2. 获取订单详情

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
    "reference_no": "ORDER001",
    "platform": "AMAZON",
    "shipping_method": "DHL",
    "warehouse_code": "US01",
    "country_code": "US",
    "province": "California",
    "city": "Los Angeles",
    "company": null,
    "address1": "123 Main St",
    "address2": "Apt 4B",
    "zipcode": "90001",
    "doorplate": null,
    "name": "John Doe",
    "last_name": "Doe",
    "cell_phone": null,
    "phone": "+1-555-123-4567",
    "email": "john@example.com",
    "order_desc": "Please handle with care",
    "customer_package_requirement": 1,
    "verify": 1,
    "is_shipping_method_not_allow_update": 1,
    "is_signature": 0,
    "is_insurance": 0,
    "insurance_value": 0.0,
    "fba_shipment_id": null,
    "property_label": null,
    "business_type": 0,
    "is_change_label": 1,
    "age_detection": 0,
    "lift_gate": 0,
    "attachment_ids": null,
    "estimated_arrival_date": null,
    "estimated_arrival_time": null,
    "is_euro_label": null,
    "is_warehouse_packing": 0,
    "sender_info": null,
    "vat_change_info": null,
    "vas": null,
    "carton_info": null,
    "truck_info": null,
    "order_code": "GC20240101001",
    "is_deleted": 0,
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00"
  }
}
```

---

### 3. 创建订单

**接口地址**: `POST /order/create`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| reference_no | string | 否 | 订单参考号（最大50字符） |
| platform | string | 否 | 平台代码（默认OTHER） |
| shipping_method | string | 否 | 物流产品代码 |
| warehouse_code | string | 否 | 发货仓库代码 |
| country_code | string | 是 | 国家二字码（最大2字符） |
| province | string | 是 | 省/州（最大20字符） |
| city | string | 是 | 城市（最大32字符） |
| company | string | 否 | 公司名称 |
| address1 | string | 是 | 地址1（最大50字符） |
| address2 | string | 否 | 地址2 |
| zipcode | string | 是 | 邮编（最大20字符） |
| doorplate | string | 否 | 门牌号 |
| name | string | 是 | 收件人名（最大48字符） |
| last_name | string | 否 | 收件人姓 |
| cell_phone | string | 否 | 分机号 |
| phone | string | 否 | 联系电话（最大20字符） |
| email | string | 否 | 邮箱（最大100字符） |
| order_desc | string | 否 | 订单备注（最大500字符） |
| customer_package_requirement | integer | 否 | 包材要求（1-4） |
| verify | integer | 否 | 审核状态（默认0草稿） |
| is_shipping_method_not_allow_update | integer | 否 | 是否可修改物流（默认1不可修改） |
| is_signature | integer | 否 | 是否需签名（默认0无需） |
| is_insurance | integer | 否 | 是否有保险（默认0无） |
| insurance_value | float | 否 | 保额（默认0） |
| fba_shipment_id | string | 否 | FBA Shipment ID |
| property_label | string | 否 | 平台模式 |
| business_type | integer | 否 | 业务类型（默认0仓配一体） |
| is_change_label | integer | 否 | 是否换标（默认1换标） |
| age_detection | integer | 否 | 年龄检测（默认0不检测） |
| lift_gate | integer | 否 | 是否LiftGate（默认0否） |
| attachment_ids | array | 否 | 附件ID数组 |
| estimated_arrival_date | datetime | 否 | 预计到货日期 |
| estimated_arrival_time | string | 否 | 到货时间段 |
| is_euro_label | integer | 否 | 欧盟贴标（1贴标 0不贴标） |
| is_warehouse_packing | integer | 否 | 仓库装箱（默认0否） |

**请求示例**:
```json
POST /api/v1/order/create
{
  "reference_no": "ORDER002",
  "platform": "EBAY",
  "shipping_method": "UPS",
  "warehouse_code": "US02",
  "country_code": "US",
  "province": "New York",
  "city": "New York",
  "address1": "456 Broadway",
  "zipcode": "10012",
  "name": "Jane Smith",
  "phone": "+1-555-987-6543",
  "email": "jane@example.com",
  "order_desc": "Gift package",
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
    "reference_no": "ORDER002",
    "platform": "EBAY",
    "shipping_method": "UPS",
    "warehouse_code": "US02",
    "country_code": "US",
    "province": "New York",
    "city": "New York",
    "company": null,
    "address1": "456 Broadway",
    "address2": null,
    "zipcode": "10012",
    "doorplate": null,
    "name": "Jane Smith",
    "last_name": null,
    "cell_phone": null,
    "phone": "+1-555-987-6543",
    "email": "jane@example.com",
    "order_desc": "Gift package",
    "customer_package_requirement": null,
    "verify": 0,
    "is_shipping_method_not_allow_update": 1,
    "is_signature": 0,
    "is_insurance": 0,
    "insurance_value": 0.0,
    "fba_shipment_id": null,
    "property_label": null,
    "business_type": 0,
    "is_change_label": 1,
    "age_detection": 0,
    "lift_gate": 0,
    "attachment_ids": null,
    "estimated_arrival_date": null,
    "estimated_arrival_time": null,
    "is_euro_label": null,
    "is_warehouse_packing": 0,
    "sender_info": null,
    "vat_change_info": null,
    "vas": null,
    "carton_info": null,
    "truck_info": null,
    "order_code": null,
    "is_deleted": 0,
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00"
  }
}
```

---

### 4. 更新订单

**接口地址**: `PUT /order/update/{id}`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | integer | 是 | 订单ID（Path参数） |
| reference_no | string | 否 | 订单参考号 |
| platform | string | 否 | 平台代码 |
| shipping_method | string | 否 | 物流产品代码 |
| warehouse_code | string | 否 | 发货仓库代码 |
| country_code | string | 否 | 国家二字码 |
| province | string | 否 | 省/州 |
| city | string | 否 | 城市 |
| company | string | 否 | 公司名称 |
| address1 | string | 否 | 地址1 |
| address2 | string | 否 | 地址2 |
| zipcode | string | 否 | 邮编 |
| doorplate | string | 否 | 门牌号 |
| name | string | 否 | 收件人名 |
| last_name | string | 否 | 收件人姓 |
| cell_phone | string | 否 | 分机号 |
| phone | string | 否 | 联系电话 |
| email | string | 否 | 邮箱 |
| order_desc | string | 否 | 订单备注 |
| customer_package_requirement | integer | 否 | 包材要求 |
| verify | integer | 否 | 审核状态 |
| is_shipping_method_not_allow_update | integer | 否 | 是否可修改物流 |
| is_signature | integer | 否 | 是否需签名 |
| is_insurance | integer | 否 | 是否有保险 |
| insurance_value | float | 否 | 保额 |
| fba_shipment_id | string | 否 | FBA Shipment ID |
| property_label | string | 否 | 平台模式 |
| business_type | integer | 否 | 业务类型 |
| is_change_label | integer | 否 | 是否换标 |
| age_detection | integer | 否 | 年龄检测 |
| lift_gate | integer | 否 | 是否LiftGate |
| attachment_ids | array | 否 | 附件ID数组 |
| estimated_arrival_date | datetime | 否 | 预计到货日期 |
| estimated_arrival_time | string | 否 | 到货时间段 |
| is_euro_label | integer | 否 | 欧盟贴标 |
| is_warehouse_packing | integer | 否 | 仓库装箱 |
| sender_info | object | 否 | 发件人信息 |
| vat_change_info | object | 否 | 欧盟税改信息 |
| vas | object | 否 | 增值服务 |
| carton_info | object | 否 | FBA转仓单信息 |
| truck_info | object | 否 | 卡派渠道信息 |

**请求示例**:
```
PUT /api/v1/order/update/1
```
```json
{
  "order_desc": "Updated: Fragile items",
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
    "reference_no": "ORDER001",
    "platform": "AMAZON",
    "shipping_method": "DHL",
    "warehouse_code": "US01",
    "country_code": "US",
    "province": "California",
    "city": "Los Angeles",
    "address1": "123 Main St",
    "address2": "Apt 4B",
    "zipcode": "90001",
    "name": "John Doe",
    "phone": "+1-555-123-4567",
    "email": "john@example.com",
    "order_desc": "Updated: Fragile items",
    "verify": 1,
    "is_deleted": 0,
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-02T00:00:00"
  }
}
```

---

### 5. 删除订单

**接口地址**: `DELETE /order/delete`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | integer | 是 | 订单ID（Query参数） |

**请求示例**:
```
DELETE /api/v1/order/delete?id=1
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
| reference_no | string | 订单参考号 |
| platform | string | 平台代码 |
| shipping_method | string | 物流产品代码 |
| warehouse_code | string | 发货仓库代码 |
| country_code | string | 国家二字码 |
| province | string | 省/州 |
| city | string | 城市 |
| company | string | 公司名称 |
| address1 | string | 地址1 |
| address2 | string | 地址2 |
| zipcode | string | 邮编 |
| doorplate | string | 门牌号 |
| name | string | 收件人名 |
| last_name | string | 收件人姓 |
| cell_phone | string | 分机号 |
| phone | string | 联系电话 |
| email | string | 邮箱 |
| order_desc | string | 订单备注 |
| customer_package_requirement | integer | 包材要求 |
| verify | integer | 审核状态 |
| is_shipping_method_not_allow_update | integer | 是否可修改物流 |
| is_signature | integer | 是否需签名 |
| is_insurance | integer | 是否有保险 |
| insurance_value | float | 保额 |
| fba_shipment_id | string | FBA Shipment ID |
| property_label | string | 平台模式 |
| business_type | integer | 业务类型 |
| is_change_label | integer | 是否换标 |
| age_detection | integer | 年龄检测 |
| lift_gate | integer | 是否LiftGate |
| attachment_ids | array | 附件ID数组 |
| estimated_arrival_date | datetime | 预计到货日期 |
| estimated_arrival_time | string | 到货时间段 |
| is_euro_label | integer | 欧盟贴标 |
| is_warehouse_packing | integer | 仓库装箱 |
| sender_info | object | 发件人信息 |
| vat_change_info | object | 欧盟税改信息 |
| vas | object | 增值服务 |
| carton_info | object | FBA转仓单信息 |
| truck_info | object | 卡派渠道信息 |
| order_code | string | 谷仓返回订单号 |
| is_deleted | integer | 是否删除 |
| created_at | datetime | 创建时间 |
| updated_at | datetime | 更新时间 |

---

## 用户管理接口

### 1. 用户注册

**接口地址**: `POST /auth/register`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| username | string | 是 | 用户名（3-64字符） |
| password | string | 是 | 密码（明文，1-128字符） |
| nickname | string | 否 | 昵称（最大64字符） |
| email | string | 否 | 邮箱（最大128字符） |
| phone | string | 否 | 手机号（最大32字符） |
| avatar | string | 否 | 头像URL（最大512字符） |
| gender | string | 否 | 性别（默认unknown） |
| bio | string | 否 | 个人简介（最大512字符） |

**性别说明 (gender)**:
- unknown: 未知
- male: 男性
- female: 女性

**请求示例**:
```json
POST /api/v1/auth/register
{
  "username": "test_user",
  "password": "123456",
  "nickname": "测试用户",
  "email": "test@example.com",
  "phone": "13800000000",
  "gender": "male"
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "id": 1,
    "username": "test_user",
    "nickname": "测试用户",
    "email": "test@example.com",
    "phone": "13800000000",
    "avatar": "",
    "gender": "male",
    "bio": "",
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00"
  }
}
```

---

### 2. 用户登录

**接口地址**: `POST /auth/login`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| username | string | 是 | 用户名（3-64字符） |
| password | string | 是 | 密码（明文，1-128字符） |

**请求示例**:
```json
POST /api/v1/auth/login
{
  "username": "test_user",
  "password": "123456"
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "id": 1,
    "username": "test_user",
    "nickname": "测试用户",
    "email": "test@example.com",
    "phone": "13800000000",
    "avatar": "",
    "gender": "male",
    "bio": "",
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00"
  }
}
```

---

### 3. 获取用户信息

**接口地址**: `GET /auth/get_profile`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| user_id | integer | 是 | 用户ID |

**请求示例**:
```
GET /api/v1/auth/get_profile?user_id=1
```

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "id": 1,
    "username": "test_user",
    "nickname": "测试用户",
    "email": "test@example.com",
    "phone": "13800000000",
    "avatar": "",
    "gender": "male",
    "bio": "",
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00"
  }
}
```

---

### 4. 更新用户信息

**接口地址**: `PUT /auth/update_profile`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| user_id | integer | 是 | 用户ID（Query参数） |
| nickname | string | 否 | 昵称 |
| email | string | 否 | 邮箱 |
| phone | string | 否 | 手机号 |
| avatar | string | 否 | 头像URL |
| gender | string | 否 | 性别 |
| bio | string | 否 | 个人简介 |

**请求示例**:
```
PUT /api/v1/auth/update_profile?user_id=1
```
```json
{
  "nickname": "新昵称",
  "email": "new@example.com",
  "bio": "更新后的个人简介"
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "id": 1,
    "username": "test_user",
    "nickname": "新昵称",
    "email": "new@example.com",
    "phone": "13800000000",
    "avatar": "",
    "gender": "male",
    "bio": "更新后的个人简介",
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-02T00:00:00"
  }
}
```

---

**用户对象 UserOut 字段说明**:

| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | integer | 用户ID |
| username | string | 用户名 |
| nickname | string | 昵称 |
| email | string | 邮箱 |
| phone | string | 手机号 |
| avatar | string | 头像URL |
| gender | string | 性别 |
| bio | string | 个人简介 |
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

---

## 库存管理接口

### 1. 获取库存列表

**接口地址**: `GET /inventory/get_list`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 | 默认值 |
|--------|------|------|------|--------|
| page | integer | 否 | 页码，从1开始 | 1 |
| page_size | integer | 否 | 每页条数(1-100) | 20 |
| product_sku | string | 否 | 商品SKU | - |
| product_sku_arr | array | 否 | 多个商品SKU数组 | - |
| warehouse_code | string | 否 | 仓库代码 | - |
| warehouse_code_arr | array | 否 | 多个仓库代码数组 | - |

**请求示例**:
```
GET /api/v1/inventory/get_list?warehouse_code=USWE&page=1&page_size=20
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
        "product_barcode": "BAR001",
        "warehouse_code": "USWE",
        "warehouse_desc": "美西仓",
        "onway": 50,
        "pending": 20,
        "sellable": 100,
        "unsellable": 5,
        "reserved": 10,
        "shipped": 200,
        "stocking": 30,
        "pi_no_stock": 0,
        "pi_freeze": 5,
        "product_sales_value": 29.99,
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

### 2. 同步库存

**接口地址**: `POST /inventory/sync`

**功能说明**: 
- 从第三方GoodCang API获取库存数据
- 同步策略：标记删除(API不存在的记录) → 更新(存在的记录) → 新增(新记录)
- 支持按仓库或按SKU同步

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| warehouse_code | string | 否* | 仓库代码 |
| warehouse_code_arr | array | 否* | 多个仓库代码数组 |
| product_sku | string | 否 | 商品SKU |
| product_sku_arr | array | 否 | 多个商品SKU数组 |

> * warehouse_code 或 warehouse_code_arr 至少指定一个

**请求示例**:
```json
POST /api/v1/inventory/sync
{
  "warehouse_code_arr": ["USWE", "USEA"]
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "total_count": 100,
    "deleted_count": 5,
    "updated_count": 80,
    "created_count": 15,
    "warehouses": ["USWE", "USEA"]
  }
}
```

**库存字段说明**:

| 字段名 | 类型 | 说明 |
|--------|------|------|
| onway | integer | 在途数量 |
| pending | integer | 待上架数量 |
| sellable | integer | 可售库存 |
| unsellable | integer | 不可售/不合格数量 |
| reserved | integer | 预占/待出库数量 |
| shipped | integer | 历史出库数量 |
| stocking | integer | 备货数量 |
| pi_no_stock | integer | 缺货数量 |
| pi_freeze | integer | 冻结数量 |
| product_sales_value | float | 商品销售价值 |

---

## 入库单管理接口

### 1. 创建入库单

**接口地址**: `POST /inbound_order/create`

**功能说明**: 
- 先调用第三方GoodCang API创建入库单
- 第三方API创建成功后再写入本地数据库

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| transit_type | integer | 是 | 入库单类型 (0:自发 3:中转 5:FBA) |
| receiving_shipping_type | integer | 是 | 运输方式 (0-5) |
| warehouse_code | string | 是 | 海外仓仓库编码 |
| reference_no | string | 否 | 参考号 |
| sm_code | string | 否 | 物流产品(中转特有) |
| transit_warehouse_code | string | 否 | 中转仓仓库编码(中转特有) |
| customs_type | integer | 否 | 报关方式(中转特有) |
| tracking_number | string | 否 | 跟踪号/海柜号 |
| eta_date | datetime | 否 | 预计到达时间 |
| receiving_desc | string | 否 | 备注 |
| verify | integer | 否 | 是否审核 (默认0) |
| weight | float | 否 | 重量(kg) |
| volume | float | 否 | 体积(立方米) |
| is_rollover | integer | 否 | 是否仓库装箱商品 (默认0) |
| shiper_address | object | 否 | 发件人地址(自发入库单) |
| items | array | 是 | 入库单明细 |

**入库单类型 (transit_type)**:
- 0: 自发入库单
- 3: 中转入库单
- 5: FBA入库单

**运输方式 (receiving_shipping_type)**:
- 0: 空运
- 1: 海运散货
- 2: 快递
- 3: 铁运整柜
- 4: 海运整柜
- 5: 铁运散货

**请求示例**:
```json
POST /api/v1/inbound_order/create
{
  "transit_type": 0,
  "receiving_shipping_type": 0,
  "warehouse_code": "USWE",
  "reference_no": "IN20240301001",
  "eta_date": "2024-03-15T00:00:00",
  "verify": 1,
  "items": [
    {
      "box_no": 1,
      "box_details": [
        {
          "product_sku": "SKU001",
          "quantity": 50
        }
      ]
    }
  ]
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "id": 1,
    "receiving_code": "GRN-USWE-001",
    "reference_no": "IN20240301001",
    "transit_type": 0,
    "receiving_shipping_type": 0,
    "warehouse_code": "USWE",
    "verify": 1,
    "items": [
      {
        "id": 1,
        "inbound_order_id": 1,
        "box_no": 1,
        "product_sku": "SKU001",
        "quantity": 50,
        "created_at": "2024-01-01T00:00:00"
      }
    ],
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00",
    "is_deleted": 0
  }
}
```

---

### 2. 获取入库单详情

**接口地址**: `GET /inbound_order/{id}`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | integer | 是 | 入库单ID (Path参数) |

**请求示例**:
```
GET /api/v1/inbound_order/1
```

---

### 3. 获取入库单列表

**接口地址**: `GET /inbound_order/`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 | 默认值 |
|--------|------|------|------|--------|
| page | integer | 否 | 页码，从1开始 | 1 |
| page_size | integer | 否 | 每页条数(1-100) | 20 |
| receiving_code | string | 否 | 入库单号 | - |
| reference_no | string | 否 | 参考号 | - |
| warehouse_code | string | 否 | 仓库编码 | - |

---

## 仓库代码说明

| 代码 | 说明 |
|------|------|
| USWE | 美西仓 |
| USEA | 美东仓 |
| UKLD | 英国仓 |
