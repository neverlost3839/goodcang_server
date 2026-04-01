RESTFUL V1获取库存
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
说明：获取系统中的商品库存信息，方便客户管理自己的库存数据
URLhttps://oms.goodcang.net/public_open/inventory/get_product_inventory
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
    "pageSize": "1",
    "page": 1,
    "product_sku": "",
    "product_sku_arr": [],
    "warehouse_code": "USEA",
    "warehouse_code_arr": []
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
    "ask": "Success",
    "message": "Success",
    "count": "137",
    "data": [
        {
            "product_barcode": "000011-TEST150810002",
            "product_sku": "TEST150810002",
            "warehouse_code": "USEA",
            "onway": "1482",
            "pending": "31",
            "sellable": "10335",
            "unsellable": "0",
            "reserved": "10",
            "shipped": "18",
            "sold_shared": "0",
            "tune_out": 2,
            "tune_in": 1,
            "product_sales_value": "0.00",
            "warehouse_desc": "美东仓库",
            "stocking": 10,
            "pi_no_stock": 1,
            "pi_freeze": 0
        }
    ]
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
pageSize	Int	Required		每页数据长度，最大值为200	10
page	Int	Required		当前页	1
product_sku	String	Optional	24	商品编码
精确匹配搜索，
编码为系统编码时，库存数 = 系统编码库存。
编码为外部编码时，库存数 = 外部编码库存。
LZZTEST1212
product_sku_arr	String[]	Optional		多个SKU,数组格式
最多允许200个元素，每个元素精确匹配搜索。
["LZZTEST1212","LZZTEST1212"]
warehouse_code	String	Optional	32	仓库代码	USEA
warehouse_code_arr	String[]	Optional		多个仓库代码,数组格式	["USEA"]
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
count	Int	总数量
data	Object	数据内容
data参数

参数名	数据类型	说明
product_sku	String	SKU
warehouse_code	String	仓库代码
onway	Int	在途数量
pending	Int	待上架数量
sellable	Int	可售数量
unsellable	Int	不合格数量
reserved	Int	待出库数量
shipped	Int	历史出库数量
product_barcode	String	商品编码（客户代码-商品编码）
stocking	Int	备货数量
pi_no_stock	Int	缺货数量
warehouse_desc	String	仓库描述
pi_freeze	Int	冻结数量


