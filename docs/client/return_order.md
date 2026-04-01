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