RESTFUL V1创建入库单
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
说明：创建入库单
目的仓为美南仓库时，单个入库单最多只能录入20种SKU且货型为S或XS的商品不允许添加，单个海柜号最多只能录入20种SKU
URLhttps://oms.goodcang.net/public_open/inbound_order/create_grn
METHODPOST
创建中转入库单请求JSON示例

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
{
    "transit_type": 3,
    "receiving_shipping_type": 1,
    "sm_code": "2233",
    "reference_no": "test201905080030",
    "transit_warehouse_code": "wh002",
    "warehouse_code": "UK",
    "customs_type": "1",
    "collecting_service": "1",
    "collecting_address": [
        {
            "ca_first_name": "tf1",
            "ca_last_name": "li",
            "ca_contact_phone": "18888888888",
            "ca_state": "广东省",
            "ca_city": "深圳市",
            "ca_country_code": "中国",
            "ca_zipcode": "518000",
            "ca_address1": "sadg"
        }
    ],
    "collecting_time": "2019-12-25 12:12:12",
    "value_add_service": "",
    "clearance_service": 1,
    "import_company": 120,
    "export_company": 121,
    "receiving_desc": "易碎品,轻拿轻放",
    "verify": "0",
    "car_model_code": "",
    "weight": 0,
    "volume": 0,
    "items": [
        {
            "box_no": "1",
            "reference_box_no": "",
            "box_details": [
                {
                    "product_sku": "DDDD",
                    "quantity": "10",
                    "data_code": "",
                    "serial_number": ""
                }
            ]
        },
        {
            "box_no": "2",
            "reference_box_no": "",
            "box_details": [
                {
                    "product_sku": "MHTEST58439",
                    "quantity": "20",
                    "data_code": "",
                    "serial_number": ""
                }
            ]
        },
        {
            "box_no": "3",
            "reference_box_no": "",
            "box_details": [
                {
                    "product_sku": "YDQ530006",
                    "quantity": "20",
                    "data_code": "",
                    "serial_number": ""
                }
            ]
        }
    ]
}
创建入库单_自发&FBA请求JSON示例

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
{
    "transit_type": 0,
    "receiving_shipping_type": 1,
    "reference_no": "test201905080030",
    "tracking_number": "32321565",
    "warehouse_code": "USEA",
    "eta_date": "2017-03-12",
    "import_company": 103,
    "receiving_desc": "易碎品,轻拿轻放",
    "verify": "0",
    "items": [
        {
            "box_no": "1",
            "reference_box_no": "",
            "box_details": [
                {
                    "product_sku": "DDDD",
                    "quantity": "10"
                }
            ]
        },
        {
            "box_no": "2",
            "reference_box_no": "",
            "box_details": [
                {
                    "product_sku": "MHTEST58439",
                    "quantity": "20"
                }
            ]
        },
        {
            "box_no": "3",
            "reference_box_no": "",
            "box_details": [
                {
                    "product_sku": "YDQ530006",
                    "quantity": "20"
                }
            ]
        }
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
{
    "ask": "Success",
    "message": "Success",
    "data": {
        "receiving_code": "RVG296-190703-0001"
    }
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
reference_no	String	Optional	50	参考号	2020062901
transit_type	Int	Required		入库单类型：
0：自发入库单
3：中转入库单
5：FBA入库单
3
receiving_shipping_type	Int	Required		运输方式
0：空运
1：海运散货
2：快递
3：铁运整柜
4：海运整柜
5：铁运散货
0
tracking_number	String	Optional	35	跟踪号/海柜号
中转选填，verify=1（入库单提交审核）时自发，FBA转仓必填
MATS7401101
warehouse_code	String	Required	32	海外仓仓库编码	USEA
eta_date	Datetime	Optional	datetime	预计到达时间
（格式：YYYY-MM-DD）。自发入库单和FBA入库单必填
2020-07-01
receiving_desc	String	Optional	255	备注	备注
import_company	Int	Optional		进口商编码
- 目的仓库对应的国家需要提供VAT(目前英国、德国、法国需要提供)
- transit_type=3特有
- 必填条件：clearance_service=1（自有税号清关）
785
verify	Int	Optional		是否审核值
0：新建不审核(草稿状态)
1：新建并审核
默认为0，审核通过之后，不可编辑	0
items	Object	Required		入库单明细	
shiper_address	Object	Optional		入库单发货地址
（仅适用于自发入库单）
sm_code	String	Required	255	物流产品
transit_type=3特有。物流产品（整柜无需填）
USEAAIRFREIGHT6000D
transit_warehouse_code	String	Required	255	中转仓仓库编码
transit_type=3特有。（非整柜：物流产品绑定的中转仓库 ， 整柜：国内中转仓库）
DG
customs_type	Int	Required		报关方式
transit_type=3特有
0：EDI报关
1：委托报关
2：报关自理
1
collecting_service	Int	Required		揽收服务
transit_type=3特有
0：自送货物
1：上门提货
1
collecting_address	Object[]	Optional		揽收资料
transit_type=3特有
必填条件：当collecting_service=1（上门揽收）时必填
collecting_time	Datetime	Optional	datetime	揽收时间
transit_type=3特有
注：揽收时间不允许小于创建时间
2020-07-02 12:00
customers_send_info	Object	Optional		客户自送信息
- 参见 CustomersSendInfo 对象
- transit_type=3特有
- 必填条件：当collecting_service=0（自送货物）时必填
value_add_service	String	Optional	255	增值服务
transit_type=3特有
world_ease：worldease服务
origin_crt：产地证
fumigation：熏蒸
world_ease
clearance_service	Int	Required		是否自有税号清关
transit_type=3特有
0：否（KJ清关：KJ税号）
1：是（KJ清关+自主税号）
注：当warehouse_code开启了VAT，必为1；如没开启，可选0或者1
0
export_company	Int	Optional		出口商编码
transit_type=3特有
372
car_model_code	String	Optional	255	车型 车型接口获取。transit_type=3特有。当collecting_service=1时必填。	minivan
weight	Float	Optional	8	重量(kg)
小于等于100000
取值范围0.01-999999.99，最多保留2位小数
10
volume	Float	Optional	5	体积(立方米)
小于等于100
取值范围0.01-99999.99，最多保留2位小数
10
wp_code	String	Optional		物理仓仓库代码
通过获取系统仓库接口获取物理仓编码，不传默认为仓库主物理仓编码。
is_delay	Int	Optional		是否递延，0否（默认），1是	
is_rollover	Int	Optional		是否仓库装箱商品
0：否（默认）
1：是
transit_type=5（FBA入库单）必填
items参数

参数名	数据类型	是否必填	最大数据长度	说明	示例
box_no	Int	Required		箱号
从1开始的连续正整数
1
reference_box_no	String	Optional	30	箱唛参考号 自发入库单/FBA入库单 才有该字段
FBA入库单，且为仓库装箱商品（is_rollover=1）时，必填。
1
box_details	Object[]	Required		箱子信息，参见对象 box_details。	
box_details

参数名	数据类型	是否必填	最大数据长度	说明	示例
product_sku	String	Required	24	SKU	TEST20200428
quantity	Int	Required		数量
为仓库装箱商品（is_rollover=1）时，数量值会置为1。
10
fba_product_code	String	Optional	20	FBA商品编码
transit_type=5（FBA入库单）, 且不是仓库装箱商品（is_rollover=0）时，必填。
为仓库装箱商品（is_rollover=1）时，无需填写，该值会默认置空。
ABC
data_code	String	Optional	100	序列号集成码，限制100个字符,	
serial_number	String	Optional	100	序列号，限制6-100个字符, 仅支持：数字、字母、下划线、中横线、小数点、+	
shiper_address(发件人地址)

参数名	数据类型	是否必填	最大数据长度	说明	示例
sa_contacter	String	Required	50	联系人	lucy
sa_contact_phone	String	Required	50	联系电话（手机号）	18500000000
sa_country_code	String	Required	2	发件国家/地区简称	CN
sa_state	String	Required	50	省/州	广东省
sa_city	String	Required	50	城市	深圳市
sa_region	String	Optional	50	区	龙岗区
sa_address1	String	Optional	50	地址1	创汇国际
sa_address2	String	Optional	50	地址2	地址2
collecting_address (揽收地址)

参数名	数据类型	是否必填	最大数据长度	说明	示例
ca_first_name	String	Required	50	揽收联系人-名	Li
ca_last_name	String	Required	50	揽收联系人-姓	max
ca_contact_phone	String	Required	50	揽收联系人电话	18565743265
ca_state	String	Required	50	揽收地址州/省份	广东省
ca_city	String	Required	50	揽收地址城市	深圳市
ca_country_code	String	Required	50	揽收地址国家/地区	中国
ca_zipcode	String	Required	50	揽收地址邮编	45362
ca_address1	String	Required	50	揽收地址1	创汇国际
ca_address2	String	Required	50	揽收地址2	地址2
CustomersSendInfo (客户自送信息)

参数名	数据类型	是否必填	最大数据长度	说明	示例
arrive_transfer_warehouse_time	Datetime	Optional	datetime	预计到达中转仓时间
注：时间需大于等于当前时间
2020-07-02 12:00:00
company_name	String	Optional	50	快递公司名称	
delivery_code	String	Optional	500	快递单号
注：多个快递单号用英文逗号隔开
plate_no	String	Optional	50	车牌号	
driver_name	String	Optional	50	司机姓名	
driver_phone	String	Optional	50	司机电话
仅支持输入数字、+、-
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
data	Object	入库创建/修改响应结果，参见 InboundOrderMutationResp。
InboundOrderMutationResp

参数名	数据类型	说明
receiving_code	String