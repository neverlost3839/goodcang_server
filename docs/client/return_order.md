RESTFUL V1退货单查询
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
URLhttps://oms.goodcang.net/public_open/return_order/search
METHODPOST
请求JSON示例

1
2
3
4
{
    "reference_no": "fdzxcv4654132",
    "asroCodes": "RG296-170914-0013"
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
{
    "ask": "Success",
    "message": "Success",
    "data": [
        {
            "asro_code": "RG296-170914-0013",
            "order_code": "G296-170914-0002",
            "reference_no": "fdzxcv4654132",
            "asro_status": "4",
            "cass_type": "1",
            "asro_add_time": "2017-09-14 17:07:41",
            "asro_audit_time": "2017-09-14 17:08:08",
            "asro_putaway_time": "0000-00-00 00:00:00",
            "warehouse_code": "USEA",
            "sm_type": "0",
            "collect_warehouse_code": "",
            "service_type": 1,
            "is_transit": 2,
            "tracking_no": "787722279346",
            "asro_reason": "xzv",
            "product_detail": [
                {
                    "product_barcode": "G296-SKU8945421522",
                    "product_sku": "SKU8945421522",
                    "sellable_qty": 1,
                    "unsellable_qty": 0,
                    "destruction_qty": 0,
                    "sellable_detail": [],
                    "unsellable_detail": [],
                    "destruction_detail": [],
                    "return_auth": 1,
                    "return_replacement_sku": null,
                    "photo_list": null
                }
            ],
            "sm_code": "TJDX-XF",
            "as_length": "0.00",
            "as_width": "0.00",
            "as_height": "0.00",
            "charge_weight": "0.000",
            "asro_note": "我要留言",
            "fee_details": {
                "shipping_fee": 8.307,
                "fuel_surcharge": 4.886,
                "other_fee": 0.489,
                "currency_code": "USD"
            }
        }
    ]
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
reference_no	String	Optional	50	参考号	fdzxcv4654132
asroCodes	String	Optional	32	退件单号	R000010-200710-0005
参数二选一或者2个都填
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
data	Object	数据内容
data参数

参数名	数据类型	说明
asro_code	String	退件单号
order_code	String	订单号
reference_no	String	参考号
is_transit	Int	是否退回集货仓：
1：是
2：否
collect_warehouse_code	String	集货区域仓编码
service_type	Int	退货服务类型：
1：退件质检
2：退件销毁
asro_status	String	退件状态
0：草稿
1：已提交
4：收货完成
5：处理完成
6：废弃
7：处理中
改动说明：由于业务调整，去掉了2待确认，3已确认等状态
cass_type	String	退件类型
0：服务商退件
1：客户退件
2：未预报退件
asro_add_time	String	创建时间
asro_audit_time	String	审核时间
asro_putaway_time	String	上架完成时间
warehouse_code	String	退件收货仓库
sm_type	String	派送方式
0：代选物流
1：自选物流
tracking_no	String	跟踪号
asro_reason	String	退件原因
product_detail	Object[]	退件产品明细
sm_code	String	物流产品编码
as_length	Int	计费长
as_width	Int	计费宽
as_height	Int	计费高
charge_weight	Int	计费重
asro_note	String	客服留言
return_identification	Int	退件标识：
1：谷仓发货退件
2：非谷仓发货退件
product_detail参数

参数名	数据类型	说明
product_barcode	String	商品编码
product_sku	String	客户商品编码
return_auth	Int	退件授权
0：否
1：是
return_replacement_sku	String	换标编码
photo_list	String[]	图片信息
sellable_qty	Int	良品数量
unsellable_qty	Int	不良品数量
destruction_qty	Int	销毁数量
sellable_detail	Object[]	良品明细
unsellable_detail	Object[]	不良品明细
destruction_detail	Object[]	销毁明细
sellable_detail | unsellable_detail | destruction_detail 参数

参数名	数据类型	说明
pas_code	String	售后码
new_product_sku	String	新客户商品编码
new_product_barcode	String	该字段已废弃，请使用new_product_sku
fee_details参数

参数名	数据类型	说明
shipping_fee	Float	运输费
operating_fee	Float	操作费用
fuel_surcharge	Float	燃油附加费
other_fee	Float	其它费用
currency_code	String	币别




RESTFUL V1退货单列表
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
URLhttps://oms.goodcang.net/public_open/return_order/list
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
{
    "currentPage": "1",
    "pageSize": "10",
    "startTime": "2020-08-12 11:00:00",
    "endTime": "2020-10-13 10:08:00",
    "startUpdateTime": "2021-04-06 11:00:00",
    "endUpdateTime": "2021-05-05 10:08:00",
    "asroStatus": "4",
    "cassType": "1",
    "asroCodes": "RG296-170914-0013"
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
    "message": "Success",
    "data": [
        {
            "asro_code": "RG296-170914-0013",
            "reference_no": "fdzxcv4654132",
            "asro_status": "4",
            "cass_type": "1",
            "asro_add_time": "2017-09-14 17:07:41",
            "asro_audit_time": "2017-09-14 17:08:08",
            "asro_putaway_time": "0000-00-00 00:00:00",
            "warehouse_code": "USEA",
            "sm_type": "0",
            "tracking_no": "787722279346",
            "collect_warehouse_code": "",
            "service_type": 1,
            "is_transit": 2,
            "asro_reason": "xzv",
            "product_detail": [
                {
                    "product_barcode": "G296-SKU8945421522",
                    "product_sku": "SKU8945421522",
                    "sellable_qty": 1,
                    "unsellable_qty": 0,
                    "destruction_qty": 0,
                    "sellable_detail": [],
                    "unsellable_detail": [],
                    "destruction_detail": [],
                    "return_auth": 1,
                    "return_replacement_sku": null,
                    "photo_list": null
                }
            ],
            "sm_code": "TJDX-XF",
            "fee_details": {
                "shipping_fee": 8.307,
                "fuel_surcharge": 4.886,
                "other_fee": 0.489,
                "currency_code": "USD"
            }
        }
    ],
    "Error": {
        "errCode": "",
        "errMessage": ""
    },
    "count": "1"
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
pageSize	String	Required		每页数据长度, 最大值100	10
currentPage	String	Required		当前页	1
startTime	String	Optional	datetime	创建时间	2020-06-22 09:00:00
endTime	String	Optional	datetime	结束时间	2020-06-22 09:00:00
startUpdateTime	String	Optional	datetime	更新时间	2020-06-22 09:00:00
endUpdateTime	String	Optional	datetime	结束更新时间	2020-06-22 09:00:00
asroStatus	String	Optional	2	售后退件状态
0：草稿
1：已提交
4：收货完成
5：处理完成
6：废弃
7：处理中
0
cassType	String	Optional	2	退件类型
0：服务商退件
1：客户退件
2：未预报退件
1
asroCodes	String	Optional	32	退件单号	R000010-200623-0001
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
data	Object	数据内容
data参数

参数名	数据类型	说明
asro_code	String	退件单号
reference_no	String	参考号
asro_status	Int	退件状态
0：草稿
1：已提交
4：收货完成
5：处理完成
6：废弃
7：处理中
改动说明：由于业务调整，去掉了2待确认，3已确认等状态
cass_type	Int	退件类型
0：服务商退件
1：客户退件
2：未预报退件
asro_add_time	String	创建时间
asro_audit_time	String	审核时间
asro_putaway_time	String	上架完成时间
is_transit	Int	是否退回集货仓：
1：是
2：否
collect_warehouse_code	String	集货区域仓编码
service_type	Int	退货服务类型：
1：退件质检
2：退件销毁
warehouse_code	String	退件收货仓库
sm_type	Int	派送方式
0：代选物流
1：自选物流
tracking_no	String	跟踪号
asro_reason	String	退件原因
product_detail	object[]	退件产品明细
sm_code	String	物流产品编码
order_code	String	订单号
as_length	Int	计费长
as_width	Int	计费宽
as_height	Int	计费高
charge_weight	Int	计费重
asro_note	String	客服留言
return_identification	Int	退件标识：
1：谷仓发货退件
2：非谷仓发货退件
fee_details	Object	费用明细
validity_period_detail	Object[]	效期实收明细
product_detail参数

参数名	数据类型	说明
product_barcode	String	商品编码
product_sku	String	客户商品编码
return_auth	Int	退件授权
0：否
1：是
return_replacement_sku	String	换标编码
photo_list	String[]	图片信息
sellable_qty	Int	良品数量
unsellable_qty	Int	不良品数量
destruction_qty	Int	销毁数量
sellable_detail	Object[]	良品明细
unsellable_detail	Object[]	不良品明细
destruction_detail	Object[]	销毁明细
sellable_detail | unsellable_detail | destruction_detail 参数

参数名	数据类型	说明
pas_code	String	售后码
new_product_sku	String	新客户商品编码
new_product_barcode	String	该字段已废弃，请使用new_product_sku
fee_details参数

参数名	数据类型	说明
shipping_fee	Float	运输费
operating_fee	Float	操作费用
fuel_surcharge	Float	燃油附加费
other_fee	Float	其它费用
currency_code	String	币别
validity_period_detail参数

参数名	数据类型	说明
product_sku	String	商品SKU
custom_product_sku	String	换标编码
validity_period_days	Int	有效期天数
on_shelf_num	Int	上架数量
receipt_num	Int	实收数量
creation_date	String	生产日期
expiration_date	String	过期日期




RESTFUL获取待确认退货列表
这是RESTFUL WEB API，接入方式请参见GD开放平台(V2)接入指引。
URLhttps://oms.goodcang.net/public_open/return_order/unauthorized_list
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
    "start_time": "2018-01-01 10:41:05",
    "end_time": "2018-11-01 10:42:05",
    "time_type": 1,
    "page_size": 2,
    "page": 1
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
    "code": 0,
    "message": "Success",
    "data": {
        "list": [
        {
            "asro_code": "RG296-180720-0001",
            "reference_no": "",
            "asro_status": "2",
            "cass_type": "1",
            "tracking_no": "61299992140482387342",
            "sm_code": "TJDX-XF",
            "warehouse_code": "USEA",
            "product_barcode": "G296-SKU8945421522",
            "product_sku": "SKU8945421522",
            "pas_code": "SHM20180720000036",
            "photos": [
                "data: image/jpg;base64,/9j/4AAQIY62Au6eIXqmtX+iIJt9i8j1cPfl7q6//Z"
            ],
            "quantity": 1,
            "received_time": "2018-07-20 11:23:57",
            "exception_process_status": "已处理"
        }
    ],
    "total": 3
    }
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
page_size	Int	Required		每页数据长度，最大值100	10
page	Int	Required		当前页	1
pas_code	String	Optional	50	售后码	fdzxcv4654132
product_sku	String	Optional	24	商品编码	fdzxcv4654132
reference_no	String	Optional	50	参考号	fdzxcv4654132
asro_code	String	Optional	32	退件单号	R000010-200518-0006
start_time	String	Optional	datetime	创建时间（开始）
格式YYYY-MM-DD HH:II:SS
如果退件单号或参考号传值时，该参数无效	2020-06-01 10:41:05
end_time	String	Optional	datetime	创建时间（结束）
格式YYYY-MM-DD HH:II:SS
如果退件单号或参考号传值时，该参数无效	2020-06-01 10:41:05
time_type	Int	Optional		查询时间区间类型
1：创建时间
2：收货时间
默认为创建时间类型	1
响应JSON

参数名	数据类型	说明
code	Int	0 成功，其它值表示失败。
message	String	文本消息
data	Object	数据内容 参见UnauthorizedListResp类型
UnauthorizedListResp类型

参数名	数据类型	说明
list	Object[]	列表数据 参见UnauthorizedListItemResp类型
total	Int	总数量
UnauthorizedListItemResp类型

参数名	数据类型	说明
asro_code	String	退件单号
reference_no	String	参考号
order_code	String	订单号
sm_type	Int	派送方式:
0：代选物流
1：自选物流
collect_warehouse_code	string	集货仓库代码
confirm_status	Int	确认状态:
0：待确认
1：已确认
该接口只返回"待确认"的数据
cass_type	String	退件类型
0：服务商退件
1：客户退件
2：未预报退件
tracking_no	String	跟踪号
sm_code	String	物流产品编码
warehouse_code	String	退件收货仓库
product_sku	String	客户商品编码
pas_code	String	售后码
photos	String[]	商品图片URL列表
数组元素为URL完整WEB路径
quantity	Int	收货数量
received_time	String	收货日期
已废弃product_barcode	String	商品编码（字段已废弃，请使用product_sku替代）




RESTFUL V1退货认领列表
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
URLhttps://oms.goodcang.net/public_open/return_order/claim_order_list
METHODPOST
请求JSON示例

1
2
3
4
5
{
    "reference_no": "",
    "pageSize": 10,
    "page": "1"
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
{
    "ask": "Success",
    "message": "Success",
    "data": [
        {
            "tracking_no": "dsadsads",
            "claim_code": "CEL122-211029-0001",
            "asro_code": "REL122-211103-5001",
            "warehouse_code": "USEA",
            "service_type": 0,
            "status": 2,
            "create_time": "2021-10-29 14:33:05",
            "claim_time": "2021-11-03 11:12:48",
            "destroy_time": "2021-10-29 14:33:15",
            "error_message": "",
            "expire_destroy_time": ""
        }
    ],
    "count": 1
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
pageSize	String	Required		每页数据长度, 最大值100	10
page	String	Required		当前页	1
tracking_code	String	Optional	50	跟踪号	test666
claim_code	String	Optional	50	认领单号	2020234
asro_code	String	Optional	datetime	退件单号	As908888
warehouse_code	String	Optional	32	仓库代码	2020-06-22 09:00:00
status	Int	Optional	1	状态
1：待认领
2：已认领
3：已销毁
1
create_time_start	String	Optional	50	收货开始时间	
create_time_end	String	Optional	50	收货结束时间	
dispose_time_start	String	Optional	50	销毁开始时间	
dispose_time_end	String	Optional	50	销毁结束时间	
claim_time_start	String	Optional	50	认领开始时间	
claim_time_end	String	Optional	50	认领结束时间	
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
data	Object[]	数据内容,参见Data参数
count	Int	总数
Data参数

参数名	数据类型	说明
tracking_no	String	跟踪号
claim_code	String	认领单号
asro_code	String	退件单号
warehouse_code	String	仓库代码
service_type	Int	退货服务类型：1:退件质检,2:退件销毁
status	Int	状态 1待认领 2已认领 3已销毁
create_time	String	收货时间
claim_time	String	认领时间
destroy_time	String	销毁时间
error_message	String	认领失败信息
expire_destroy_time	String	超期销毁剩余时间 (单位：天)




RESTFUL V1获取查件单详情
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
URLhttps://oms.goodcang.net/public_open/return_order/get_service_config
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
{
    "ask": 'Success',
    "message": "Success",
    "data": [
        {
            "warehouse_code": "USEA",
            "warehouse_name": "美东仓库",
            "cass_type": 0,
            "service_type_list": [
                1
            ],
            "enable_transit": 2,
            "return_identification": 1,
            "collect_warehouse": []
        },
        {
            "warehouse_code": "USEA",
            "warehouse_name": "美东仓库",
            "cass_type": 1,
            "service_type_list": [
                1
            ],
            "enable_transit": 2,
            "return_identification": 1,
            "collect_warehouse": []
        },
        {
            "warehouse_code": "USWE",
            "warehouse_name": "美西仓库",
            "cass_type": 0,
            "service_type_list": [
                1
            ],
            "enable_transit": 2,
            "return_identification": 1,
            "collect_warehouse": []
        },
        {
            "warehouse_code": "USWE",
            "warehouse_name": "美西仓库",
            "cass_type": 1,
            "service_type_list": [
                1
            ],
            "enable_transit": 2,
            "return_identification": 1,
            "collect_warehouse": [
            {
                "warehouse_code": "AU",
                "wp_code": "W51-2"
            },
            {
                "warehouse_code": "USWE",
                "wp_code": "USWE-6"
            }
        ]
        },
        {
            "warehouse_code": "JP",
            "warehouse_name": "日本仓库",
            "cass_type": 0,
            "service_type_list": [
                1
            ],
            "enable_transit": 2,
            "return_identification": 1,
            "collect_warehouse": []
        },
        {
            "warehouse_code": "JP",
            "warehouse_name": "日本仓库",
            "cass_type": 1,
            "service_type_list": [
                1
            ],
            "enable_transit": 2,
            "return_identification": 1,
            "collect_warehouse": []
        }
    ]
}
请求JSON

响应JSON

参数名	数据类型	说明
code	Int	0 成功，其它值表示失败。
message	String	文本消息
data	Object[]	数据内容，参见Data参数
Data参数

参数名	数据类型	说明
warehouse_code	String	仓库代码
warehouse_name	String	仓库名称
cass_type	Int	服务类型: 0.服务商退件，1.客户退件
service_type_list	Int[]	退货服务类型：1:退件质检,2:退件销毁
enable_transit	Int	是否支持退件转仓 0不支持 1支持
return_identification	String	1.谷仓发货退件, 2.非谷仓发货退件, 3.全部
collect_warehouse	Object[]	集货仓信息
collect_warehouse参数

参数名	数据类型	说明
warehouse_id	String	仓库id
warehouse_code	String	仓库代码
warehouse_name	String	仓库名称
country_name	String	国家名称
country_code	String	国家编码
state	String	省/州
city	String	城市
street_address1	String	街道地址1
street_address2	String	街道地址2
postcode	String	邮编
wp_code	String	物理仓编码




RESTFUL退货认领详情
这是RESTFUL WEB API，接入方式请参见GD开放平台(V2)接入指引。
URLhttps://oms.goodcang.net/public_open/return_order/claim_order_details
METHODPOST
请求JSON示例

1
2
3
{
    "claim_code": "CLAIM_CODE"
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
{
    "code": 0,
    "message": "success",
    "data": {
        "asro_code": "售后单号",
        "claim_code": "认领单",
        "tracking_no": "跟踪号",
        "reference_no": "参考号",
        "product_list": [
            {
                "ref_product_sku": "",
                "quantity": 0
            }
        ],
        "create_time": "添加时间",
        "claim_time": "认领时间",
        "customer_code": "客户代码",
        "expire_disposal_time": "超期销毁剩余时间",
        "disposal_time": "销毁时间",
        "internal_info_list": [
            {
                "product_sku": "",
                "quantity": 0,
                "replace_product_sku": ""
            }
        ],
        "return_pic_url_list": [
            "退货图片"
        ],
        "service_type": 1,
        "status": 1,
        "update_time": "更新时间",
        "warehouse_code": "退件仓",
        "warehouse_name": "退件仓中文名称",
        "log_list": [
            {
                "claim_code": "认领单号",
                "user_name": "操作人名称",
                "create_time": "创建时间",
                "content": "日志内容",
                "user_code": "操作人code",
                "before": "之前",
                "after": "之后",
                "type": 2
            }
        ]
    }
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
claim_code	String	Required		认领单号	
响应JSON

参数名	数据类型	说明
code	Int	0 成功，其它值表示失败。
message	String	文本消息
data	Object	参见ClaimOrderDetailResp类型
ClaimOrderDetailResp数据类型

参数名	数据类型	可为空	说明
asro_code	String	True	退件单号
claim_code	String	True	认领单号
tracking_no	String	True	跟踪号
reference_no	String	True	参考号
product_list	Object[]	False	认领单商品信息,参见ProductItemInformation类型
create_time	String	False	添加时间
claim_time	String	True	认领时间
customer_code	String	False	客户代码
expire_disposal_time	String	True	超期销毁剩余时间
disposal_time	String	True	销毁时间
internal_info_list	Object[]	False	商品内件信息,参见InternalProductItemInformation类型
return_pic_url_list	String[]	False	退货图片列表， 冗余字段，谷仓暂不提供未预报退件的拆包拍照服务
service_type	Int	True	服务类型，(枚举类型)
1: 退件质检
2: 退件销毁
3: 退件暂存
status	Int	True	状态，(枚举类型)
1: 待认领
2: 已认领
3: 已销毁
update_time	String	False	更新时间
warehouse_code	String	True	退件仓
warehouse_name	String	True	退件仓中文名称
log_list	Object[]	False	日志列表，参见ClaimOrderLogItem数据类型
ProductItemInformation数据类型

参数名	数据类型	可为空	说明
ref_product_sku	String	False	参考商品编码
该参数内容不一定指向商品信息，可能是任何参考信息，可能是包装上的条码,也有可能是sku，等等
quantity	Int	False	数量
InternalProductItemInformation数据类型

参数名	数据类型	可为空	说明
product_sku	String	False	商品编码(sku)
quantity	Int	False	数量
replace_product_sku	String	False	换标编码
ClaimOrderLogItem数据类型

参数名	数据类型	可为空	说明
user_name	String	False	操作人名称
claim_code	String	False	费用名称
create_time	String	False	费用名称
type	Int	False	类型，(枚举类型)
1: 状态
2: 服务类型
3: 退件参考号
4: 内件信息
5: 新增
before	String	False	之前
after	String	False	之后
user_code	String	False	操作人code
content	String	False	日志内容
