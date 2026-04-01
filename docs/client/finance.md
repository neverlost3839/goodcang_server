RESTFUL V1获取仓租信息
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
说明：获取 客户在系统中的仓租信息
URLhttps://oms.goodcang.net/public_open/finance/get_wh_inventory_storage
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
    "page": 1,
    "pageSize": 20,
    "ow_id_charge": "USWE",
    "wis_code": "WTG296-4-20170904",
    "dateFrom": "2014-01-01 12:22:32",
    "dateTo": "2019-01-01 12:22:32"
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
{
    "ask": "Success",
    "message": "Success",
    "count": "1",
    "Error": "",
    "data": [
        {
            "wis_code": "WTG296-4-20170904",
            "wp_settlement_cycle": "日结",
            "ow_id_charge": "USWE",
            "is_date": "2017-09-04",
            "isdb_volume": "1.660",
            "is_amount": "0.366",
            "currency_code": "USD",
            "note": "2017年09月04日仓租"
        }
    ]
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
wis_code	String	Optional	32	单号	WT000010-1-20200722
ow_id_charge	String	Optional	32	仓库代码	USEA
dateFrom	Date	Optional	datetime	开始时间
格式:Y-m-d H:i:s
如果开始时间和截止时间都不填，则默认查询一个月。
2020-07-21 09:30:00
dateTo	Date	Optional	datetime	截至时间
格式:Y-m-d H:i:s
如果开始时间和截止时间都不填，则默认查询一个月。
2020-07-21 09:30:00
page	Int	Required		查询页数，不传值则默认第1页	1
pageSize	Int	Required		每页显示数量
不传值则默认10条数量，大于100查询100	20
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
count	Int	总数量
data	Object	数据内容
data参数

参数名	数据类型	说明
wis_code	String	单号
wp_settlement_cycle	String	结算周期
ow_id_charge	String	仓库代码
is_date	Date	发生时间 Y:m:d
isdb_volume	String	体积(m3)
is_amount	String	计费总金额
currency_code	String	计费货币
is_settlement_amount	String	结算总金额
settlement_currency_code	String	结算货币
note	String	


RESTFUL V1获取仓租明细
这是RESTFUL WEB API(V1)，接入方式请参见GD开放平台(V1/V2)接入指引。
说明：根据仓租单号(wis_code)获取仓租明细
URLhttps://oms.goodcang.net/public_open/finance/get_wh_inventory_storage_detail
METHODPOST
请求JSON示例

1
2
3
{
    "wis_code": "WTG296-8-20181018"
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
{
    "ask": "Success",
    "message": "Success",
    "data": [
        {
            "wis_code": "WTG296-8-20181022",
            "product_barcode": "G296-BATTERY_005",
            "product_name": "BATTERY",
            "reference_no": "00123",
            "charge_date": "2018-10-22",
            "putaway_date": "2017-08-25 00:00:00",
            "length": "10.00",
            "width": "5.00",
            "height": "5.00",
            "quantity": "1",
            "volume": "0.001",
            "bill_amount": "0.000",
            "bill_currency_code": "GBP",
            "settlement_amount": "0.000",
            "settlement_currency_code": "USD",
            "day": "423",
            "peak_season_surcharge": "1",
            "isdb_amount": "5",
            "warehouse_code": "UK",
            "storage_shape": "箱",
            "bill_unit": "数量"
        }
    ],
    "count": 6
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
wis_code	String	Required	32	单号	WT000010-1-20200722
响应JSON

参数名	数据类型	说明
ask	String	Success 成功，其它值表示失败。
message	String	文本消息
这是V1版本API，所以响应结构为V1版本，请开者注意区别。
count	Int	总数量
data	Object[]	仓租明细数组，数组对象结构参见WarehouseRentDetailItemResp
WarehouseRentDetailItemResp 对象

参数名	数据类型	说明
wis_code	String	单号
product_barcode	String	产品代码
product_name	String	产品名称
reference_no	String	参考编号
charge_date	Datetime	计费时间
putaway_date	Datetime	上架时间
length	Float	长(cm)
width	Float	宽(cm)
height	Float	高(cm)
quantity	Int	数量
volume	Float	体积(m3)
bill_amount	Float	计费金额
bill_currency_code	String	计费币种
settlement_amount	Float	结算金额
settlement_currency_code	String	结算币种
day	Int	库龄(天)
peak_season_surcharge	String	旺季附加费
isdb_amount	String	仓租金额
warehouse_code	String	仓库代码
storage_shape	String	存储物理形态
储位盒
箱
托
件
bill_unit	String	计费单位，如： 数量，体积，数量/月均，数量/天，体积/天



RESTFUL获取费用流水
这是RESTFUL WEB API，接入方式请参见GD开放平台(V2)接入指引。
URLhttps://oms.goodcang.net/public_open/finance/cost_flow_list
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
    "types_of_fee":"",
    "flow_type":"",
    "order_number":"",
    "account_code":"",
    "business_type": 0,
    "currency_code":"",
    "charge_type":0,
    "page": 1,
    "page_size": 10,
    "happen_start_time": "2021-09-13 00:00:00",
    "happen_end_time": "2021-10-14 23:59:59",
    "number_type": "order_number",
    "next_page_token": ""
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
{
    "code": 0,
    "message": "success",
    "data": {
        "list": [
            {
                "order_number": "SFG296-211014-0003",
                "reference_number": "SFG296-211014-0003",
                "account_code": "ACG29602",
                "types_of_fee_name_cn": "仓租附加费",
                "types_of_fee_name_en": "kunei-a",
                "flow_type": 1,
                "flow_type_text": "扣款",
                "amount": "37535.69",
                "currency_code": "GBP",
                "currency_balance": "74059292.024",
                "currency_balance_text": "74059292.024 GBP",
                "exchange_rate": "1",
                "add_time": "2021-10-15 03:44:56",
                "source": "1",
                "types_of_fee": "kunei1",
                "types_of_fee_text": "仓租附加费",
                "charge_type": 0,
                "charge_type_text": "未出账",
                "remark": null,
                "business_type": "0",
                "business_type_text": "海外仓储",
                "id": "144873315125869690"
            }
        ],
        "next_page_token": "",
        "prev_page_token": "",
        "total"=> 999
    }
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
flow_type	String	Optional		流水类型，(枚举类型)
0: 入款
1: 扣款
2: 冻结
3: 解冻
1
number_type	String	Optional		单号类型，(枚举类型，参数必须与order_number成对提交)
"order_number": 单号
"reference_number": 参考号
order_number
order_number	String	Optional		单号（订单号或者参考号的值，参数必须与number_type成对提交）	
account_code	String	Optional		账户编号	ACCOUNT_CODE_STRING
business_type	Int	Optional		业务类型，(枚举类型)
"0": 海外仓储
"1":中转代发
0
types_of_fee	String	Optional		费用类型(具体详见获取费用类型接口)	CBC
currency_code	String	Optional		币种(具体参见获取货币列表接口)	JPY
charge_type	Int	Optional		业务类型，(枚举类型)
"0": 未出账
"1":已出账
"2":出账中
0
page	Int	Required		当前分页	1
page_size	Int	Required		分页数量(最大200)	20
happen_start_time	String	Required		发生开始时间
时间跨度最大为365天（北京时间, 时间区间参数必须一起提交）
2021-09-13 00:00:00
happen_end_time	String	Required		发生结束时间
时间跨度最大为365天（北京时间, 时间区间参数必须一起提交）
2021-10-14 00:00:00
next_page_token	String	Optional	200	下一页token
当请求分页数据 > 5000条时，next_page_token, prev_page_token 必填其一
next_page_token, prev_page_token 不能同时存在，
因为有矛盾（翻下一页，或上一页是根据这个token而定的）。
prev_page_token	String	Optional	200	上一页token
当请求分页数据 > 5000条时，next_page_token, prev_page_token 必填其一。
next_page_token, prev_page_token 不能同时存在，
因为有矛盾（翻下一页，或上一页是根据这个token而定的）。
响应JSON

参数名	数据类型	说明
code	Int	0 成功，其它值表示失败。
message	String	文本消息
data	Object	参见 CostStatementListResp类型
CostStatementListResp类型

参数名	数据类型	可为空	说明
total	Int	False	总数量
list	Object[]	False	列表数据 参见CostStatementItemResp类型
next_page_token	String	True	超过5000时的下一页token
当请求分页数据 > 5000条时，不再支持页码跳转（page参数暂时失效），
要根据出参的next_page_token/prev_page_token查询上一页/下一页数据。
prev_page_token	String	True	超过5000时的上一页token
当请求分页数据 > 5000条时，不再支持页码跳转（page参数暂时失效），
要根据出参的next_page_token/prev_page_token查询上一页/下一页数据。
CostStatementItemResp类型

参数名	数据类型	可为空	说明
order_number	String	False	单号
reference_number	String	True	交易流水号
account_code	String	False	账户编码
types_of_fee_name_cn	String	True	费用代码中文名称
types_of_fee_name_en	String	True	费用代码英文名称
flow_type	String	False	流水类型
flow_type_text	String	False	流水类型文本
amount	String	False	发生金额
currency_code	String	False	币种
currency_balance	String	False	当前账户币种余额
exchange_rate	String	True	汇率
types_of_fee_text	String	True	费用类型编码描述
charge_type_text	String	True	出账状态
add_time	String	False	发生时间（北京时间）




RESTFUL获取充值明细
这是RESTFUL WEB API，接入方式请参见GD开放平台(V2)接入指引。
URLhttps://oms.goodcang.net/public_open/finance/top_up_record
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
    "code_field": "reference_number",
    "begin_add_time": "2021-04-11 00:00:00",
    "end_add_time": "2021-10-14 23:59:59",
    "page": 1,
    "page_size": 10,
    "code_value":"",
    "transaction_gd_status":0,
    "bank_name":"宁波银行",
    "account_code":""
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
{
    "code": 0,
    "message": "success",
    "data": {
        "list":[
            {
                "order_number": "412344124",
                "reference_number": null,
                "account_code": "ACG29608",
                "sign_body_name": "测试企业",
                "service_body_type": 0,
                "service_body_name": "4123414",
                "sign_business_type_list": [
                    0
                ],
                "sign_business_type_text": "海外仓储",
                "drawee": "测试P卡",
                "transaction_type": 3,
                "transaction_type_text": "Payoneer",
                "bank_name": "P卡（TRE）",
                "drawee_account": "testpppppp",
                "transaction_status": 2,
                "transaction_status_text": "已废弃",
                "register_amount": "2",
                "arrival_amount": "11.75",
                "currency_code": "USD",
                "exchange": "6.5297",
                "add_time": "2021-07-27 09:41:23",
                "service_charge": "0",
                "recharge_code": "RMB",
                "actual_amount": "0",
                "remark": "p卡充值失败，自动废弃",
                "serial_number": "",
                "update_time": "2021-07-27 11:17:39"
            }
        ],
        "total": 12132
    }
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
code_field	String	Required		单号类型，(枚举类型)
"reference_number": 银行流水号
"order_number": 充值单号
reference_number
code_value	String	Optional		字段值	order_number
transaction_type	Int	Optional		充值交易类型，(枚举类型)
0: 余额转汇（转入）
1: 余额转汇（转出）
2: 银行转账
3: Payoneer
4: 自动转汇（转入）
5: 自动转汇（转出）
6: 原件返利
7: 退件返利
8: 现金支付
9: 主体余额转移（转入）
10: 主体余额转移（转出）
11: 调增充值
12: 调减充值
0
transaction_gd_status	Int	Optional		交易状态，(枚举类型)
0: 待处理
1: 已到账
2: 已废弃
3: 草稿
4: 审核异常
5: 驳回
0
bank_name	String	Optional		付款银行名称(参见银行列表接口)	招商银行
account_code	String	Optional		账户编码	
begin_add_time	String	Optional		充值开始日期
北京时间，186天跨度, 时间区间参数必须一起提交 
2021-07-27 00:41:23
end_add_time	String	Optional		充值结束日期
北京时间，186天跨度，时间区间参数必须一起提交
2021-07-27 12:41:23
page	Int	Required		分页标签	
page_size	Int	Required		分页数量(最大200)	20
响应JSON

参数名	数据类型	说明
code	Int	0 成功，其它值表示失败。
message	String	文本消息
data	Object	详见TopUpRecordResp参数
TopUpRecordResp数据结构

参数名	数据类型	说明
list	Object[]	详见TopUpRecordItemResp数据结构
total	Int	总数
TopUpRecordItemResp数据结构

参数名	数据类型	可为空	说明
order_number	String	False	单号
reference_number	String	True	交易流水号
account_code	String	False	账户编码
sign_body_name	String	False	签约主体名称
service_body_name	String	False	服务主体名称
sign_business_type_text	String	True	签约业务类型
drawee	String	True	付款人
transaction_type_text	String	False	交易方式文本
bank_name	String	True	付款银行
drawee_account	String	True	付款银行账号
transaction_status_text	String	False	审核状态
register_amount	String	False	登记金额
arrival_amount	String	False	到账金额
actual_amount	String	False	实收金额
currency_code	String	False	币种，比如USD
exchange	String	False	转汇汇率
add_time	String	False	充值时间（北京时间）
recharge_code	String	False	充值币种
update_time	String	False	到账时间（北京时间）



RESTFUL获取账单列表
这是RESTFUL WEB API，接入方式请参见GD开放平台(V2)接入指引。
URLhttps://oms.goodcang.net/public_open/finance/billing_list
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
    "bill_number": "",
    "account_code": "",
    "begin_bill_to_time": "2021-04-12 00:00:00",
    "end_bill_to_time": "2021-10-15 23:59:59",
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
{
    "code": 0,
    "message": "success",
    "data": {
        "total": 2,
        "list": [
            {
                "bill_number": "B20210728G2960029",
                "account_code": "ACG29603",
                "bill_from_time": "2021-06-01 00:00:00",
                "bill_to_time": "2021-07-27 23:59:59",
                "bill_file_path": "FILE_PATH",
                "sign_body_name": "3412341243",
                "sign_business_type_list_text": "3412341243",
                "service_body_name": "3412341243",
                "all_total": [
                    {
                        "currency_code": "JPY",
                        "balance": "0"
                    }
 
                ],
                "start_balance": [
                    {
                        "currency_code": "CZK",
                        "balance": "0"
                    }
                ],
                "end_balance": [
                    {
                        "currency_code": "CZK",
                        "balance": "0"
                    }
                ],
                "cash_back_balance": [
                    {
                        "currency_code": "CZK",
                        "balance": "0"
                    }
                ]
            }
        ]
    }
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
bill_number	String	Optional		账单号	
begin_bill_to_time	String	Optional		账单截至时间开始
北京时间, 186天跨度, 时间区间参数必须一起提交
2021-04-12 00:00:00
end_bill_to_time	String	Optional		账单截至时间结束
北京时间, 186天跨度, 时间区间参数必须一起提交
2021-10-15 23:59:59
account_code	String	Optional		账户编码（不传则查询所有账户）	
page	Int	Required		分页标签	1
page_size	Int	Required		分页数量(最大200)	10
响应JSON

参数名	数据类型	说明
code	Int	0 成功，其它值表示失败。
message	String	文本消息
data	Object[]	详见参见 BillingListResp类型
BillingListResp数据结构

参数名	数据类型	说明
list	Object[]	参见BillingItemResp类型
total	Int	总数
BillingItemResp数据结构

参数名	数据类型	可为空	说明
bill_number	String	False	交易流水号
account_code	String	False	账户编码
bill_from_time	String	False	账单开始日期
bill_to_time	String	False	账单结束日期
bill_file_path	String	False	账单文件地址
sign_body_name	String	False	签约主体
sign_business_type_list_text	String	False	签约业务
service_body_name	String	False	服务主体
all_total	Object[]	False	账单总金额 参见BillFundsResp类型
start_balance	Object[]	False	期初余额 参见BillFundsResp类型
end_balance	Object[]	False	期末余额 参见BillFundsResp类型
cash_back_balance	Object[]	False	返现金额 参见BillFundsResp类型
BillFundsResp数据结构

参数名	数据类型	可为空	说明
currency_code	String	False	币种
balance	String	False	金额





RESTFUL获取货币列表
这是RESTFUL WEB API，接入方式请参见GD开放平台(V2)接入指引。
URLhttps://oms.goodcang.net/public_open/finance/currency_rate_list
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
{
     "code": 0,
     "message": "success",
     "data": [
         {
             currency_code: "JPY",
             currency_name: "日元",
             symbol: "¥JPY"
         }
   ]
 }
响应JSON

参数名	数据类型	说明
code	Int	0 成功，其它值表示失败。
message	String	文本消息
data	Object[]	参见 CurrencyRateItemResp类型
CurrencyRateItemResp数据类型

参数名	数据类型	可为空	说明
currency_code	string	False	货币缩写
currency_name	String	False	货币名称
symbol	String	False	货币标识符




RESTFUL获取银行列表
这是RESTFUL WEB API，接入方式请参见GD开放平台(V2)接入指引。
URLhttps://oms.goodcang.net/public_open/finance/my_bank_list
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
{
    "code": 0,
    "message": "success",
    "data": [
        {
            bank_code: "P01",
            bank_name: "中国工商银行",
            bank_name_cn: "中国工商银行",
            bank_name_en: "ICBC",
            is_third: "1"
        }
  ]
}
响应JSON

参数名	数据类型	说明
code	Int	0 成功，其它值表示失败。
message	String	文本消息
data	Object[]	数组元素类型, 参见BankListItemResp类型
BankListItemResp数据类型

参数名	数据类型	可为空	说明
bank_code	String	True	银行编码
bank_name	String	True	银行名称
bank_name_cn	String	True	银行中文名
bank_name_en	String	True	银行英文名
is_third	String	True	是否第三方, 1:是 0:否
