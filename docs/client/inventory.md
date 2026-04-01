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