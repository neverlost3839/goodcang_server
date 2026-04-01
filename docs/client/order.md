RESTFUL V1新建订单
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
说明：在系统中创建订单信息，正常订单的订单号和参考号是唯一的（订单在废弃之后，参考号可以重复使用）
「指定批次」（适用于销毁和自提的订单的一个选项）的订单，不能通过API创建，请在浏览器用手动方式创建。
URLhttps://oms.goodcang.net/public_open/order/create_order
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
{
    "reference_no": "POSTMAN-TEST-GD-0421",
    "platform": "EBAY",
    "shipping_method": "FEDEX-SMALLPARCEL",
    "warehouse_code": "USEA",
    "country_code": "US",
    "province": "FL",
    "city": "Miami",
    "company": "Goodcang Inc.",
    "address1": "2225TH AVE WED",
    "address2": "",
    "address3": "",
    "zipcode": "33000",
    "doorplate": "",
    "name": "Katiu",
    "last_name": "Fake",
    "phone": "88888888",
    "email": "",
    "verify": 0,
    "is_signature": 0,
    "order_desc": "订单备注",
    "customer_package_requirement": null,
    "items": [
        {
            "product_sku": "00853",
            "quantity": 1
        }
    ],
    "sender_info": {
        "name": "MR ZHANG",
        "phone": "12345678"
    },
    "vat_change_info":{
        "ioss_number": "ioss_123",
        "pid_number": "pid_123",
        "recipient_eori": "eori_123",
        "recipient_vat": "vat_123",
        "shipper_eori": "shipper_123",
        "shipper_company_name": "shipper_apple",
        "shipper_vat": "shipper_123"
    }
}
响应JSON示例

