RESTFUL V1进出口商列表
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
获取进出口商信息，用于创建英国仓、法国仓、德国仓的入库单
URLhttps://oms.goodcang.net/public_open/inbound_order/get_vat_list
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
{
    "ask": "Success",
    "message": "",
    "data": [
        {
            "cv_id": "102",
            "vat_type": "2",
            "company_name": "525252",
            "vat_number": "",
            "exemption_number": "",
            "eori": "",
            "warehouse_code": "",
            "cv_contacter": "1222222222",
            "cv_contact_phone": "19696969696",
            "vat_email": "696@qq.com",
            "cv_business_address": "456546",
            "cv_status": "1",
            "cv_create_time": "2019-01-20 09:42:20",
            "auditing_time": "0000-00-00 00:00:00",
            "cv_update_time": "2019-03-22 16:51:53",
            "importer_company_licence": {
                "file_type": "base64",
                "file": "jpg"
            },
            "gst_certificate": {
                "file_type": "base64",
                "file": "jpeg"
            }
        }
    ]
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
page_size	Int	Optional		每页数据长度，最大值为200	10
page	Int	Optional		当前页	1
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
data	Object[]	进口商信息数组，数组元素参见VatItem类型。
VatItem参数

参数名	数据类型	说明
vat_type	Int	进出口商,1：进口商,2：出口商
company_name	String	公司名称
vat_number	String	增值税号
exemption_number	String	增值税豁免号
eori	String	EORI
warhouse_code	String	海外仓仓库代码
cv_contacter	String	联系人
cv_contact_phone	String	联系人电话
vat_email	String	联系人邮箱
cv_business_address	String	公司主要营业地址
importer_company_licence	Object	营业执照/商业登记书文件，参见VatFile类型。
gst_certificate	Object	增值税证明文件，参见VatFile类型。
cv_status	String	0已废弃 1待审核 2审核通过 3审核驳回
cv_create_time	Datetime	创建时间 格式:Y-m-d H:i:s
auditing_time	Datetime	审核时间 格式:Y-m-d H:i:s
cv_update_time	Datetime	更新时间 格式:Y-m-d H:i:s
cv_id	Int	进/出口商编码
VatFile

参数名	数据类型	说明
file_url	String	对应文件的URL访问地址（完整URL路径）
file_type	String	返回文件类型



RESTFUL V1获取物流产品与目的仓中转仓
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
说明：获取中转入库单的中转物流产品，和对应的目的仓、中转仓及服务方式
URLhttps://oms.goodcang.net/public_open/inbound_order/get_smcode_twc_to_warehouse
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
{
    "ask": "Success",
    "message": "Success",
    "data": {
        "AIR": [
            {
                "sm_code": "xxqe",
                "sm_code_name": "深圳治治",
                "twc_to_warehouse": [
                    {
                        "warehouse_code": "USEA",
                        "warehouse_name": "美东仓库"
                    }
                ]
            },
            {
                "sm_code": "cccc",
                "sm_code_name": "田氏专运-空运",
                "twc_to_warehouse": [
                    {
                        "transit_warehouse_code": "wh001",
                        "transit_warehouse_name": "深圳仓库",
                        "warehouse_code": "USEA",
                        "warehouse_name": "美东仓库"
                    },
                    {
                        "transit_warehouse_code": "wh001",
                        "transit_warehouse_name": "深圳仓库",
                        "warehouse_code": "USWE",
                        "warehouse_name": "美西仓库"
                    }
                ]
            }
        ],
        "LCL": [
            {
                "sm_code": "aaa",
                "sm_code_name": "田氏专运-海运散货",
                "twc_to_warehouse": [
                    {
                        "transit_warehouse_code": "wh001",
                        "transit_warehouse_name": "深圳仓库",
                        "warehouse_code": "USEA",
                        "warehouse_name": "美东仓库"
                    }
                ]
            },
            {
                "sm_code": "werw",
                "sm_code_name": "捷克谷仓海运散货",
                "twc_to_warehouse": [
                    {
                        "transit_warehouse_code": "wh001",
                        "transit_warehouse_name": "深圳仓库",
                        "warehouse_code": "USEA",
                        "warehouse_name": "美东仓库"
                    }
                ]
            }
        ],
        "EXPRESS": [
            {
                "sm_code": "dddd",
                "sm_code_name": "田氏专运-快递",
                "twc_to_warehouse": [
                    {
                        "transit_warehouse_code": "wh001",
                        "transit_warehouse_name": "深圳仓库",
                        "warehouse_code": "USEA",
                        "warehouse_name": "美东仓库"
                    },
                    {
                        "transit_warehouse_code": "wh001",
                        "transit_warehouse_name": "深圳仓库",
                        "warehouse_code": "USWE",
                        "warehouse_name": "美西仓库"
                    }
                ]
            }
        ],
        "FCL": [
            {
                "sm_code": "abc002",
                "sm_code_name": "E美国UPS蓝单5000（同行）",
                "twc_to_warehouse": [
                    {
                        "warehouse_code": "USEA",
                        "warehouse_name": "美东仓库"
                    },
                    {
                        "warehouse_code": "AU",
                        "warehouse_name": "澳洲仓库"
                    },
                    {
                        "warehouse_code": "USSC",
                        "warehouse_name": "美南仓库"
                    }
                ]
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
data	Object	运输方式对象，参见 InboundOrderDelivery
InboundOrderDelivery

参数名	数据类型	说明
AIR	Object[]	空运服务方式，对象数组，参见 InboundOrderDeliveryItem。
LCL	Object[]	海运散货服务方式，对象数组，参见 InboundOrderDeliveryItem。
EXPRESS	Object[]	快递服务方式，对象数组，参见 InboundOrderDeliveryItem。
InboundOrderDeliveryItem

参数名	数据类型	说明
sm_code	String	物流产品
sm_code_name	String	物流产品名称
twc_to_warehouse	Object[]	物流产品绑定中转仓目的仓对象数组，参见 InboundOrderDeliveryWarehouseItem。
InboundOrderDeliveryWarehouseItem

warehouse_code	String	目的仓代码
warehouse_name	String	目的仓名称
transit_warehouse_code	String	中转仓代码
transit_warehouse_name	String	中转仓名称



RESTFUL V1获取入库单列表
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
说明：获取入库单列表
URLhttps://oms.goodcang.net/public_open/inbound_order/get_grn_list
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
11
12
13
{
    "page_size": 100,
    "page": 1,
    "receiving_code_arr": [
        "RVG296-190117-0005",
        "RVG296-190116-0060"
    ],
    "create_date_from": "2019-01-06 00:00:00",
    "create_date_to": "2019-01-16 23:59:59",
    "modify_date_from": "2019-01-06 00:00:00",
    "modify_date_to": "2019-01-16 23:59:59",
    "is_rollover":1
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
{
    "ask": "Success",
    "count": 2,
    "data": [
        {
            "box_total_count": 1,
            "create_at": "2021-04-30 17:59:08",
            "overseas_box_total": null,
            "overseas_sku_total": null,
            "receiving_code": "RVG880-210430-0005",
            "receiving_shipping_type": 1,
            "receiving_status": 0,
            "reference_no": "test20210001",
            "sku_total_count": 100,
            "sm_code": "aaa",
            "tracking_number": null,
            "transit_type": 3,
            "transit_warehouse_code": "wh001",
            "update_at": null,
            "remark": null,
            "warehouse_code": "USEA",
            "customs_docs_status": "4",
            "is_rollover":1,
            "track_status":"揽收"
        },
        {
            "box_total_count": 4,
            "create_at": "2021-04-13 15:01:06",
            "overseas_box_total": 4,
            "overseas_sku_total": 44,
            "receiving_code": "RVG880-210413-0032",
            "receiving_shipping_type": 4,
            "receiving_status": 10,
            "reference_no": null,
            "sku_total_count": 44,
            "sm_code": "",
            "tracking_number": "7774",
            "transit_type": 3,
            "transit_warehouse_code": "wh001",
            "update_at": "2021-04-13 15:40:05",
            "remark": null,
            "warehouse_code": "USEA",
            "customs_docs_status": "4",
            "is_rollover":1,
            "track_status":"揽收"
        }
    ],
    "message": "Success"
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
page_size	Int	Required		每页数据长度，最大值为100	10
page	Int	Required		当前页	1
receiving_code_arr	String[]	Optional		多个入库单号,数组格式,最多100	["RVG296-190117-0005", "RVG296-190116-0060"]
create_date_from	Date	Optional	datetime	创建开始日期	2020-07-07 00:00:00
create_date_to	Date	Optional	datetime	创建结束日期	2020-07-07 23:59:59
modify_date_from	Date	Optional	datetime	修改开始时间	2020-07-07 23:59:59
modify_date_to	Date	Optional	datetime	修改结束时间	2020-07-07 23:59:59
is_rollover	Int	Optional		是否仓库装箱商品：0否，1是	1
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
count	Int	总数量
data	Object[]	入库单信息数组，参见InboundOrderItem类型。
InboundOrderItem

参数名	数据类型	说明
receiving_code	String	入库单号
reference_no	String	客户参考号
transit_type	Int	入库单类型
0标准入库单
3中转入库单
5FBA入库单
sm_code	String	服务方式(物流产品代码)
receiving_status	Int	入库单状态
0草稿
1待审核
2审核不通过
3中转仓待签收
4中转仓待收货
5中转仓待配货
6中转仓待发货
7海外仓在途
8海外仓收货中
9海外仓收货完成
10海外仓上架完成
100废弃
                                    
receiving_shipping_type	Int	货运方式
0空运
1海运散货
2快递
3铁运整柜
4海运整柜
5铁运散货
create_at	Date	创建日期
update_at	Date	修改日期
warehouse_code	String	海外仓仓库编码
box_total_count	Int	预报箱数
sku_total_count	Int	预报sku件数
overseas_box_total	Int	海外仓入库端收货总箱数
overseas_sku_total	Int	海外目的仓收货总件数
tracking_number	String	跟踪号
transit_warehouse_code	String	国内中转仓库代码
wp_code	String	物理仓编码
remark	String	备注
customs_docs_status	int	报关资料上传状态
0无需上传
1未上传
2已上传
is_rollover	Int	是否仓库装箱商品
0否
1是
track_status	String	最后中转运输轨迹状态名称
declaration_examine	int	报关资料审核状态
1审核通过
2审核驳回
3待审核
4待上传



RESTFUL V1获取入库单明细
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
说明：获取入库单明细
URLhttps://oms.goodcang.net/public_open/inbound_order/get_grn_detail
METHODPOST
请求JSON示例

1
2
3
{
    "receiving_code": "RVG296-180906-0001"
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
{
    "ask": "Success",
    "message": "",
    "Error": null,
    "data": {
        "receiving_code": "RV000012-150716-0001",
        "receiving_shipping_type": 1,
        "transit_type": 3,
        "sm_code": 141,
        "reference_no": "",
        "value_added_service": [
            "world_ease",
            "origin_crt",
            "fumigation"
        ],
        "receiving_status": 10,
        "weight": 125.64,
        "volume": 9.78,
        "receiving_desc": "",
        "create_at": "2014-10-14 00:53:57",
        "update_at": "2014-10-14 00:54:13",
        "warehouse_code": "USEA",
        "box_total_count ": 1,
        "sku_total_count ": 2,
        "tracking_number": "987465145",
        "customs_type": 1,
        "pickup_form ": 1,
        "clearance_service ": 1,
        "export_company ": 50,
        "import_company ": 54,
        "collecting_service ": 1,
        "transit_warehouse_code ": "CZ",
        "transit_box_total ": 1,
        "eta_date ": "2014-10-14 00:54:13",
        "gc_putaway_time": "2020-07-27 14:01:45",
        "collecting_address ": {
            "ca_first_name ": "张",
            "ca_last_name ": "海威",
            "ca_contact_phone ": "13632806874",
            "ca_state ": "广东省",
            "ca_city": "深圳市",
            "ca_country_code": "CN",
            "ca_zipcode ": "518000",
            "ca_address1 ": "民治地铁向南商业大厦",
            "ca_address2": ""
        },
        "transfer_detail": [
            {
                "box_no": "RV000012-150716-0001-1",
                "product_sku": "18005001",
                "transit_pre_count ": 10
            }
        ],
        "overseas_detail": [
            {
                "box_no": "RV000012-150716-0001-1",
                "fba_product_code": "18005001",
                "overseas_pre_count ": 10,
                "overseas_shelves_count ": 10,
                "sn_list": [
                    {
                        "data_code": "DATA_CODE",
                        "sn_item_list": ["SN1", "SN2"]
                    }
                ]
            }
        ]
    }
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
receiving_code	String	Required	255	入库单号	RV000010-200707-0001
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
data	Object	入库单详情信息，参见InboundOrderDetails类型
InboundOrderDetails

参数名	数据类型	说明
receiving_code	String	入库单号
receiving_shipping_type	Int	货运方式 0：空运, 1：海运散货, 2：快递, 3：铁运整柜, 4：海运整柜, 5：铁运散货
transit_type	Int	0:标准入库单 3-中转入库单 5-FBA入库单
sm_code	String	FMS服务方式(物流产品代码)
reference_no	String	客户参考号
value_added_service	Object	增值服务:world_ease(worldease服务) origin_crt(产地证 ) fumigation(熏蒸 )
receiving_status	Int	入库单状态
0草稿
1待审核
2审核不通过
3中转仓待签收
4中转仓待收货
5中转仓待配货
6中转仓待发货
7海外仓在途
8海外仓收货中
9海外仓收货完成
10海外仓上架完成
100废弃
weight	Decimal(10,2)	预报重量(kg)
最多保留2位小数
volume	Decimal(10,2)	预报体积(立方米)
最多保留2位小数
receiving_desc	String	备注
create_at	Datetime	创建日期
update_at	Datetime	修改日期
warehouse_code	String	海外目的仓仓库代码
box_total_count	Int	预报箱数
sku_total_count	Int	预报sku件数
customs_type	Int	报关项,0:EDI报关,1:委托报关,2:报关自理
pickup_form	Int	提单类型,0:电放;1:正本
clearance_service	Int	是否自有税号清关,0:否,1:是
export_company	Int	出口商id
import_company	Int	进口商id
collecting_service	Int	揽收服务(送货方式),0:自送货物,1:上门提货
collecting_address	Object[]	揽收资料,当collection_service为1时必填
transit_warehouse_code	String	中转仓仓库代码
transit_box_total	Int	中转仓收货总箱数
tracking_number	String	跟踪号
eta_date	Datetime	预计到达时间
transfer_detail	Object[]	中转入库明细
overseas_detail	Object[]	海外仓入库明细
gc_putaway_time	Datetime	上架时间
wp_code	String	物理仓仓库编码
is_delay	Int	是否递延,0:否,1:是
is_rollover	Int	是否仓库装箱商品, 0:否,1:是
booking_cabin_no	String	订舱单号
tax_rebate_data_url	String	退税资料url
customers_send_info	Object	客户自送信息对象
- 参见 CustomersSendInfo
- 当transit_type=3（中转入库单） 并且 collecting_service=0（自送货物） 时，存在
collecting_address参数

参数名	数据类型	说明
ca_first_name	String	揽收联系人-名
ca_last_name	String	揽收联系人-姓
ca_contact_phone	String	揽收联系人电话
ca_state	String	揽收地址州/省份
ca_city	String	揽收地址城市
ca_country_code	String	揽收地址国家
ca_zipcode	String	揽收地址邮编
ca_address1	String	揽收地址1
ca_address2	String	揽收地址2
transfer_detai参数

参数名	数据类型	说明
box_no	Int	箱号
product_sku	String	SKU
transit_pre_count	Int	中转预报数量
transit_receiving_count	Int	中转收货数量
overseas_detail参数

参数名	数据类型	说明
box_no	Int	箱号
reference_box_no	String	箱唛参考号(适用于自发入库单、FBA入库单)
product_sku	String	SKU
fba_product_code	String	fba商品编码
overseas_pre_count	Int	海外仓预报数量
overseas_shelves_count	Int	海外端上架数量
sn_list	Int	详见SnListItem类型
SnListItem类型

参数名	数据类型	说明
data_code	String	序列号集成码
sn_item_list	String[]	序列号列表
CustomersSendInfo 对象

参数名	数据类型	可空	说明
arrive_transfer_warehouse_time	Datetime	否	预计到达中转仓时间
company_name	String	是	快递公司名称
delivery_code	String	是	快递单号
注：多个快递单号用英文逗号隔开
plate_no	String	是	车牌号。
driver_name	String	是	司机姓名
driver_phone	String	是	司机电话




RESTFUL V1获取上架批次
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
说明：获取上架批次
URLhttps://oms.goodcang.net/public_open/inbound_order/get_batch
METHODPOST
请求JSON示例

1
2
3
{
    "receiving_code": "RVG296-190222-0001"
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
{
    "ask": "Success",
    "message": "Success",
    "data": [
        {
            "receiving_code": "RVG296-190222-0001",
            "receiving_status": "S",
            "product_sku": "123SDF",
            "quantity": "17",
            "putaway_time": "2019-03-04 21:51:17",
            "inventory_type": 1,
            "shelf_lift": 1,
            "shelf_lift_day": 30,
            "shelf_life_list": [
                {
                    "expiration_date": "2022-05-19",
                    "manufacture_date": "2022-04-19",
                    "rbd_putaway_qty": 100
                }
            ]
        },
        {
            "receiving_code": "RVG296-190222-0001",
            "receiving_status": "S",
            "product_sku": "123456789012345678901234",
            "quantity": "4",
            "putaway_time": "2019-03-04 21:51:17",
            "inventory_type": 1,
            "shelf_lift": 1,
            "shelf_lift_day": 30,
            "shelf_life_list": [
                {
                    "expiration_date": "2022-05-19",
                    "manufacture_date": "2022-04-19",
                    "rbd_putaway_qty": 100
                }
            ]
        },
        {
            "receiving_code": "RVG296-190222-0001",
            "receiving_status": "S",
            "product_sku": "SKU20180807001",
            "quantity": "10",
            "putaway_time": "2019-03-04 21:51:17",
            "inventory_type": 1,
            "shelf_lift": 1,
            "shelf_lift_day": 30,
            "shelf_life_list": [
                {
                    "expiration_date": "2022-05-19",
                    "manufacture_date": "2022-04-19",
                    "rbd_putaway_qty": 100
                }
            ]
        },
        {
            "receiving_code": "RVG296-190222-0001",
            "receiving_status": "S",
            "product_sku": "ABCDEFGHIJKLMNOPQR123456",
            "quantity": "8",
            "putaway_time": "2019-03-04 21:51:17",
            "inventory_type": 1,
            "shelf_lift": 1,
            "shelf_lift_day": 30,
            "shelf_life_list": [
                {
                    "expiration_date": "2022-05-19",
                    "manufacture_date": "2022-04-19",
                    "rbd_putaway_qty": 100
                }
            ]
        }
    ]
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
receiving_code	String	Required	255	入库单号	RV000010-200707-0001
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
data	Object[]	入库单上架批次信息数组，数组元素参见InboundOrderShelfBatchItem类型。/td>
InboundOrderShelfBatchItem

参数名	数据类型	说明
receiving_code	String	入库单号
receiving_status	Int	入库单状态
0草稿
1待审核
2审核不通过
3中转仓待签收
4中转仓待收货
5中转仓待配货
6中转仓待发货
7海外仓在途
8海外仓收货中
9海外仓收货完成
10海外仓上架完成
100废弃
product_sku	String	商品编码
quantity	Int	上架数量
putaway_time	Date	上架时间
inventory_type	Int	库存类型
1良品
2不良品
shelf_lift	Int	是否有效期管理(0.否, 1.是)
shelf_lift_day	Int	有效期天数
shelf_life_list	Object[]	效期实收明细，参见 shelf_life_list
shelf_life_list参数

参数名	数据类型	说明
manufacture_date	String	生产日期, 格式: 2020-01-01
expiration_date	String	过期日期, 格式: 2020-12-01
rbd_putaway_qty	Int	上架数量



RESTFUL V1获取收货批次
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
说明：获取收货批次
URLhttps://oms.goodcang.net/public_open/inbound_order/get_receipt_batch
METHODPOST
请求JSON示例

1
2
3
{
    "receiving_code": "RVG296-190222-0001"
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
{
    "ask": "Success",
    "message": "Success",
    "transit_type": 0,
    "receiving_status": "10",
    "data": {
        "gc_receiving_data": [
            {
                "receiving_code": "RVG296-190222-0001",
                "box_no": "RVG296-190222-0001-1",
                "product_sku": "123SDF",
                "received_qty": "0",
                "received_time": "2019-02-22 09:38:59",
                "product_weight": "4.000",
                "product_length": "5.00",
                "product_width": "6.00",
                "product_height": "7.00",
                "quantity": "3"
            },
            {
                "receiving_code": "RVG296-190222-0001",
                "box_no": "RVG296-190222-0001-1",
                "product_sku": "123SDF",
                "received_qty": "0",
                "received_time": "2019-02-22 09:48:07",
                "product_weight": "4.000",
                "product_length": "5.00",
                "product_width": "6.00",
                "product_height": "7.00",
                "quantity": "3"
            }
        ],
        "transit_data": [
            {
                "receiving_code": "RVG296-190222-0001",
                "box_no": "RVG296-190222-0001-1",
                "quantity": "3",
                "received_qty": "3",
                "product_sku": "123SDF",
                "product_weight": "4.000",
                "product_length": "5.00",
                "product_width": "3.00",
                "product_height": "3.00"
            }
        ],
        "transit_box_data": [
            {
                "receiving_code": "RVG296-190222-0001",
                "box_no": "RVG296-190222-0001-1",
                "box_weight": "8.000",
                "box_length": "5.00",
                "box_width": "4.00",
                "box_height": "3.00"
            }
        ],
        "receiving_status": 5,
        "transit_type": 3
    }
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
receiving_code	String	Required	255	入库单号	RV000010-200707-0001
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
data	Object	入库单收货批次信息，参见ReceiptBatchResp类型
ReceiptBatchResp

参数名	数据类型	说明
transit_type	Int	入库单类型0:标准入库单 3-中转入库单 5-FBA入库单
transit_data	Object[]	中转仓收货批次(商品)，参见transit_data类型
transit_box_data	Object[]	中转仓收货批次(箱子)，参见transit_box_data类型
gc_receiving_data	Object[]	尾程仓收货批次，参见gc_receiving_data类型
receiving_status	Int	入库单状态
0草稿
1待审核
2审核不通过
3中转仓待签收
4中转仓待收货
5中转仓待配货
6中转仓待发货
7海外仓在途
8海外仓收货中
9海外仓收货完成
10海外仓上架完成
100废弃
transit_data参数

参数名	数据类型	说明
receiving_code	String	入库单号
box_no	String	入库单箱号
quantity	Int	预报数量
received_qty	Int	收货数量
product_sku	String	商品编码
product_weight	Float	商品重量，单位KG
product_length	Float	商品长度，单位CM
product_width	Float	商品宽度，单位CM
product_height	Float	商品高度，单位CM
transit_box_data参数

参数名	数据类型	说明
receiving_code	String	入库单号
box_no	String	入库单箱号
box_weight	Float	箱子重量，单位KG
box_length	Float	箱子长度，单位CM
box_width	Float	箱子宽度，单位CM
box_height	Float	箱子高度，单位CM
gc_receiving_data参数

参数名	数据类型	说明
receiving_code	String	入库单号
box_no	String	入库单箱号
quantity	Int	预报数量
received_qty	Int	收货数量
product_sku	String	商品编码
product_weight	Float	商品重量，单位KG
product_length	Float	商品长度，单位CM
product_width	Float	商品宽度，单位CM
product_height	Float	商品高度，单位CM
product_height	Float	商品高度，单位CM



RESTFUL V1获取车型
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
获取入库单适用的车型数据列表
URLhttps://oms.goodcang.net/public_open/inbound_order/cars_model
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
{
    "ask": "Success",
    "message": "Success",
    "data": {
        "car_model_name": "",
        "car_model_code": ""
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
data	Object	返回结果
response data参数

参数名	数据类型	说明
car_model_name	String	车型名称
car_model_code	String	车型代码




RESTFUL V1获取清关文件上传状态
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
说明：获取清关文件上传状态(配合接口 uploadClearanceDocument使用,当uploadClearanceDocument上传成功,5分钟后再使用此接口判断对应的入库单上传清关文件是否成功)
URLhttps://oms.goodcang.net/public_open/inbound_order/get_clearance_document
METHODPOST
请求JSON示例

1
2
3
4
5
6
{
    "receiving_list": [
        "RV000010-201010-00001",
        "RV000010-201010-00002"
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
{
    "ask": "Success",
    "message": "Success",
    "data": [
        {
            "receiving_code": "RV000010-201010-00001",
            "file_status": 2
        },
        {
            "receiving_code": "RV000010-201010-00002",
            "file_status": 2
        }
    ]
}
请求JSON

名称	参数	数据类型	是否必填	最大数据长度	说明	示例
入库单号数组	receiving_list	String[]	Required		请输入需要上传资料的入库单,否则上传不成功	["RV000010-201010-00001","RV000010-201010-00002"]
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
data	Object[]	清关文件数组，数组元素参见ClearanceDocumentListItem类型
ClearanceDocumentListItem

参数名	数据类型	说明
receiving_code	String	入库单号
file_status	Int	状态:1 未上传 ，2 已上传
