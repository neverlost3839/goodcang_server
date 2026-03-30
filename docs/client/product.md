RESTFUL V1新建商品
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
说明：在系统中创建商品信息，为后期发货和出单做基础数据。
注：商品编码和商品参考号是唯一。
URLhttps://oms.goodcang.net/public_open/product/add_product
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
{
    "product_sku": "mhtest45604",
    "reference_no": "sku45441",
    "cat_id_level2": "600011",
    "cat_lang": "zh",
    "product_name_cn": "门户api商品测试",
    "product_name_en": "test-product-api",
    "product_link": "http://pic3.nipic.com/20090527/1242397_102231006_2.jpg",
    "branded": "1",
    "product_brand": "门户商品",
    "product_model": "MH001",
    "product_weight": "2.269",
    "product_length": "10.23",
    "product_width": "10.45",
    "product_height": "10.69",
    "contain_battery": "0",
    "type_of_goods": "0",
    "unit": "pcs",
    "image_link": [
        "http://pic3.nipic.com/20090527/1242397_102231006_2.jpg",
        "http://pic3.nipic.com/20090527/1242397_102231006_2.jpg"
    ],
    "verify": "0",
    "product_declared_name_cn": "中文申报品名",
    "product_declared_name": "",
    "product_material": "",
    "product_function": "",
    "export_country": [
        {
            "country_code": "CN",
            "declared_value": 12.5
        }
    ],
    "import_country": [
        {
            "country_code": "US",
            "declared_value": 12.5
        },
        {
            "country_code": "GB",
            "declared_value": 12.5
        },
        {
            "country_code": "DE",
            "declared_value": 12.5
        }
    ],
    "certificate_url_list": [
        "http://www.SAMPLE_DOMAIN.com/file1.pdf",
        "http://www.SAMPLE_DOMAIN.com/file2.pdf"
    ],
    "thirdparty_sku_mapping": [
        "Blue2020_2XL"
    ],
    "sn_info":{
        "is_collect_serial_number": 0,
        "is_inbound_collect_serial_number": 1,
        "is_return_collect_serial_number": 0
    },
    "sku_wrapper_type": null,
    "remark":"备注"
}
响应JSON示例