1
2
3
4
5
{
    "ask": "Success",
    "message": "Success",
    "order_code": "000-160617-0001"
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
reference_no	String	Optional	50	订单参考号(建议使用平台单号)	2020071601
platform	String	Optional	20	平台，默认OTHER
3DCART
AE CERTIFIED
ALIBABA
ALIEXPRESS
ALLEGRO
ALLVALUE
AMAZON
AMAZON MSF
AMERICANAS
ASOS
展开>>	EBAY
shipping_method	String	Required	32	物流产品代码，参考getShippingMethod。（当使用物流优选服务时，可选填项，参见vas.logistics_recommendation_option选项）。 当使用物流优选时，该参数必须传null，或者不传，否则报错。	FEDEX-SMALLPARCEL
warehouse_code	String	Required	32	配送仓库代码，参考getWarehouse。（当使用物流优选服务时，可选填项，参见vas.logistics_recommendation_option选项）。 当使用物流优选时，且入参提供了仓库，则系统在该仓库范围内选择适用的物流方式。	USEA
country_code	String	Required	2	收件人国家/地区，参考getCountry	US
province	String	Required	20	省	FL
city	String	Required	32	城市	Miami
company	String	Optional	50	公司名称	谷仓
address1	String	Required	50	地址1
关于地址1长度限制50的说明：
市面上绝大部分物流服务商，不支持地址1超过50字符，超过的部分，要拆解到地址2。
地址1、地址2必填一个。
One Microsoft Way
address2	String	Optional	50	地址2
地址1、地址2必填一个。
创汇国际2
zipcode	String	Required	20	邮编	33178
doorplate	String	Optional	20	门牌号	35
name	String	Required	48	收件人名	samuel
last_name	String	Optional	48	收件人姓	fake
cell_phone	String	Optional	8	分机号
当platform为AMAZON时，此参数无效。
-1
phone	String	Optional	20	收件人联系方式
当platform为AMAZON时，可以由此分解分机号(cell_phone)参数。
435028690
email	String	Optional	100	收件人邮箱	xx@gmail.com
order_desc	String	Optional	500	订单备注	xx
customer_package_requirement	Int	Optional		包材要求，请注意：未开启订单销售包材服务不支持选择
1：纸箱
2：快递袋
3：气泡袋
4：环保袋
1
verify	Int	Optional		是否直接审核，默认为0
0：新建不审核(草稿状态)
1：新建并审核
审核通过之后，不可编辑	1
is_shipping_method_not_allow_update	Int	Optional		派送方式是否允许修改
0：可以修改
1：不允许修改（默认值）
0
is_signature	Int	Optional		签名服务
0：不选择签名服务
1：签名服务
不填默认为0	0
is_insurance	Int	Optional		保险服务, 不填默认为0
0：不需要
1：需要
0
insurance_value	Float	Optional	7	保额, 不填为0
最多保留3位小数
0
fba_shipment_id	String	Optional	12	FBA Shipment ID FBA 类型订单必填 是12位数字+加字母组成	FBA15D330YGA
fba_shipment_id_create_time	String	Optional	datetime	FBA Shipment ID创建时间 FBA 类型订单必填	2020-07-17 14:14:14
property_label	String	Optional	50	平台模式
SFP
SFP
business_type	Int	Optional		配送方式
0:仓配一体
1:仓配分离
该字段受限于是否开通仓配分离服务
0
is_change_label	Int	Optional		FBA换标服务
1：换标
0：不换标
(不填，默认为1)	0
age_detection	Int	Optional		若选择的物流产品支持年龄检测服务不填则默认16，该服务只可填16或18。其他物流产品默认为0不检测。
特别说明：如果物流产品支持年龄检测服务，该参数只能传16或18，传0或者不传，将强制改为16。	0
items	Object[]	Required		订单明细
如果是FBA订单，并且选择仓库装箱商品（is_warehouse_packing = 1），不能填写。
LiftGate	Int	Optional		LiftGate服务
0：为否
1：为是
0
payment_time	String	Optional	datetime	付款时间 格式必须为 YYYY-MM-DD HH:MM:SS，例如 2021-10-01 22:12:01	2020-07-17 14:14:14
attachment_ids	Int[]	Optional		订单附件id数组
参考上传附件接口上传附件，注意use_for要用ORDER_ATTACHMENT，其它类型无法用在当前场景。
[12,88]
estimated_arrival_date	String	Optional	datetime	预计到货日期, 物流产品支持则填写， 格式例如：2021-03-01	2020-07-17
estimated_arrival_time	Int | String	Optional	datetime	到货时间段
兼容数字枚举 或 具体时间段
具体时间段支持“~”和“-”两种时间分隔符（例如：08:00~12:00 或 08:00-12:00）
物流产品支持则可填写，否则输入无效。支持选项有：
108:00~12:00
212:00~14:00
314:00~16:00
416:00~18:00
518:00~20:00
600:00~10:00
700:00~17:00
1
sender_info	Object	Optional		发件人信息，参见SenderInfo。（仓库所在地为日本时适用，否则该参数将被忽略）	
vat_change_info	Object	Optional		欧盟税改资料，参见VatChangeInfo。（非标准订单时，该参数将被忽略）	
is_euro_label	Int	Optional		是否贴标。1是，0否	
vas	Object	Optional		增值服务选项，参见对象 ValueAddedService。	
is_warehouse_packing	Int	Optional		是否仓库装箱商品（FBA订单适用）。
1：是
0：否（默认）
is_warehouse_packing = 1时，FBA转仓单信息（carton_info）必填。
carton_info	Object	Optional		FBA转仓单信息，参见对象 CartonProductItem。
如果是FBA订单，并且选择仓库装箱商品（is_warehouse_packing = 1），必填。
truck_info	Object	Optional		卡派渠道物流信息，参见对象 TruckInfo。
FBA类型订单 并且 所选物流产品为卡派渠道（is_truck=1）时, 必填。
items参数

参数名	数据类型	是否必填	最大数据长度	说明	示例
product_sku	String	Required	24	SKU	LZZTEST1212
quantity	Int	Required		数量	1
transaction_id	String	Optional	50	订单交易号	291529280347
item_id	String	Optional	50	订单商品编码	291529280347
fba_product_code	String	Optional	20	FBA商品编码，当is_change_label=1时必填	X00170NZI8
euro_terms_code	String	Optional		合规负责人编码	
label_replacement_qty	int	Optional		内件货物总数量
FBA订单适用
product_declared_value	String	Optional	8,2	申报价值(USD)
取值范围0.01-99999999.99，最多保留2位小数
hs_code	String	Optional	10	海关编码，必须为6-10位数字	
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
CartonProductItem（FBA订单适用）

参数名	数据类型	是否必填	长度	说明
carton_list	Object[]	Required		箱唛号列表，参见数组元素 CartonListItem。
renewal_product_list	Object[]	Optional		商品信息变更列表，参见数组元素 CartonProductLineItem。
CartonListItem（FBA订单适用）

参数名	数据类型	是否必填	长度	说明
carton_no	String	Required		箱唛号
fba_box_mark	String	Required	30	FBA箱唛号
CartonProductLineItem（FBA订单适用）

参数名	数据类型	是否必填	长度	说明
sku	String	Required	24	商品sku
product_declared_value	String	Required	8,2	申报价值(USD) 必须在0.01到99999999.99范围内，不能为0，最多保留2位小数；
hs_code	String	Required	10	海关编码，必须为6-10位数字
TruckInfo（FBA订单适用）

参数名	数据类型	是否必填	长度	说明
reference_id	String	Required	100	参考号，当物流产品为卡派渠道时需要填写，也可更换非卡派渠道物流产品
seller_name	String	Required	100	店铺名称，当物流产品为卡派渠道时需要填写，也可更换非卡派渠道物流产品
fba_warehouse_code	String	Required	100	亚马逊仓库地址四字代码，当物流产品为卡派渠道时需要填写，也可更换非卡派渠道物流产品
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
data	Object	创建/修改订单结果响应对象，参见 OrderMutationResp。
OrderMutationResp

参数名	数据类型	可空	说明
order_code	String	可空	订单号