RESTFUL V1获取库存动态列表
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
URLhttps://oms.goodcang.net/public_open/inventory/get_inventory_log
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
{
    "pageSize": "10",
    "page": 1,
    "warehouse_code": "USEA",
    "application_code": 3,
    "reference_no_list": [
        "RVG296-210518-0016",
        "RVG296-210329-0001"
    ],
    "product_sku_list": [
        "ALI_AND_NINO"
    ],
    "create_date_from": "2021-05-07",
    "create_date_end": "2021-05-10"
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
{
    "ask": "Success",
    "message": "Success",
    "data": [
        {
            "reference_no": "RVG296-210329-0001",
            "ref_no": "RVG296-210329-0001",
            "application_code": "Putaway",
            "application_code_text": "入库上架",
            "product_barcode": "G296-ALI-AND-NINO3",
            "product_sku": "ALI-AND-NINO3",
            "warehouse_code": "USEA",
            "warehouse_name": "美东仓库",
            "inventory_change_type": 1,
            "inventory_change_type_text": "新增",
            "ibl_change_quantity": 2,
            "remark": "",
            "ibl_add_time": "2021-05-07 11:38:26"
        }
    ],
    "count": 1
}
请求JSON

参数名	数据类型	是否必填	说明	示例
pageSize	Int	Required	每页数据长度，最大值为200	10
page	Int	Required	当前页	1
application_code	Int	Optional	操作类型
1：调出下架，
2：调入上架，
3：盘点，
4：订单签出，
5：库存调整，
6：售后上架，
7：入库上架
8：增值完成
3
warehouse_code	String	Optional	仓库代码	USEA
product_sku_list	String[]	Optional	多个SKU，数组格式，精确匹配。	["ALI_AND_NABC_INO", "IND_KGRN_AD_KO"]
reference_no_list	String[]	Optional	操作单号, 数组格式	["RVG296-210518-0016", "RVG296-210329-0001"]
create_date_from	datetime	Required	操作开始时间, 格式YYYY-MM-DD	2021-05-07
create_date_end	datetime	Required	操作结束时间, 格式YYYY-MM-DD。最大时间跨度为31天	2021-05-10
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
count	Int	总数量
data	Object[]	数据内容
data参数

参数名	数据类型	说明
reference_no	String	操作单号
ref_no	String	参考号
application_code	String	操作类型
product_sku	String	商品编码 (不带客户编码)
warehouse_code	String	仓库代码
warehouse_name	String	仓库名称
inventory_change_type	Int	变动类型（1：新增，2：减少）
ibl_change_quantity	Int	变动量
remark	String	备注
ibl_add_time	String	操作时间




RESTFUL获取库龄列表
这是RESTFUL WEB API，接入方式请参见GD开放平台(V2)接入指引。
URLhttps://oms.goodcang.net/public_open/inventory/inventory_age_list
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
     "product_sku_list": [],
     "product_title": "",
     "product_title_en": "",
     "fifo_time_from": "2021-04-11 00:00:00",
     "fifo_time_to": "2021-10-14 23:59:59",
     "page": 1,
     "page_size": 20
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
    "code":0,
    "message":"success",
    "data":{
        "count":476,
        "list":[
            {
                "warehouse_code":"USEA",
                "product_sku":"20200114-AAAAAAAAAAAAAAA",
                "iba_quantity":1932,
                "iba_fifo_time":"2020-01-14",
                "iba_warning_age":90,
                "product_title":"中国特产hhh",
                "product_title_en":"goodcang",
                "warehouse_desc":"美东仓库",
                "warehouse_age":671
            },
            {
                "warehouse_code":"USEA",
                "product_sku":"20200114-BBBBBBBBBBBBBBB",
                "iba_quantity":3150,
                "iba_fifo_time":"2020-01-14",
                "iba_warning_age":90,
                "product_title":"中国特产hhh",
                "product_title_en":"goodcang",
                "warehouse_desc":"美东仓库",
                "warehouse_age":671
            }
        ]
    }
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
product_sku_list	String[]	Optional		商品编码列表(最多200个元素)	
product_title	String	Optional		商品名称	
product_title_en	String	Optional		商品英文名称	
fifo_time_from	String	Optional		上架时间起始值
北京时间, 时间区间参数必须成对提交
2021-04-11 00:00:00
fifo_time_to	String	Optional		上架时间末位值
北京时间，时间区间参数必须成对提交
2021-10-14 23:59:59
age_from	Int	Optional		库龄起始值	
age_to	Int	Optional		库龄末位值	
quantity_from	Int	Optional		在库库存起始值	
quantity_to	Int	Optional		在库库存末位值	
warning_age_type	Int	Optional		库龄预警， 枚举类型
1：超出
2：未超出
warehouse_code	String	Optional		仓库代码	
page	Int	Required		分页页码	1
page_size	Int	Required		分页数量(最大200)	20
响应JSON

参数名	数据类型	说明
code	Int	0 成功，其它值表示失败。
message	String	文本消息
data	Object	详情参考InventoryAgeListResp
InventoryAgeListResp数据结构

参数名	数据类型	可为空	说明
total	Int	False	总数量
list	Object[]	False	列表数据 详见InventoryAgeItemResp
InventoryAgeItemResp数据结构

参数名	数据类型	可为空	说明
warehouse_code	String	False	仓库代码
product_sku	String	False	商品编码
iba_quantity	Int	False	在库库存
iba_fifo_time	String	False	上架时间（北京时间）
iba_warning_age	Int	False	预警库龄
product_title	String	False	商品中文名称
product_title_en	String	False	商品英文名称
warehouse_desc	String	False	仓库名称
warehouse_age	Int	False	库龄
expiration_date	String	False	过期日期