1
2
3
4
5
6
{
    "ask": "Success",
    "message": "Success",
    "product_sku": "EA140512114042",
    "product_barcode": "G562-EA140512114640"
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
product_sku	String	Required	24	SKU
商品编码限制24个字符, 仅支持：数字、字母、下划线、中横线、小数点、+
XH009
sn_info	Object	Optional		采集序列号信息, 参见 SnInfo 对象	
sku_wrapper_type	Int	Optional		SKU包装属性，默认预包装
1：预包装
2：销售包装
3：原包彩盒
1
reference_no	String	Optional	50	客户参考代码
增加输入字符数范围，商品参考号不能超过255个字符
GCC001002
product_name_cn	String	Required	255	商品名称
不能超过255个字符
电脑
product_name_en	String	Required	255	商品英文名称
不能超过255个字符,不支持中文
computer
product_weight	Float	Required	7	重量，单位KG
取值范围0.001-9999.999，最多保留3位小数
10
product_length	Float	Required	6	长，单位CM
取值范围0.01-9999.99，最多保留2位小数
10
product_width	Float	Required	6	宽，单位CM
取值范围0.01-9999.99，最多保留2位小数
10
product_height	Float	Required	6	高，单位CM
取值范围0.01-9999.99，最多保留2位小数
6
contain_battery	Int	Required		货物属性，默认为0
    0：普货
    1：含电池
    2：纯电池
    3：纺织品
    4：易碎品
    6：超标纯电池
    7：超标含电池
    
0
type_of_goods	Int	Required		包裹类型
0：包裹
1：信封
0
cat_lang	String	Optional	2	品类语言，默认为zh
zh：中文
en：英文
zh
cat_id_level2	Int	Required		品类ID
传值是获取系统品类接口返回的品类级别（category_level）为2的品类ID
602276
verify	Int	Optional		是否自动提交审核
0：创建  状态草稿下需要手动在oms 提交审核
1：默认推送wms  审核

如不填 默认值是 0
注：审核之后产品信息不允许修改	0
product_declared_name_cn	String	Required	255	中文申报品名	数据线
product_declared_name	String	Optional	255	英文申报品名	data line
product_material	String	Required	255	材质	Metal
product_function	String	Optional	100	用途	phone
branded	Int	Required	2	是否品牌
0：否
1：是
0
product_brand	String	Optional	100	商品品牌
- 当branded为1时必填
- 不能超过100个字符；
苹果笔记本
product_model	String	Optional	100	商品型号
未填写默认“无”，表示无商品型号。
无
product_link	String	Required	1000	商品链接
最长1000字符：卖家在平台售卖的商品链接。
如：https://www.ebay.com.hk/itm/123456789.html
unit	String	Optional	11	单位
- 枚举值有：台、米、箱等。
- 具体请看成交单位表，默认为PCS，校验是在计量单位表是否存在；如果退税，以出口增值税发票成交单位结算。
PCS
image_link	String[]	Optional	300	商品图片链接
最多传10张
["http://pic3.nipic.com/20090527/1242397_102231006_2.jpg"]
export_country	Object	Required		出口国关税信息维护，参见 ExportCountry 对象	
import_country	Object	Required		进口国清关信息维护，参见 ImportCountry 对象	
certificate_url_list	String[]	Optional		商品证书URL地址数组列表
最多允许30个
["http://pic3.nipic.com/20090527/xxx"]
thirdparty_sku_mapping	String[]	Optional		映射编码数组列表
最多填写1个，限制50个字符, 仅支持：数字、字母、下划线、中横线、小数点、+
["Blue2020_2XL"]
return_auth	Int	Optional		退件授权
0：未授权
1：已授权
传空则默认为：1（已授权）
return_replacement_sku	String	Optional		换标编码	
batch_management_enabled	Integer	Optional		是否进行批次管理：默认为0
0：否
1：是
0
batch_info	Object	Optional		批次信息, 参见 BatchInfo 对象	0
battery_info	Object	Optional		电池信息, 参见BatteryInfo对象
货物属性为以下值必填
6：超标纯电池
7：超标含电池
remark	String	Optional		备注
最大长度为500个字符
备注
BatchInfo

参数名	数据类型	是否必填	最大数据长度	说明	示例
validity_period_info	Object	Optional		有效期批次信息，参见ValidityPeriodInfo	
ValidityPeriodInfo

参数名	数据类型	是否必填	最大数据长度	说明	示例
expiration_enabled	Integer	Required		是否进行有效期管理
0：否
1：是
0
shelf_life_days	Integer	Optional		有效期天数
- expiration_enabled=1时，必填
- 大于0小于等于9000的整数
360
outbound_threshold	Integer	Optional		禁售天数
- expiration_enabled=1时，必填
- 大于等于0并且小于有效期天数的整数
10
warning_days	Integer	Optional		预警天数
- expiration_enabled=1时，必填
- 大于禁售天数并且小于有效期天数的整数
30
inbound_threshold	Integer	Optional		禁收天数
- expiration_enabled=1时，必填
- 大于禁售天数并且小于有效期天数的整数
90
ExportCountry

参数名	数据类型	是否必填	最大数据长度	说明	示例
country_code	String	Required	2	国家/地区简称,目前只能填写CN	CN
declared_value	Float	Required	6	申报价值
币种只能为USD，最多保留两位小数
取值范围0.01-9999.99，最多保留2位小数
10
ImportCountry

参数名	数据类型	是否必填	最大数据长度	说明	示例
country_code	String	Required	2	国家/地区简称
可支持的国家/地区代码与您的账户所开通的仓库覆盖国家/地区相关，
查询已开通仓库请参见API「获取系统仓库」。
US
declared_value	Float	Required	6	申报价值
币种只能为USD
取值范围0.01-9999.99，最多保留2位小数
10
SnInfo

参数名	数据类型	是否必填	最大数据长度	说明	示例
is_collect_serial_number	Int	Optional		出库是否采集序列号
- 默认不采集，指仓库出库扫描时是否需采集商品序列号（SN码）信息。
- 如需要采集，请务必在序列号管理中提前维护商品的序列号信息
- 当入库是否采集序列号为是1时，出库是否采集序列号必须为1
0：不采集序列号
1：采集序列号
0
is_inbound_collect_serial_number	Int	Optional		入库是否采集序列号
- 默认不采集，指仓库入库扫描时是否需采集商品序列号（SN码）信息。
- 如需要采集，请务必在序列号管理中提前维护商品的序列号信息
0：不采集序列号
1：采集序列号
0
is_return_collect_serial_number	Int	Optional		退件是否采集序列号
- 默认不采集，指退件扫描时是否需采集商品序列号（SN码）信息
- 如需要采集，请务必在序列号管理中提前维护商品的序列号信息
- 当出库是否采集序列号为1时，退件是否采集序列号必须为1；
    反之出库是否采集序列号为0时，退件是否采集序列号必须为0
0：不采集序列号
1：采集序列号
0
BatteryInfo

参数名	数据类型	是否必填	最大数据长度	说明	示例
battery_model	String	Required	50	电池型号	GB-S04-733068
un_code	String	Required	16	UN编码	UN3480
battery_power_range	Integer	Required		电池功率范围（WH）
1：101WH~300WH
2：>300WH
1
battery_power	Integer	Optional		电池功率（WH）	200
msds_file_url	String	Required	300	MSDS报告证书链接	http://pic3.nipic.com/20090527/xxx
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
data	Object	创建订单响应结构，参见 ProductMutationResp。
ProductMutationResp

product_sku	String	SKU
product_barcode	String	商品条码