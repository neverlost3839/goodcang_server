RESTFUL V1获取国家/地区列表
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
说明：获取系统预设的国家/地区的简称，英文全称，中文名称。
URLhttps://oms.goodcang.net/public_open/base_data/get_country
METHODPOST
请求JSON示例

1
2
{
}
响应JSON示例

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
{
    "ask": "Success",
    "message": "success",
    "data": [
        {
            "country_code": "CN",
            "country_name": "中国",
            "country_name_en": "China"
        },
        {
            "country_code": "DZ",
            "country_name": "阿尔及利亚",
            "country_name_en": "Algeria"
        },
        {
            "country_code": "AF",
            "country_name": "阿富汗",
            "country_name_en": "Afghanistan"
        },
        {
            "country_code": "HK",
            "country_name": "中国香港",
            "country_name_en": "Hong Kong"
        },
        {
            "country_code": "MO",
            "country_name": "中国澳门",
            "country_name_en": "Macao"
        },
        {
            "country_code": "TW",
            "country_name": "中国台湾",
            "country_name_en": "Taiwan"
        }
    ]
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
无
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
data	Object[]	国家/地区数据数组，数组元素对象说明参见下文CountryListItem。
CountryListItem

参数名	数据类型	说明
country_code	String	国家/地区二字码
country_name	String	国家/地区中文名
country_name_en	String	国家/地区英文名

----------------------------------------------------------------

RESTFUL V1获取系统仓库
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
说明：获取系统中仓库的仓库代码、仓库名称和所在国家/地区的信息。
URLhttps://oms.goodcang.net/public_open/base_data/get_warehouse
METHODPOST
请求JSON示例

1
2
{
}
响应JSON示例

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
{
    "ask": "Success",
    "message": "success",
    "data": [
        {
            "warehouse_code": "FRVI",
            "warehouse_name": "法国仓库",
            "country_code": "FR"
        },
        {
            "warehouse_code": "ES",
            "warehouse_name": "西班牙仓库",
            "country_code": "ES"
        },
        {
            "warehouse_code": "USWE",
            "warehouse_name": "美西仓库",
            "country_code": "US"
        }
    ]
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
无
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
data	Object[]	仓库数据数组，数组元素对象说明参见下文WarehouseListItem。
WarehouseListItem参数

参数名	数据类型	说明
warehouse_code	String	仓库代码
warehouse_name	String	仓库名称
country_code	String	仓库所在国家/地区代码
wp_list	Object[]	物理仓对象数组，数组元素对像结构参见 PhysicalWarehouseItem 对象。
PhysicalWarehouseItem

参数名	数据类型	说明
code	String	物理仓代码
name	String	物理仓名称
address	Object[]	地址信息，参见 PhysicalWarehouseAddress
PhysicalWarehouseAddress

参数名	数据类型	说明
state	String	省/州
city	String	城市
postcode	String	邮编
contacter	String	联系人
phone	String	电话
street_address1	String	地址1
street_address2	String	地址2
street_number	String	门牌号


------------------------------------------

RESTFUL V1获取物流产品
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
说明：获取系统中 所有物流派送方式的物流代码和物流产品中英文名称，和对应支持派送的仓库信息。
URLhttps://oms.goodcang.net/public_open/base_data/get_shipping_method
METHODPOST
请求JSON示例

1
2
3
{
    "warehouseCode": "USEA"
}
响应JSON示例

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
{
    "ask": "Success",
    "message": "success",
    "data": [
        {
            "code": "TRACKED_NS",
            "name": "Tracked_NS挂号(包裹)",
            "name_en": "",
            "warehouse_code": "UK",
            "type": "0",
            "is_signature": 0,
            "is_specify_arrival_time": 0
        },
        {
            "code": "UPSROUND",
            "name": "UPSround",
            "name_en": "",
            "warehouse_code": "USWE",
            "type": "0",
            "is_signature": 1,
            "is_specify_arrival_time": 0
        }
    ]
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
warehouseCode	String	Optional	32	尾程仓库代码	USWE
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
data	Object[]	物流方式数据数组，数组元素对象说明参见下文ShippingMethodListItem。
ShippingMethodListItem参数

参数名	数据类型	说明
code	String	物流产品代码
name	String	物流产品中文名称
name_en	String	物流产品英文名称
warehouse_code	String	仓库代码
type	String	物流产品类型
0-尾程物流产品
1-退件代选物流产品
2-头程物流产品
3-退件自选物流产品
4-未预报退件物流产品
5-销毁物流产品
6-自提物流产品
 
sp_code	String	服务商代码
is_signature	Number	是否支持签名服务（0 否，1 是）
address_validation_enabled	Number	是否支持地址校验（0 不支持，1 支持）
is_truck	Number	是否卡派渠道（0 否，1 是）
is_specify_arrival_time	Number	是否指定到货时间（1 支持，2 不支持）
delivery_time_list	String[]	支持的到货时间段
sm_business_type	Int	业务类型
1：仓配一体
3：仓配分离
 
 --------------------------------------------

 RESTFUL V1获取公司账户
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
说明：获取签约主体、和相关主体资料、余额等等。
URLhttps://oms.goodcang.net/public_open/base_data/get_account_list
METHODPOST
请求JSON示例

1
2
{
}
响应JSON示例

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
{
    "ask": "Success",
    "message": "Success",
    "data": {
        "customer_code": "G296",
        "account_list": [
            {
                "firm_name": "企业名称1",
                "firm_status": 3,
                "server_firm_name": "ETARGET LIMITED",
                "business_type_list": [
                    0,
                    1
                ],
                "account_code": "AC123456",
                "balance_list": [
                    {
                        "currency_code": "AUD",
                        "amount": "0"
                    },
                    {
                        "currency_code": "USD",
                        "amount": "-21058639.794"
                    }
                ]
            },
            {
                "firm_name": "企业名称2",
                "firm_status": 5,
                "server_firm_name": "",
                "business_type_list": [],
                "account_code": "AC0000",
                "balance_list": []
            }
        ]
    }
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
无
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
data	Object	账户详情，请参见下文 AccountItem。
AccountItem参数

参数名	数据类型	说明
customer_code	String	客户代码
account_list	Object[]	账户信息数据数组，数组元素请参见下文 AccountListItem。
AccountListItem参数

参数名	数据类型	说明
firm_name	String	签约主体名称（例如企业名称）
firm_status	String	签约主体状态
0-审核中
1-审核不通过
2-可用
3-停用
4-已作废
5-草稿
6-待签约
server_firm_name	String	服务主体
0-深圳谷仓科技有限公司
1-ETARGET LIMITED
2-ELOGISTIC
business_type_list	String	签约业务类型
0-海外仓储
1-中转代发
balance_list	Object[]	币种信息数组，数组元素请参见下文 BalanceListItem。
BalanceListItem参数

参数名	数据类型	说明
currency_code	String	公司代码
amount	String	金额（双精度数字，避免精度丢失，API以字符串形式返回，请客户端酌情处理）

-------------------------------------------------------

RESTFUL获取费用类型
这是RESTFUL WEB API，接入方式请参见GD开放平台(V2)接入指引。
URLhttps://oms.goodcang.net/public_open/base_data/cost_type_list
METHODPOST
请求JSON示例

1
2
3
{
    "sign_business_type":0
}
响应JSON示例

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
{
    "code": 0,
    "message": "success",
    "data": [
        {
            "cost_name": "备用费用-2",
            "cost_code": "SCF2"
        },
        {
            "cost_name": "备用费用-1",
            "cost_code": "SCF1"
        },
        {
            "cost_name": "超重费-2",
            "cost_code": "OWF2"
        }
    ]
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
sign_business_type	Int	Required		业务类型，(枚举类型)
0: 海外仓储
1: 中转代发
0
响应JSON

参数名	数据类型	说明
code	Int	0 成功，其它值表示失败。
message	String	文本消息
data	Object[]	数组元素类型, 参见CostTypeItemResp类型
CostTypeItemResp数据类型

参数名	数据类型	可为空	说明
cost_name	String	False	费用名称
cost_code	String	False	费用编码

----------------------------------------------------------------------------

RESTFUL获取燃油费率
这是RESTFUL WEB API，接入方式请参见GD开放平台(V2)接入指引。
URLhttps://oms.goodcang.net/public_open/base_data/fuel_rate_list
METHODPOST
请求JSON示例

1
2
3
4
5
6
7
8
{
    "logistic_type": 0,
    "sm_code": "code",
    "begin_time": "2021-09-15 00:00:00",
    "end_time": "2021-10-15 23:59:59",
    "page": 1,
    "page_size": 10
}
响应JSON示例

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
{
    "code": 0,
    "message": "success",
    "data": {
        "total": 1231,
        "list": [
            {
                 "fls_rate": "",
                 "fls_begin_time": "",
                 "fls_end_time": "",
                 "sm_name": "",
                 "sm_code": ""
            }
        ]
    }
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
logistic_type	Int	Required		物流产品，(枚举类型)
0: 发货物流
1: 退货物流
0
sm_code	String	Required		物流产品编码	CZ_DHL_DOMESTICPK
begin_time	String	Required		起始生效时间（北京时间,31天跨度,时间区间参数必须成对出现）	2021-09-15 00:00:00
end_time	String	Required		结束生效时间（北京时间, 31天跨度，时间区间参数必须成对出现）	2021-10-15 23:59:59
page	Int	Required		分页页码	1
page_size	Int	Required		分页数量(最大200)	20
响应JSON

参数名	数据类型	说明
code	Int	0 成功，其它值表示失败。
message	String	文本消息
data	Object	参见FuelRateListResp类型
FuelRateListResp数据结构

参数名	数据类型	可为空	说明
list	Object[]	False	燃油费率信息列表，数组元素定义参数 FuelRateItemResp
total	Int	False	列表总数
FuelRateItemResp数据结构

参数名	数据类型	可为空	说明
fls_rate	String	False	燃油费率
fls_begin_time	String	False	开始有效时间(北京时间)
fls_end_time	String	False	结束有效时间(北京时间)
sm_name	String	False	物流产品名称
sm_code	String	False	物流产品代码
