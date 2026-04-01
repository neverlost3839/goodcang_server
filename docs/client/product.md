RESTFUL V1获取系统品类
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
说明：获取系统中所有的商品品类信息，创建商品时需要填写 相应商品的3级类目
URLhttps://oms.goodcang.net/public_open/product/get_category
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
{
    "ask": "Success",
    "data": [
        {
            "category_id": 1,
            "category_level": 0,
            "category_name": "机械设备/测量检测设备及其零配件(NEW)",
            "category_name_en": "Mechanical, Testing Equipment & Accessories",
            "parent_category_id": 0
        },
        {
            "category_id": 2,
            "category_level": 1,
            "category_name": "机械设备/测量检测设备及其零配件(NEW)",
            "category_name_en": "Mechanical, Testing Equipment & Accessories",
            "parent_category_id": 1
        },
        {
            "category_id": 601563,
            "category_level": 2,
            "category_name": "机械设备/测量检测设备及其零配件(NEW)",
            "category_name_en": "Mechanical, Testing Equipment & Accessories",
            "parent_category_id": 2
        }
    ],
    "message": "Success"
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
无
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
data	Object[]	系统品类数据数组，数组元素对象说明参见下文CategoryItem。
CategoryItem

参数名	数据类型	说明
category_id	Int	品类ID
parent_category_id	Int	品类父ID
category_name	String	品类中文名
category_name_en	String	品类英文名
category_level	Int	品类级别


RESTFUL V1获取建议中文申报品名
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
说明：获取谷仓系统建议的中文申报品名，建议新建商品时在这些选项中选择。
如果无匹配的选项，可以反馈给我们的技术支持，我们会考虑将选项加入系统中。
同时，商户可以按规则自由输入中文申报品名内容。
URLhttps://oms.goodcang.net/public_open/product/get_declare_commodity_name_list
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
{
    "ask": "Success",
    "message": "Success",
    "data": {
        "declare_list": [" 一次成像照相机", "18英寸越野自行车", "20英寸越野自行车"]
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
data	Object	申报品名数据，参见DeclareNameListResp
DeclareNameListResp

参数名	数据类型	说明
declare_list	String[]	申报品名列表



RESTFUL V1获取建议材质
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
说明：获取谷仓系统建议的商品材质，建议新建商品时在这些选项中选择。
如果无匹配的选项，可以反馈给我们的技术支持，我们会考虑将选项加入系统中。
同时，商户可以按规则自由输入材质内容。
URLhttps://oms.goodcang.net/public_open/product/get_material_list
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
{
    "ask": "Success",
    "message": "Success",
    "data": {
        "material_list": [
            "金属",
            "金属+复合木+塑料"
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
data	Object	参见下文MaterialList。
MaterialList

参数名	数据类型	说明
material_list	String[]	材质列表
Copyright © 2026 海外仓, All Rights Reserved


RESTFUL V1获取商品列表
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
URLhttps://oms.goodcang.net/public_open/product/get_product_sku_list
METHODPOST
请求JSON示例

1
2
3
4
5
6
7
{
  "pageSize": 10,
  "page": 1,
  "product_sku": "",
  "product_update_time_from": "",
  "product_update_time_to": ""
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
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
{
    "ask": "Success",
    "message": "Success",
    "data": [
        {
            "product_sku": "SKU_123",
            "reference_no": "",
            "product_status": "S",
            "product_title_cn": "商品名称_Cres",
            "product_title_en": "cres_test",
            "product_weight": 5,
            "product_length": 1,
            "product_width": 2,
            "product_height": 3,
            "Product_real_weight": 0,
            "Product_real_length": 0,
            "Product_real_width": 0,
            "Product_real_height": 0,
            "contain_battery": 0,
            "type_of_goods": 0,
            "cat_id_level0": 0,
            "cat_id_level1": 0,
            "cat_id_level2": 601602,
            "cat_lang": "zh",
            "branded": 1,
            "product_brand": "SST",
            "product_model": "sss",
            "product_link": "http://example.com/product/123.html",
            "unit": "个/只/件/支/枝/把",
            "image_link": [
                "http://example.com/product/123.png",
                "http://example.com/product/456.png"
            ],
            "tax_info": [
                {
                    "exportable_country": "GB",
                    "product_declared_name": "WATERCOLOR PEN",
                    "tariff_calculation_value": null,
                    "currency": null,
                    "tariff_percentage": null,
                    "additional_tax_rate": "",
                    "vat_tax_rate": null,
                    "allow_save": "Y",
                    "head_type": "GC",
                    "declared_value": 2.5
                },
                {
                    "exportable_country": "US",
                    "product_declared_name": "",
                    "tariff_calculation_value": null,
                    "currency": null,
                    "tariff_percentage": null,
                    "additional_tax_rate": null,
                    "vat_tax_rate": null,
                    "allow_save": "Y",
                    "head_type": "GC",
                    "declared_value": 5.5
                }
            ],
            "export_country": [
                {
                    "country_code": "CN",
                    "declared_value": 2
                }
            ],
            "import_country": [],
            "IsIrregular": 0,
            "import_country_remark": "",
            "check_remark": "",
            "cargo_type": "M",
            "product_add_time": "2021-04-23 15:04:31",
            "product_modify_time": "2021-04-23 16:03:10",
            "is_collect_serial_number": false,
            "is_inbound_collect_serial_number": false,
            "sku_wrapper_type": 1,
            "remark":null,
 
        },
        {
            "product_sku": "SKU_456",
            "reference_no": "",
            "product_status": "S",
            "product_title_cn": "商品名称_Cres",
            "product_title_en": "cres_test",
            "product_weight": 5,
            "product_length": 1,
            "product_width": 2,
            "product_height": 3,
            "Product_real_weight": 0,
            "Product_real_length": 0,
            "Product_real_width": 0,
            "Product_real_height": 0,
            "contain_battery": 0,
            "type_of_goods": 0,
            "cat_id_level0": 0,
            "cat_id_level1": 0,
            "cat_id_level2": 601602,
            "cat_lang": "zh",
            "branded": 1,
            "product_brand": "SST",
            "product_model": "sss",
            "product_link": "http://example.com/product/456.html",
            "unit": "个/只/件/支/枝/把",
            "image_link": [
                "http://example.com/product/456.png",
                "http://example.com/product/456-2.jpg"
            ],
            "tax_info": [
                {
                    "exportable_country": "GB",
                    "product_declared_name": "WATERCOLOR PEN",
                    "tariff_calculation_value": null,
                    "currency": null,
                    "tariff_percentage": null,
                    "additional_tax_rate": "",
                    "vat_tax_rate": null,
                    "allow_save": "Y",
                    "head_type": "GC",
                    "declared_value": 2.5
                },
                {
                    "exportable_country": "US",
                    "product_declared_name": "",
                    "tariff_calculation_value": null,
                    "currency": null,
                    "tariff_percentage": null,
                    "additional_tax_rate": null,
                    "vat_tax_rate": null,
                    "allow_save": "Y",
                    "head_type": "GC",
                    "declared_value": 5.5
                }
            ],
            "export_country": [
                {
                    "country_code": "CN",
                    "declared_value": 2
                }
            ],
            "import_country": [],
            "IsIrregular": 0,
            "import_country_remark": "",
            "check_remark": "",
            "cargo_type": "M",
            "product_add_time": "2021-04-23 15:04:31",
            "product_modify_time": "2021-04-23 16:03:10",
            "is_collect_serial_number": false,
            "is_inbound_collect_serial_number": false,
            "sku_wrapper_type": 1,
            "remark":"备注",
        }
    ],
    "count": 13967
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
pageSize	Int	Required		每页显示的sku 数量	10
page	Int	Required		查询页数	1
product_sku	String	Optional	24	SKU
精确搜索匹配
AALING1
product_sku_arr	String[]	Optional		多个SKU,数组格式
精确搜索匹配
["EA14051211404212", "EA110"]
product_update_time_from	Date	Optional	datetime	修改开始时间 格式:Y-m-d H:i:s	2020-07-15 09:00:00
product_update_time_to	Date	Optional	datetime	修改结束时间 格式:Y-m-d H:i:s	2020-07-15 09:00:00
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
count	Int	总数量
data	Object[]	商品数据对象数组，数组元素结构参见 ProductItem。
ProductItem

参数名	数据类型	说明
product_sku	String	商品编码
reference_no	String	客户参考代码
product_status	String	产品状态
X:废弃
D:草稿
S:可用
W:审核中
R:审核不通过
product_title_cn	String	商品名称
product_title_en	String	商品英文名称
product_weight	Float	重量，单位KG
product_length	Float	长，单位CM
product_width	Float	宽，单位CM
product_height	Float	高，单位CM
contain_battery	Int	货物属性，默认为0
    0：普货
    1：含电池
    2：纯电池
    3：纺织品
    4：易碎品
    6：超标纯电池
    7：超标含电池
    
type_of_goods	Int	包裹类型。0包裹，1信封
branded	Int	是否品牌，0否，1是
product_brand	String	商品品牌
product_model	String	商品型号
cat_lang	String	品类语言，zh中文，en英文，默认为zh
cat_id_level0	Int	一级品类，参考getCategory
cat_id_level1	Int	二级品类，参考getCategory
cat_id_level2	Int	三级品类，参考getCategory
unit	String	成交单位
image_link	Object	商品图片链接,数组格式
product_link	String	商品链接
cargo_type	String	货型
Product_real_weight	Float	实收重量，单位KG
Product_real_length	Float	实收长，单位CM
Product_real_width	Float	实收宽，单位CM
Product_real_height	Float	实收高，单位CM
product_add_time	Date	添加时间
product_modify_time	Date	修改时间
tax_info	Object	商品关税信息
export_country	Object	出口国关税信息维护
import_country	Object	进口国清关信息维护
IsIrregular	Int	是否异形商品，0否 1是
check_remark	String	查验审核备注
import_country_remark	String	进口国备注
product_material	String	材质
product_function	String	用途
thirdparty_sku_mapping	String[]	映射编码列表
is_collect_serial_number	Bool	出库是否采集序列号，指仓库出库扫描时是否需采集商品序列号（SN码）信息。
如需要采集，请务必在序列号管理中提前维护商品的序列号信息
is_inbound_collect_serial_number	Bool	入库是否采集序列号，指仓库入库扫描时是否需采集商品序列号（SN码）信息。
如需要采集，请务必在序列号管理中提前维护商品的序列号信息
battery_info	Object	电池信息, 参见BatteryInfo对象
sku_wrapper_type	Int	SKU包装属性，默认预包装
1：预包装
2：销售包装
3：原包彩盒
remark	String	备注
export_country,import_country

参数名	数据类型	说明
country_code	String	国家简称
declared_value	String	申报价值
tax_info参数

参数名	数据类型	说明
exportable_country	String	可发国家
product_declared_name	String	申报品名
tariff_calculation_value	Float	关税计算值
currency	String	币种
tariff_percentage	Float	关税百分比
additional_tax_rate	String	附加关税税率
vat_tax_rate	Float	VAT税率
allow_save	String	海外仓是否可存，是："Y"，否："N"
head_type	String	头程类型;谷仓头程"GC",卖家直发："MJ"
declared_value	String	申报价值
BatteryInfo参数

参数名	数据类型	说明
battery_model	String	电池型号
un_code	String	UN编码
battery_power_range	Integer	电池功率范围（WH） 1：101WH~300WH 2：>300WH
battery_power	Integer	电池功率（WH）
msds_file_url	String	MSDS报告证书链接
BatteryInfo参数

参数名	数据类型	说明
battery_model	String	电池型号
un_code	String	UN编码
battery_power_range	Integer	电池功率范围（WH） 1：101WH~300WH 2：>300WH
battery_power	Integer	电池功率（WH）
msds_file_url	String	MSDS报告证书链接



RESTFUL获取序列号列表
这是RESTFUL WEB API，接入方式请参见GD开放平台(V2)接入指引。
URLhttps://oms.goodcang.net/public_open/product/serial_number_list
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
9
10
{
    "code_type": 2,
    "status": null,
    "code_value": null,
    "time_type": 1,
    "page": 1,
    "pageSize": 100,
    "start_time": "2022-01-10 12:09:12",
    "end_time": "2022-03-10 12:09:12"
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
    "code": 0,
    "message": "success",
    "data": {
        "list": [
            {
                "order_code": "",
                "product_sku": "MAMAMAMAMAMA002",
                "serial_number": "1231231231",
                "status_text": "已废弃",
                "create_time": "2022-02-21 19:20:06",
                "update_time": "2022-02-21 20:42:30",
                "ship_time": "",
                "discard_time": "2022-02-21 20:42:30",
                "inbound_code": "",
                "data_code": ""
            }
        ],
        "total": 33
    }
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
status	Int	Optional		查询类型，枚举值
    0: 待收货
    1: 待出库
    2: 已出库
    3: 已废弃
1
code_type	Int	Optional		查询类型，枚举值
    1: 序列号
    2: 商品编码
    3: 订单号
    4: 序列号集成码
    5: 入库单号
1
code_value	String	Optional		查询值	""
time_type	Int	Optional		查询时间类型，枚举值
    1: 创建时间
    3: 出库时间
    4: 废弃时间
1
start_time	String	Optional	50	时间类型
开始时间和结束时间必须成对出现，且结束时间晚于开始时间	
end_time	String	Optional	50	时间类型
开始时间和结束时间必须成对出现，且结束时间晚于开始时间	
响应JSON

参数名	数据类型	说明
code	Int	0 成功，其它值表示失败。
message	String	文本消息
data	Object	参见 SerialNumberDataResp类型。
SerialNumberDataResp类型

list	Object[]	序列信息数组，数组元素参见SerialNumberListItem类型。
total	Int	总数
SerialNumberListItem类型

order_code	String	订单号
product_sku	String	商品编码
serial_number	String	商品编码
status_text	String	状态
create_time	String	创建时间
update_time	String	更新时间
ship_time	String	出库时间
discard_time	String	废弃时间
data_code	String	序列号集成码
inbound_code	String	入库单号
