RESTFUL V1根据订单号获取单票订单信息
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
根据订单号获取单票订单信息
URLhttps://oms.goodcang.net/public_open/order/get_order_by_code
METHODPOST
请求JSON示例

1
2
3
{
    "order_code": "100057-141014-0001"
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
        {
            "ask": "Success",
            "message": "Success",
            "data": {
                "order_code": "G000-210420-0004",
                "reference_no": "RVG000-210310-0041",
                "platform": "OTHER",
                "order_status": "D",
                "shipping_method": "ZT-WULIU",
                "fba_shipment_id": "",
                "fba_shipment_id_create_time": "",
                "tracking_no": "",
                "warehouse_code": "USEA",
                "order_weight": "10.000",
                "order_desc": "",
                "date_create": "2021-04-20 19:40:28",
                "date_release": "2021-04-20 19:40:37",
                "date_shipping": "2021-04-21 15:18:50",
                "date_modify": "2021-04-21 15:20:08",
                "abnormal_problem_reason": "",
                "consignee_country_code": "US",
                "consignee_country_name": "美国",
                "consignee_state": "NJ",
                "consignee_city": "Dayton1",
                "consignee_district": "",
                "consignee_address1": "Docks 32 Road Korner Side 4",
                "consignee_address2": "NY",
                "consignee_address3": "",
                "consigne_zipcode": "18810",
                "consignee_doorplate": "110",
                "consignee_company": "ZT",
                "consignee_name": "WONG",
                "consignee_last_name": "Fen",
                "consignee_phone": "",
                "consignee_email": "",
                "LiftGate": 0,
                "age_detection": 0,
                "estimated_arrival_date": null,
                "estimated_arrival_time": "",
                "payment_time":"0000-00-00 00:00:00",
                "customer_package_requirement": 1,
                "items": [
                    {
                        "product_sku": "FISH65",
                        "fba_product_code": "",
                        "quantity": 10,
                        "transaction_id": "",
                        "item_id": ""
                    }
                ],
                "fee_details": {
                    "totalFee": 79.844,
                    "SHIPPING": 1,
                    "OPF": 30.88,
                    "FSC": 0,
                    "DT": 0,
                    "RSF": 0,
                    "OTF": 47.964,
                    "currency_code": "USD"
                },
                "orderBoxInfo": [
                    {
                        "box_no": "1-1",
                        "ob_length": 100,
                        "ob_width": 100,
                        "ob_height": 100,
                        "ob_weight": 11,
                        "ob_add_time": "2021-04-21 15:20:08",
                        "tracking_number": "",
                        "product_barcode": "G000-FISH65",
                        "order_code": "G000-210420-0004",
                        "ob_qty": 10
                    }
                ],
                "sn_info_list": [
                    {
                        "product_sku": "123123",
                        "serial_number": "3412341"
                    }
        ]
    }
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
order_code	String	Required	50	订单号	000010-200716-0006
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
data	Object	订单数据，参见OrderItemComposite。
OrderItemComposite

参数名	数据类型	说明
order_code	String	订单号
reference_no	String	客户参考号
platform	String	平台
order_status	String	订单状态 C:待发货审核
W:待发货
D:已发货
H:暂存
N:异常订单
P:问题件
X:废弃
abnormal_problem_reason	String	异常问题原因
shipping_method	String	配送方式
tracking_no	String	跟踪号
warehouse_code	String	配送仓库代码
wp_code	String	物理仓代码
order_weight	Float	订单重量
order_desc	String	订单说明
date_create	Datetime	创建时间
date_release	Datetime	审核时间
date_shipping	Datetime	出库时间
date_modify	Datetime	修改时间
fba_shipment_id	String	FBA Shipment ID FBA 类型订单必填
fba_shipment_id_create_time	String	FBA Shipment ID创建时间 FBA 类型订单必填
consignee_country_code	String	收件人国家二字码
consignee_country_name	String	收件人国家/地区
consignee_state	String	省
consignee_city	String	城市
consignee_district	String	区域
consignee_address1	String	地址1
consignee_address2	String	地址2
consignee_address3	String	地址3
consigne_zipcode	String	邮编
consignee_doorplate	String	门牌号
consignee_company	String	公司
consignee_name	String	收件人名
consignee_last_name	String	收件人姓
consignee_phone	String	收件人电话
consignee_email	String	收件人邮箱
age_detection	String	年龄检测服务
0 - 否
16 - 对应16岁
18 - 对应18岁
LiftGate	Int	LiftGate服务 0为否 1为是
items	Object[]	订单明细对象数组，元素结构参数 OrderLineItem。
fee_details	Object	订单费用对象，参见OrderFeeComposite。
orderBoxInfo	Object[]	一票多箱装箱明细（适用于一票多箱，或者FBA订单），数组元素参见OrderCartonItem。
sn_info_list	Object[]	订单SKU序列号列表，数组元素参见OrderSkuSnItem。
estimated_arrival_date	String	预计到货日期
estimated_arrival_time	String	到货时间段
payment_time	String	付款时间
sender_info	Object	发件人信息，参见SenderInfo。（仓库所在地为日本时适用，否则该参数忽略）
vat_change_info	Object	欧盟税改资料，参见VatChangeInfo。（非标准订单时，该参数将被忽略）
is_euro_label	Int	商品是否贴标。1是，0否
vas	Object	增值服务选项，参见对象 ValueAddedService。
is_warehouse_packing	Int	是否仓库装箱商品。1是，0否
truck_info	Object	卡派渠道物流信息，参见对象 TruckInfo。
(FBA订单适用) 物流产品为卡派渠道时有值。
property_label	String	平台模式：SFP
customer_package_requirement	Int	包材要求
1：纸箱
2：快递袋
3：气泡袋
4：环保袋
OrderLineItem

参数名	数据类型	说明
product_sku	String	SKU
quantity	Int	数量
transaction_id	String	ebay订单交易号
fba_product_code	String	fba商品编码
item_id	String	ebay订单商品编码
euro_terms_code	String	合规负责人编码
euro_terms_company	String	合规负责人公司名称
label_replacement_qty	int	内件货物总数量
FBA订单适用
product_declared_value	Float	申报价值（价值币种同仓库币种）
hs_code	String	海关编码
OrderFeeComposite

参数名	数据类型	说明
totalFee	Float	总费用
SHIPPING	Float	运输费
OPF	Float	操作费用
FSC	Float	燃油附加费
DT	Float	关税
RSF	Float	挂号
OTF	Float	其它费用
currency_code	String	币种
OrderCartonItem

参数名	数据类型	说明
box_no	String	箱号
box_mark	String	箱唛号
fba_box_mark	String	FBA箱唛号
ob_length	Float	长，单位CM
ob_width	Float	宽，单位CM
ob_height	Float	高，单位CM
ob_weight	Float	重量，单位KG
ob_add_time	String	创建时间
tracking_number	String	跟踪号
product_barcode	String	产品编码
order_code	String	订单号
ob_qty	Int	数量
SenderInfo

参数名	数据类型	是否必填	长度	说明
name	String	Optional	200	发件人姓名
phone	String	Optional	50	发件人电话
VatChangeInfo

参数名	数据类型	是否必填	长度	说明	示例
ioss_number	String	Optional	100	IOSS号码	
pid_number	String	Optional	100	PID号码	
recipient_eori	String	Optional	100	收件人EORI	
recipient_vat	String	Optional	100	收件人VAT	
shipper_eori	String	Optional	100	发件人EORI	
shipper_vat	String	Optional	100	发件人VAT	
shipper_company_name	String	Optional	100	发件人公司名称	
recipient_vat_country	String	Optional	2	收件人VAT注册国
参考获取国家/地区列表接口的 country_code 字段
            
GB
recipient_eori_country	String	Optional	2	收件人EORI号注册国
参考获取国家/地区列表接口的 country_code 字段
            
US
ValueAddedService

参数名	数据类型	是否必填	说明	示例
logistics_recommendation_option	Int	Optional	物流优选时效枚举选项
不使用此服务时传null。
使用物流优选时（该选项不为null），则warehouse_code, shippping_method为选填项，系统将根据优选结果自动选择 仓库与物流方式选项。
1：0-3 个工作日(不包括0)
2：3-6 个工作日(不包括3)
3：6 个工作日(不包括6)
4：时效最快
5：费用最省
1
label_replacement_option	Int	Optional	换标要求
可选项有：
1 - 外箱
2 - 内箱
当换标服务为 1:换标 时，不传默认为 1外箱
当换标服务为 0:不换标 时，该参数必须为null，或者不传。
1
OrderSkuSnItem

参数名	数据类型	说明
product_sku	String	商品SKU。
serial_number	String	序列号。
TruckInfo

参数名	数据类型	说明
reference_id	String	参考号
seller_name	String	店铺名称
fba_warehouse_code	String	FBA仓库代码



RESTFUL V1获取订单列表
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
该接口只能获取状态为待发货、已发货、异常订单、问题件、废弃的订单
URLhttps://oms.goodcang.net/public_open/order/get_order_list
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
{
    "page": 1,
    "pageSize": 10,
    "order_status": "D",
    "order_code_arr": [
        "G000-210420-0004",
        "G000-210420-0005"
    ]
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
{
    "ask": "Success",
    "message": "Success",
    "errCode": "",
    "data": [
        {
            "order_code": "G000-210420-0004",
            "reference_no": "RVG000-210310-0041",
            "platform": "OTHER",
            "order_status": "D",
            "shipping_method": "ZT-WULIU",
            "fba_shipment_id": "",
            "fba_shipment_id_create_time": "",
            "tracking_no": "",
            "warehouse_code": "USEA",
            "order_weight": 10,
            "order_desc": "",
            "date_create": "2021-04-20 19:40:28",
            "date_release": "2021-04-20 19:40:37",
            "date_shipping": "2021-04-21 15:18:50",
            "date_modify": "2021-04-21 15:20:08",
            "abnormal_problem_reason": "",
            "estimated_arrival_date": null,
            "estimated_arrival_time": "",
            "consignee_country_code": "US",
            "consignee_country_name": "美国",
            "consignee_state": "NJ",
            "consignee_city": "Dayton1",
            "consignee_district": "",
            "consignee_address1": "Corner Donakis  Road Suite 000",
            "consignee_address2": "NY",
            "consignee_address3": "",
            "consignee_zipcode": "18810",
            "consignee_doorplate": "",
            "consignee_company": null,
            "consignee_name": "Jim Mc",
            "consignee_last_name": "Mc",
            "consignee_phone": "",
            "consignee_email": "",
            "age_detection": 0,
            "LiftGate": 0,
            "items": [
                {
                    "product_sku": "FISH65",
                    "quantity": 10,
                    "transaction_id": "",
                    "item_id": "",
                    "fba_product_code": "",
                    "product_declared_value": "",
                    "hs_code": ""
                }
            ],
            "fee_details": {
                "totalFee": 79.844,
                "SHIPPING": 1,
                "OPF": 30.88,
                "OTF": 47.964,
                "currency_code": "USD"
            },
            "orderBoxInfo": [
                {
                    "order_code": "G000-210420-0004",
                    "box_no": "1-1",
                    "ob_length": "100.00",
                    "ob_width": "100.00",
                    "ob_height": "100.00",
                    "ob_weight": "11.00",
                    "ob_add_time": "2021-04-21 15:20:08",
                    "tracking_number": "",
                    "product_barcode": "G000-FISH65",
                    "ob_qty": 10
                }
            ],
            "currency_code": "USD",
            "is_warehouse_packing": 0,
            "truck_info": {
                "reference_id": null,
                "seller_name": null,
                "fba_warehouse_code": null
            },
            "property_label": "",
            "customer_package_requirement": 2
        }
    ],
    "count": 82
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
pageSize	Int	Required		每页数据长度，最大值100	10
page	Int	Required		当前页	1
order_code	String	Optional	50	订单号	000010-200716-0006
order_code_arr	String[]	Optional		订单号字符串数组	["00001606170001","00001606170002"]
shipping_method	String	Optional	32	物流产品代码	FEDEX-SMALLPARCEL
create_date_from	Datetime	Optional	datetime	订单创建开始时间， 格式YYYY-MM-DD HH:II:SS 订单号传值时，该参数无效	2020-07-20 01:00:00
create_date_to	Datetime	Optional	datetime	订单创建结束时间， 格式YYYY-MM-DD HH:II:SS 订单号传值时，该参数无效	2020-07-20 01:00:00
modify_date_from	Datetime	Optional	datetime	订单修改开始时间， 格式YYYY-MM-DD HH:II:SS 订单号传值时，该参数无效	2020-07-20 01:00:00
modify_date_to	Datetime	Optional	datetime	订单修改结束时间， 格式YYYY-MM-DD HH:II:SS 订单号传值时，该参数无效	2020-07-20 01:00:00
date_shipping_from	Datetime	Optional	datetime	订单出库开始时间， 格式YYYY-MM-DD HH:II:SS 订单号传值时，该参数无效	2020-07-20 01:00:00
date_shipping_to	Datetime	Optional	datetime	订单出库结束时间， 格式YYYY-MM-DD HH:II:SS 订单号传值时，该参数无效	2020-07-20 01:00:00
order_status	String	Optional	1	订单状态
W:待发货
D:已发货
N:异常订单
P:问题件
X:废弃
D
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
count	Int	总数量
data	Object[]	订单数据对象数组，数组元素结构参见OrderItemComposite。
OrderItemComposite

参数名	数据类型	说明
order_code	String	订单号
reference_no	String	客户参考号
platform	String	平台
order_status	String	订单状态 W:待发货
D:已发货
N:异常订单
P:问题件
X:废弃
abnormal_problem_reason	String	异常问题原因
shipping_method	String	配送方式
tracking_no	String	跟踪号
warehouse_code	String	配送仓库代码
wp_code	String	物理仓代码
order_weight	Float	订单重量
order_desc	String	订单说明
date_create	Datetime	创建时间
payment_time	Datetime	付款时间
date_release	Datetime	审核时间
date_shipping	Datetime	出库时间
date_modify	Datetime	修改时间
fba_shipment_id	String	FBA Shipment ID FBA 类型订单必填
fba_shipment_id_create_time	String	FBA Shipment ID创建时间 FBA 类型订单必填
consignee_country_code	String	收件人国家二字码
consignee_country_name	String	收件人国家/地区
consignee_state	String	省
consignee_city	String	城市
consignee_district	String	区域
consignee_address1	String	地址1
consignee_address2	String	地址2
consignee_address3	String	地址3
consignee_zipcode	String	邮编
consignee_doorplate	String	门牌号
consignee_company	String	公司
consignee_name	String	收件人名
consignee_last_name	String	收件人姓
consignee_phone	String	收件人电话
consignee_email	String	收件人邮箱
age_detection	Int	年龄检测服务
0 - 否
16 - 对应16岁
18 - 对应18岁
items	Object[]	订单明细对象数组，元素结构参数 OrderLineItem。
fee_details	Object	订单费用对象，参见OrderFeeComposite。
orderBoxInfo	Object[]	一票多箱装箱明细（适用于一票多箱，或者FBA订单），数组元素参见OrderCartonItem。
LiftGate	Int	LiftGate服务 0为否 1为是
estimated_arrival_date	String	预计到货日期
estimated_arrival_time	String	到货时间段
sender_info	Object	发件人信息，参见SenderInfo。（仓库所在地为日本时适用，否则该参数忽略）
vat_change_info	Object	欧盟税改资料，参见VatChangeInfo。（非标准订单时，该参数将被忽略）
vas	Object	增值服务选项，参见对象 ValueAddedService。
currency_code	string	仓库币种
is_warehouse_packing	Int	是否仓库装箱商品。1是，0否
truck_info	Object	卡派渠道物流信息，参见对象 TruckInfo。
(FBA订单适用) 物流产品为卡派渠道时有值。
property_label	String	平台模式
SFP
customer_package_requirement	Int	包材要求
1：纸箱
2：快递袋
3：气泡袋
4：环保袋
OrderLineItem

参数名	数据类型	说明
product_sku	String	SKU
fba_product_code	String	FBA商品编码
quantity	Int	数量
transaction_id	String	ebay订单交易号
item_id	String	ebay订单商品编码
label_replacement_qty	int	内件货物总数量
FBA订单适用
product_declared_value	Float	申报价值（价值币种同仓库币种）
hs_code	String	海关编码
OrderFeeComposite

参数名	数据类型	说明
totalFee	Float	总费用
SHIPPING	Float	运输费
OPF	Float	操作费用
FSC	Float	燃油附加费
DT	Float	关税
RSF	Float	挂号
OTF	Float	其它费用
currency_code	String	币种
OrderCartonItem

参数名	数据类型	说明
box_no	String	箱号
box_mark	String	箱唛号
fba_box_mark	String	FBA箱唛号
ob_length	Float	长，单位CM
ob_width	Float	宽，单位CM
ob_height	Float	高，单位CM
ob_weight	Float	重量，单位KG
ob_add_time	String	创建时间
tracking_number	String	跟踪号
product_barcode	String	产品编码
order_code	String	订单号
ob_qty	Int	数量
SenderInfo

参数名	数据类型	说明
name	String	发件人姓名
phone	String	发件人电话
VatChangeInfo

参数名	数据类型	说明
ioss_number	String	IOSS号码
pid_number	String	PID号码
recipient_eori	String	收件人EORI
recipient_vat	String	收件人VAT
shipper_eori	String	发件人EORI
shipper_vat	String	发件人VAT
shipper_company_name	String	发件人公司名称
recipient_vat_country	String	收件人VAT注册国
recipient_eori_country	String	收件人EORI号注册国
ValueAddedService

参数名	数据类型	说明	示例
logistics_recommendation_option	Int	物流优选时效枚举选项（不使用此服务时传null）。
1
使用物流优选时（该选项不为null），则warehouse_code, shippping_method为选填项，系统将根据优选结果自动选择 仓库与物流方式选项。	
1：0-3 个工作日(不包括0)	
2：3-6 个工作日(不包括3)	
3：6 个工作日(不包括6)	
TruckInfo

参数名	数据类型	说明
reference_id	String	参考号
seller_name	String	店铺名称
fba_warehouse_code	String	FBA仓库代码



RESTFUL V1获取草稿和暂存订单列表
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
说明：批量获取设置范围内的订单信息
URLhttps://oms.goodcang.net/public_open/order/get_draft_order_list
METHODPOST
请求JSON示例

1
2
3
4
5
{
    "pageSize": "1",
    "page": "1",
    "order_status": "C"
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
{
    "ask": "Success",
    "message": "",
    "errCode": "",
    "count": "962",
    "data": [
        {
            "order_code": "G296-190105-0013",
            "reference_no": "",
            "platform": "ALIEXPRESS",
            "order_status": "C",
            "shipping_method": "BGM",
            "tracking_no": null,
            "warehouse_code": "USEA",
            "order_weight": "0.0000",
            "order_desc": "",
            "date_create": "2019-01-05 18:38:47",
            "date_release": "2019-01-05 18:38:47",
            "date_shipping": "null",
            "date_modify": "2019-01-05 18:38:45",
            "consignee_country_code": "US",
            "consignee_country_name": "UNITED STATES",
            "consignee_state": "FL",
            "consignee_city": "Miami",
            "consignee_district": null,
            "consignee_address1": "248 5TH AVE W",
            "consignee_address2": "",
            "consignee_address3": "",
            "consignee_zipcode": "33178",
            "consignee_doorplate": "",
            "consignee_company": "纵腾",
            "consignee_name": "Katiuska",
            "consignee_last_name": "Mora",
            "consignee_phone": "+867868374933",
            "consignee_email": "",
            "age_detection": "0",
            "LiftGate": "0",
            "new_order_type": "0",
            "design_batch_status": "0",
            "fee_details": {
                "totalFee": 0,
                "SHIPPING": 0,
                "OPF": 0,
                "FSC": 0,
                "DT": 0,
                "RSF": 0,
                "OTF": 0,
                "currency_code": ""
            },
            "fba_shipment_id": "",
            "fba_shipment_id_create_time": "",
            "orderBoxInfo": [],
            "abnormal_problem_reason": "",
            "payment_time": "2021-10-22 13:59:54",
            "items": [
                {
                    "product_sku": "5656_BABY",
                    "quantity": "1",
                    "transaction_id": "",
                    "item_id": "",
                    "fba_product_code": ""
                }
            ],
            "is_warehouse_packing": 0,
            "truck_info": {
                "reference_id": "",
                "seller_name": "",
                "fba_warehouse_code": ""
            },
            "property_label": "",
            "customer_package_requirement": null
        }
    ],
    "request_id": "5F962FBD16668"
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
pageSize	Int	Required		每页数据长度，最大值100	10
page	Int	Required		当前页	1
order_code	String	Optional	50	订单号	000010-200716-0006
order_code_arr	String[]	Optional		多个订单号,数组格式	["00001606170001","00001606170002"]
shipping_method	String	Optional	32	物流产品代码	FEDEX-SMALLPARCEL
create_date_from	Datetime	Optional	datetime	订单创建开始时间， 格式YYYY-MM-DD HH:II:SS 订单号传值时，该参数无效	2020-07-20 01:00:00
create_date_to	Datetime	Optional	datetime	订单创建结束时间， 格式YYYY-MM-DD HH:II:SS 订单号传值时，该参数无效	2020-07-20 01:00:00
modify_date_from	Datetime	Optional	datetime	订单修改开始时间， 格式YYYY-MM-DD HH:II:SS 订单号传值时，该参数无效	2020-07-20 01:00:00
modify_date_to	Datetime	Optional	datetime	订单修改结束时间， 格式YYYY-MM-DD HH:II:SS 订单号传值时，该参数无效	2020-07-20 01:00:00
order_status	String	Required	1	订单状态
C:待发货审核
H:暂存
C
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
count	Int	总数量
data	Object	数据内容
data参数

参数名	数据类型	说明
order_code	String	订单号
reference_no	String	客户参考号
platform	String	平台
order_status	String	订单状态 C:待发货审核
H:暂存
abnormal_problem_reason	String	异常问题原因
shipping_method	String	配送方式
tracking_no	String	跟踪号
warehouse_code	String	配送仓库代码
order_weight	float	订单重量
order_desc	String	订单说明
date_create	Datetime	创建时间
payment_time	Datetime	付款时间
date_release	Datetime	审核时间
date_shipping	Datetime	出库时间
date_modify	Datetime	修改时间
fba_shipment_id	String	FBA Shipment ID FBA 类型订单必填
fba_shipment_id_create_time	String	FBA Shipment ID创建时间 FBA 类型订单必填
consignee_country_code	String	收件人国家二字码
consignee_country_name	String	收件人国家
consignee_state	String	省
consignee_city	String	城市
consignee_district	String	区域
consignee_address1	String	地址1
consignee_address2	String	地址2
consignee_address3	String	地址3
consignee_zipcode	String	邮编
consignee_doorplate	String	门牌号
consignee_company	String	公司
consignee_name	String	收件人名
consignee_last_name	String	收件人姓
consignee_phone	String	收件人电话
consignee_email	String	收件人邮箱
age_detection	String	年龄检测服务
0 - 否
16 - 对应16岁
18 - 对应18岁
items	Object[]	订单明细
fee_details	Object	订单费用
orderBoxInfo	Object	一票多箱装箱明细，一票一箱则返回空
LiftGate	Int	LiftGate服务 0为否 1为是
sender_info	Object	发件人信息，参见SenderInfo。（仓库所在地为日本时适用，否则该参数忽略）
vat_change_info	Object	欧盟税改资料，参见VatChangeInfo。（非标准订单时，该参数将被忽略）
vas	Object	增值服务选项，参见对象 ValueAddedService。
is_warehouse_packing	Int	是否仓库装箱商品。1是，0否
truck_info	Object	卡派渠道物流信息，参见对象 TruckInfo。
(FBA订单适用) 物流产品为卡派渠道时有值。
property_label	String	平台模式
SFP
customer_package_requirement	Int	包材要求
1：纸箱
2：快递袋
3：气泡袋
4：环保袋
items参数

参数名	数据类型	说明
product_sku	String	SKU
fba_product_code	String	FBA商品编码
quantity	Int	数量
transaction_id	String	ebay订单交易号
item_id	String	ebay订单商品编码
label_replacement_qty	int	内件货物总数量
FBA订单适用
product_declared_value	Float	申报价值(USD)
hs_code	String	海关编码
fee_details参数

参数名	数据类型	说明
totalFee	Float	总费用
SHIPPING	Float	运输费
OPF	Float	操作费用
FSC	Float	燃油附加费
DT	Float	关税
RSF	Float	挂号
OTF	Float	其它费用
currency_code	String	币种
orderBoxInfo参数

参数名	数据类型	说明
box_no	String	箱号
ob_length	Float	长，单位CM
ob_width	Float	宽，单位CM
ob_height	Float	高，单位CM
ob_weight	Float	重量，单位KG
ob_add_time	String	创建时间
tracking_number	String	跟踪号
product_barcode	String	产品编码
order_code	String	订单号
ob_qty	Int	数量
SenderInfo

参数名	数据类型	是否必填	长度	说明
name	String	Optional	200	发件人姓名
phone	String	Optional	50	发件人电话
VatChangeInfo

参数名	数据类型	是否必填	长度	说明	示例
ioss_number	String	Optional	100	IOSS号码	
pid_number	String	Optional	100	PID号码	
recipient_eori	String	Optional	100	收件人EORI	
recipient_vat	String	Optional	100	收件人VAT	
shipper_eori	String	Optional	100	发件人EORI	
shipper_vat	String	Optional	100	发件人VAT	
shipper_company_name	String	Optional	100	发件人公司名称	
recipient_vat_country	String	Optional	2	收件人VAT注册国
参考获取国家/地区列表接口的 country_code 字段
            
GB
recipient_eori_country	String	Optional	2	收件人EORI号注册国
参考获取国家/地区列表接口的 country_code 字段
            
US
ValueAddedService

参数名	数据类型	是否必填	说明	示例
logistics_recommendation_option	Int	Optional	物流优选时效枚举选项
不使用此服务时传null。
使用物流优选时（该选项不为null），则warehouse_code, shippping_method为选填项，系统将根据优选结果自动选择 仓库与物流方式选项。
1：0-3 个工作日(不包括0)
2：3-6 个工作日(不包括3)
3：6 个工作日(不包括6)
4：时效最快
5：费用最省
1
label_replacement_option	Int	Optional	换标要求
可选项有：
1 - 外箱
2 - 内箱
当换标服务为 1:换标 时，不传默认为 1外箱
当换标服务为 0:不换标 时，该参数必须为null，或者不传。
1
TruckInfo

参数名	数据类型	说明
reference_id	String	参考号
seller_name	String	店铺名称
fba_warehouse_code	String	FBA仓库代码




RESTFUL批量轨迹查询
这是RESTFUL WEB API，接入方式请参见GD开放平台(V2)接入指引。
URLhttps://oms.goodcang.net/public_open/order/batch_query_tracking_status
METHODPOST
请求JSON示例

1
2
3
4
{
      "value_list": ["code1", "code2", "code3"],
      "code_type": "order_code"
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
{
    "code": 0,
    "message": "success",
    "data": [
        {
            "order_code": "code1",
            "code": "MORKRM",
            "trajectory_information": [
                {
                    "tracking_number": "MR014111284RM",
                    "item": [
                        {
                                "utc_time": "2021-03-15 13:41:27",
                                "date_time": "2021-03-15 21:41:27",
                                "info": "Delivered",
                                "location": "LAKEWOOD,NJ,US",
                                "code": "TMS_FD",
                                "code_info": "派送完毕"
                         }
                    ]
                }
 
            ]
        }
    ]
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
value_list	String[]	Required		包含订单号的字符串列表(最多包含50个)	["G123456", "G321567"]
code_type	String	Required		value_list中字符串的业务类型枚举类型
"order_code": 订单号
"reference_no": 参考号
"tracking_number": 追踪号
order_code
响应JSON

参数名	数据类型	说明
code	Int	0 成功，其它值表示失败。
message	String	文本消息
data	Object[]	参见OrderTrackingComposite类型
OrderTrackingComposite数据结构

参数名	数据类型	可为空	说明
order_code	String	False	订单号
code	String	False	渠道名称
trajectory_information	Object[]	False	参见OrderTrajectoryInformationResp类型
OrderTrajectoryInformationResp类型

参数名	数据类型	可为空	说明
tracking_number	String	True	跟踪号
status_list	Object[]	True	轨迹信息,参见OrderTrackingItemComposite类型
OrderTrackingItemComposite数据结构

参数名	数据类型	可为空	说明
utc_time	Datetime	True	utc 时间 零时区
date_time	Datetime	True	北京时间
info	String	True	物流详细信息
location	String	True	站点信息
code	String	True	轨迹代码（映射内容参见下表「轨迹代码映射」）
code_info	String	True	轨迹结构化详情
注：code 和codeinfo 后续如有变更则邮件通知 增加推送接口：时间轨迹信息更新则推送
轨迹代码映射

TMS轨迹代码（新）	轨迹描述	备注	总原则
TMS_NTI	查无轨迹	查无轨迹	
TMS_OC	订单创建	订单创建，服务商收到订单信息	
TMS_AS	预上网	预上网	
TMS_PU	揽件完毕	服务商揽件完毕	当揽收节点重复出现时，系统需取时间节点最早出现的轨迹映射为揽收
TMS_IT	运输中	货物运输途中（如到达某网点，到达某分拨中心等）	
TMS_OD	派送中	货物到达目的地城市，准备派送给收方	
TMS_WPU	到达目的地	货物到达目的地城市，等待客户上门取件	
TMS_RT	退回寄放	退回给寄放	
TMS_EXCP	轨迹异常	轨迹异常（如货物无法投递，因服务商原因导致延迟等）	
TMS_FD	派送完毕	派送完毕（如妥投，货物放在门口等）	订单超过30个自然日，无签收轨迹，系统默认为签收。以订单预报时间为起始时间
TMS_DF	投递未遂	投递未遂（如客户不在家）	
TMS_UN	无法匹配	指对抓回的轨迹系统找不到相应的匹配关系	
TMS_NP	未变化	未变化	
TMS_YD	预签收	预签收	
