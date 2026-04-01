RESTFUL计划单列表
这是RESTFUL WEB API，接入方式请参见GD开放平台(V2)接入指引。
URLhttps://oms.goodcang.net/public_open/plan_order/list
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
    "code_type": 1,
    "code_value_list": [
       "JH-XXX-20220322-12"
    ],
    "time_type": 0,
    "start_time": "2021-09-16 00:00:00",
    "end_time": "2022-03-21 23:59:59",
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
{
    "code": 0,
    "message": "success",
    "data": {
        "list": [
            {
                "plan_order_code": "JH-XXX-20220322-12",
                "reference_no": "",
                "warehouse_code": "USEA",
                "dest_warehouse_type": 1,
                "label_replacement_option": 0,
                "is_change_label": 0,
                "is_stick_label": 0,
                "actual_fee_estimate": "0.000",
                "currency_code": "USD",
                "product_list": [
                    {
                        "product_name": "sku-name",
                        "product_sku": "sku-123",
                        "quantity": 10
                    }
                ],
                "box_list": [],
                "order_status": 1,
                "abnormal_reason": "",
                "create_time": "2022-03-21 19:37:19",
                "update_time": "2022-03-21 19:37:19",
                "submit_time": null,
                "finish_time": null
            }
        ],
        "total": 1
    }
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
order_status	Int	Optional		计划单状态
不传或传null：全部
0:废弃
1:草稿
2:异常
3:待配货
4:已完成
code_type	int	Optional		单号类型
1:计划单号（默认）
2:参考号
3:商品编码
4:箱唛号
code_value_list	String[]	Optional	100	单号值
用数组传递，最多100个
warehouse_code	String	Optional	20	发货仓库	USEA
is_change_label	Int	Optional		换标服务
0：否
1：是
label_replacement_option	Int	Optional		换标要求
1:外箱
2:内箱
is_stick_label	Int	Optional		贴标服务
0：否
1：是
dest_warehouse_type	Int	Optional		目的仓类型
不传或传null：全部
1:FBA
2:第三方
time_type	Int	Optional		时间类型
0：创建时间
1：提交时间
2：配货时间
0
start_time	String	Optional		起始时间
若start_time有值，end_time字段也需要有值。
2022-03-19 00:00:00
end_time	String	Optional		截止时间
若end_time有值，start_time字段也需要有值。
2022-03-19 23:59:59
page	Int	Required		分页页码	1
page_size	Int	Required		分页数量
最大200
20
响应JSON

参数名	数据类型	说明
code	Int	0 成功，其它值表示失败。
message	String	文本消息
data	Object	订单数据，参见 BoxListResp。
BoxListResp

参数名	数据类型	可为空	说明
total	Int	False	总数量
list	Object[]	False	计划单信息列表，数组元素详见 OrderItemComposite类型。
OrderItemComposite

参数名	数据类型	可为空	说明
plan_order_code	String	False	计划单号
reference_no	String	True	参考号
warehouse_code	String	False	区域仓
dest_warehouse_type	Int	False	目的仓类型
1:FBA
2:第三方
label_replacement_option	Int	False	换标要求
0:无换标要求
1：外箱
2：内箱
is_change_label	Int	False	换标服务
0：否
1：是
is_stick_label	Int	False	贴标服务
0：否
1：是
actual_fee_estimate	String	False	费用总额
currency_code	String	False	币种
order_status	Int	False	状态
0:废弃
1:草稿
2:异常
3:待配货
4:已完成
abnormal_reason	String	True	异常原因
create_time	String	False	创建时间
update_time	String	True	更新时间
submit_time	String	True	提交时间
finish_time	String	True	完成时间（配货时间）
product_list	Object[]	False	商品信息，参见 ProductListItem。
box_list	Object[]	True	暂存箱信息，参见 BoxListItem。
ProductListItem

参数名	数据类型	可为空	说明
product_name	String	False	商品名称
product_sku	String	False	商品编码
quantity	Int	False	商品数量
BoxListItem

参数名	数据类型	可为空	说明
box_no	String	False	箱号
box_mark	String	False	箱唛号
quantity	Int	False	总数量
sku总数量
type_quantity	Int	False	商品种类
SKU种类的数量，例如有sku1, sku2, 算2个种类
product_list	Object[]	False	商品信息，参见 ProductListIndividualItem。
ProductListIndividualItem

参数名	数据类型	可为空	说明
product_sku	String	False	商品编码
quantity	Int	False	商品数量




RESTFUL装箱列表
这是RESTFUL WEB API，接入方式请参见GD开放平台(V2)接入指引。
URLhttps://oms.goodcang.net/public_open/plan_order/box_list
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
    "box_status": null,
    "code_type": 1,
    "code_value_list":[],
    "warehouse_code":"",
    "is_change_label":null,
    "is_stick_label":null,
    "time_type":1,
    "start_time":null,
    "end_time":null,
    "page_size":20,
    "page":1
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
{
    "code": 0,
    "message": "success",
    "data": {
        "list": [
            {
                "box_no": "jhqtest-001",
                "plan_order_code": "JH-XXX-20220314-0001",
                "relation_order_code": "XXX-210413-0004",
                "warehouse_code": "USEA",
                "temp_total_amount": "0.00",
                "currency_code": null,
                "is_change_label": 0,
                "label_replacement_option": 0,
                "is_stick_label": 0,
                "officer_no": null,
                "box_status": 1,
                "length": "3.00",
                "width": "2.00",
                "height": "1.00",
                "weight": "1.000",
                "pack_time": "2022-03-05 16:38:38",
                "sku_list": [
                    {
                        "fnsku": "FBA-222SSA2",
                        "product_sku": "SKU-1",
                        "quantity": 10,
                        "product_sku_name":"sku-name"
                    }
                ]
            }
        ],
        "total": 1
    }
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
box_status	Int	Optional		箱状态
0:可用
1:已用
code_type	int	Optional		单号类型
1:箱唛号（默认）
2:计划单号
3:关联单号
4:商品编码
code_value_list	String[]	Optional	100	单号值
用数组传递，最多100个
warehouse_code	String	Optional	20	发货仓库	USEA
is_change_label	Int	Optional		换标服务
0：否
1：是
label_replacement_option	Int	Optional		换标要求
1:外箱
2:内箱
is_stick_label	Int	Optional		贴标服务
0：否
1：是
time_type	Int	Optional		时间类型
1:装箱时间
1
start_time	String	Optional		起始时间
若start_time有值，end_time字段也需要有值。
2022-03-19 00:00:00
end_time	String	Optional		截止时间
若end_time有值，start_time字段也需要有值。
2022-03-19 23:59:59
page	Int	Required		分页页码	1
page_size	Int	Required		分页数量
最大200
20
响应JSON

参数名	数据类型	说明
code	Int	0 成功，其它值表示失败。
message	String	文本消息
data	Object	订单数据，参见 BoxListResp。
BoxListResp

参数名	数据类型	可为空	说明
total	Int	False	总数量
list	Object[]	False	装箱信息列表，数组元素详见 OrderItemComposite类型。
OrderItemComposite

参数名	数据类型	可为空	说明
box_no	String	False	箱唛号
plan_order_code	String	False	计划单号
relation_order_code	String	False	关联单号
warehouse_code	String	False	区域仓
temp_total_amount	String	False	暂存费用总额
currency_code	String	False	币种
is_change_label	Int	False	换标服务
0：否
1：是
label_replacement_option	Int	True	换标要求
0:无换标要求
1:外箱
2:内箱
is_stick_label	Int	False	贴标服务
0：否
1：是
euro_terms_code	String	False	合规负责人编码
box_status	Int	False	箱状态
0:可用
1:已用
length	String	False	长
width	String	False	宽
height	String	False	高
weight	String	False	重量
pack_time	String	True	装箱时间
sku_list	Object[]	False	商品信息，参见 PlanBoxSkuListItem。
PlanBoxSkuListItem

参数名	数据类型	可为空	说明
fnsku	String	False	FBA商品编码
product_sku	String	False	商品编码
quantity	Int	False	商品数量
product_sku_name	String	False	商品名称
