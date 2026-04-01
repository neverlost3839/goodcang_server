RESTFUL获取查件列表
这是RESTFUL WEB API，接入方式请参见GD开放平台(V2)接入指引。
URLhttps://oms.goodcang.net/public_open/assistant/logistic_ticket_list
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
    "code_type": "order_code",
    "code_value_list": [],
    "time_type": "add_time",
    "time_start": "",
    "time_end": "",
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
{
    "code": 0,
    "message": "success",
    "data": [
        {
            "io_code": "CJ202110210001",
            "order_code": "G296-211021-0002",
            "tracking_no": "MR014119393RM",
            "it_type_name": "无ASCAN",
            "warehouse_code": "USEA",
            "warehouse_name": "美东仓库",
            "sm_name": "MORKRM-单箱",
            "add_time": "2021-10-21 16:46:07",
            "commit_time": "2021-10-21 16:46:07",
            "last_handle_time": "",
            "reply_time": "",
            "io_status_text": "待处理",
            "trail_status_text": "",
            "customer_service_reply": "",
            "replay_attachment_file_list": []
        }
    ]
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
code_type	String	Required		查单类型，(枚举类型)
"io_code":查件单号
"order_code":订单号
"tracking_no":追踪号
io_code
code_value_list	String[]	Optional		单号值,用数组传递(最多200个元素)	["CJ302107210002"]
io_status	Int	Optional		查件状态，(枚举类型)
1:草稿
2:待处理
3:处理中
7:已回复
8:完结
10:废弃
11:驳回)
trail_status	String	Optional		轨迹状态，(枚举参见下述轨迹TrackingCode类型)	
warehouse_code	String	Optional		仓库编码	USAE
sm_code	String	Optional		物流方式编码	FEDEX-SMALLPARCEL
platform	String	Optional		销售平台(大写字母)	AMAZON
it_type_id	Int	Optional		查件类型ID，详见查件类型列表接口	
time_type	String	Optional		时间类型，(枚举类型，存在时间区间参数时，此项必填)
"add_time":创建时间
"commit_time":提交时间
"reply_time":回复时间
add_time
time_start	String	Optional		开始时间（北京时间，186天跨度, 时间区间参数必须一起提交）	2021-04-19 00:00:00
time_end	String	Optional		结束时间（北京时间，186天跨度, 时间区间参数必须一起提交）	2021-10-22 23:59:59
page	Int	Required		分页页码	1
page_size	Int	Required		分页数量(最大200)	20
TrackingCode数据类型

TMS轨迹代码（新）	轨迹描述	备注	总原则
TMS_NTI	查无轨迹	查无轨迹	
TMS_OC	订单创建	订单创建，服务商收到订单信息	
TMS_AS	预上网	预上网	
TMS_PU	揽件完毕	服务商揽件完毕	当揽收节点重复出现时，系统需取时间节点最早出现的轨迹映射为揽收
TMS_IT	运输中	货物运输途中（如到达某网点，到达某分拨中心等）	
TMS_OD	派送中	货物到达目的地城市，准备派送给收方	
TMS_WPU	到达目的地	货物到达目的地城市，等待客户上门取件	
TMS_RT	退回寄放	退回给寄放	
TMS_EXCP	轨迹异常	轨迹异常（如货物无法投递，因服务商原因导致延迟等）	
TMS_FD	派送完毕	派送完毕（如妥投，货物放在门口等）	订单超过30个自然日，无签收轨迹，系统默认为签收。以订单预报时间为起始时间
TMS_DF	投递未遂	投递未遂（如客户不在家）	
TMS_UN	无法匹配	指对抓回的轨迹系统找不到相应的匹配关系	
TMS_NP	未变化	未变化	
TMS_YD	预签收	预签收	
响应JSON

参数名	数据类型	说明
code	Int	0 成功，其它值表示失败。
message	String	文本消息
data	Object	详见LogisticTicketListDataResp参数
LogisticTicketListDataResp数据结构

参数名	数据类型	可为空	说明
total	Int	False	总数量
list	Object[]	False	列表数据 详见LogisticTicketListItem
LogisticTicketListItem数据结构

参数名	数据类型	可为空	说明
io_code	String	False	查件号
order_code	String	False	订单号
tracking_no	String	False	跟踪号
it_type_name	String	False	查件类型名
warehouse_code	String	False	仓库代码
warehouse_name	String	False	仓库名称
sm_name	String	True	物流产品
add_time	String	True	创建时间（北京时间）
commit_time	String	True	提交时间（北京时间）
last_handle_time	String	True	处理时间（北京时间）
reply_time	String	True	回复时间（北京时间）
io_status	Int	True	查件状态
1:草稿
2:待处理
3:处理中
7:已回复
8:完结
10:废弃
11:驳回
io_status_text	String	True	查件状态文本
trail_status	String	True	物流状态
枚举参见 TrackingCode 类型
trail_status_text	String	True	物流状态文本
customer_service_reply	String	True	客服回复
replay_attachment_file_list	Object[]	True	回复附件列表, 参见ReplyAttachmentItemResp类型
ReplyAttachmentItemResp数据结构

参数名	数据类型	可为空	说明
url	String	False	链接
name	String	False	名称





RESTFUL获取查件单类型列表
这是RESTFUL WEB API，接入方式请参见GD开放平台(V2)接入指引。
通过物流编码，查询该物流方式支持哪些查件操作，用户再根据需求选择相应的查件申请。
URLhttps://oms.goodcang.net/public_open/assistant/logistic_ticket_type_list
METHODPOST
请求JSON示例

1
2
3
{
    "sm_code":"SM_CODE"
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
{
    "code": 0,
    "message": "success",
    "data": [
        {
          "name": "无ASCAN",
          "value": 1
        },
        {
          "name": "拦截/改派",
          "value": 2
        }
    ]
 
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
sm_code	String	Optional	30	物流方式编码	
响应JSON

参数名	数据类型	说明
code	Int	0 成功，其它值表示失败。
message	String	文本消息
data	Object[]	参见IOTypeResp类型
IOTypeResp数据类型

参数名	数据类型	可为空	说明
name	String	False	类型名称
value	Int	False	值




RESTFUL获取查件单详情
这是RESTFUL WEB API，接入方式请参见GD开放平台(V2)接入指引。
URLhttps://oms.goodcang.net/public_open/assistant/logistic_ticket_detail
METHODPOST
请求JSON示例

1
2
3
{
    "io_code":"IOCODE"
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
{
    "code": 0,
    "message": "success",
    "data": {
        "base_info": {
            "io_code": "XX202107210002",
            "io_status_text": "废弃",
            "customer_emails": "e@e.com",
            "add_time": "2021-07-21 14:33:29",
            "io_desc": "cccccc",
            "it_type_name": "无ASCAN",
            "commit_time": "2021-07-21 14:33:29",
            "finish_time": "",
            "last_handle_time": "2021-09-16 18:06:07",
            "reply_time": "",
            "order_code": "G000-210610-0004",
            "tracking_no": "MR013942365RM",
            "attachment_file_list": [
                {
                    "name": "xxx",
                    "url": "xxxxxxxx"
                },
                {
                    "name": "xxx",
                    "url": "xxxxxxxx"
                }
            ],
            "service_reply_list": [
                {
                    "handle_result": "",
                    "handle_user": "",
                    "attachment_file_list": [
                        {
                            "name": "xxx",
                            "url": "xxxxxxxx"
                        },
                        {
                            "name": "xxx",
                            "url": "xxxxxxxx"
                        },
                        {
                            "name": "xxxx",
                            "url": "xxxxxx"
                        }
                    ]
                }
            ]
        },
        "order_info": {
            "order_code": "G000-210610-0004",
            "platform": "OTHER",
            "reference_no": "",
            "is_return": 0,
            "sm_name": null,
            "order_status_text": "已发货",
            "tracking_number": "XX0139***365RM",
            "create_type_text": "手动创建",
            "warehouse_code": "USEA",
            "fba_shipment_id": "",
            "real_weight": "0.000",
            "real_length": "0.000"
        },
        "recheck_info": null,
        "appeal_info": null,
        "log_info": {
            "list": [
                {
                    "handle_user": "系统",
                    "io_status_text": "驳回",
                    "add_time": "2021-09-16 18:06:07"
                },
                {
                    "handle_user": "系统",
                    "io_status_text": "处理中",
                    "add_time": "2021-07-21 14:34:29"
                },
                {
                    "handle_user": "G296",
                    "io_status_text": "待处理",
                    "add_time": "2021-07-21 14:33:29"
                }
            ]
        }
    }
}
请求JSON

参数名	数据类型	是否必填	最大数据长度	说明	示例
io_code	String	Required		查件单号	
响应JSON

参数名	数据类型	说明
code	Int	0 成功，其它值表示失败。
message	String	文本消息
data	Object	参考LogisticTicketDetailDataResp类型
LogisticTicketDetailDataResp数据结构

参数名	数据类型	可为空	说明
base_info	Object	False	基本信息,参见LogisticTicketDetailBaseInfo类型
order_info	Object	False	订单信息,参见LogisticTicketDetailOrderInfo类型
recheck_info	Object	True	复查信息,参见LogisticTicketDetailRecheckAppealInfo类型
appeal_info	Object	True	申诉信息,参见LogisticTicketDetailRecheckAppealInfo类型
log_info	Object	False	日志信息,参见LogisticTicketDetailLogInfo类型
LogisticTicketDetailBaseInfo数据结构

参数名	数据类型	可为空	说明
io_code	String	False	查件号
io_status_text	String	False	查件状态文本
customer_emails	String	False	通知邮箱\|客户邮箱（多个用逗号隔开）
add_time	String	False	创建时间（北京时间）
io_desc	String	False	查件需求\|问题描述
it_type_name	String	False	查件类型名称
commit_time	String	True	提交时间（北京时间）
finish_time	String	True	完结时间（北京时间）
last_handle_time	String	True	处理时间（北京时间）
reply_time	String	True	回复时间（北京时间）
order_code	String	False	订单号
tracking_no	String	False	跟踪号
attachment_file_list	Object[]	False	提交附件，详见InvestigateListAttachmentItemResp数据结构
service_reply_list	Object[]	False	处理回复信息，详见InvestigateDetailServiceReplyItemResp数据结构
InvestigateDetailServiceReplyItemResp数据结构

参数名	数据类型	可为空	说明
handle_result	String	True	回复结果
handle_user	String	False	处理人
attachment_file_list	Object[]	False	详见InvestigateListAttachmentItemResp数据结构
InvestigateListAttachmentItemResp数据结构

参数名	数据类型	可为空	说明
name	String	True	名称
url	String	False	链接地址
LogisticTicketDetailOrderInfo数据结构

参数名	数据类型	可为空	说明
order_code	String	True	订单号
platform	String	True	销售平台
reference_no	String	True	参考号
is_return	Int	True	是否退件
-1:全部
0:否
1:是
sm_name	String	True	物流方式名称
order_status_text	String	False	订单状态文本
tracking_number	String	True	跟踪号
create_type_text	String	True	订单来源文本
warehouse_code	String	True	发货仓库编码
fba_shipment_id	String	True	发货仓库编码
real_weight	String	False	实际重(KG)
real_length	String	False	实际尺寸(CM)
LogisticTicketDetailRecheckAppealInfo数据结构

参数名	数据类型	可为空	说明
list	Object[]	False	参见LogisticTicketDetailRecheckAppealInfoItem类型
LogisticTicketDetailRecheckAppealInfoItem数据结构

参数名	数据类型	可为空	说明
add_time	String	True	复查/申诉时间
attachment_file_list	Object[]	True	申诉附件 参见InvestigateListAttachmentItem类型
io_desc	String	True	申诉需求
handle_info	Object[]	True	回复结果 参见InvestigateHandleinfo类型
reply_time	String	True	回复时间
InvestigateHandleinfo数据结构

参数名	数据类型	可为空	说明
result	String	False	回复结果信息
attachment_file_list	Object[]	False	回复附件, 参见InvestigateListAttachmentItem类型
InvestigateListAttachmentItem数据结构

参数名	数据类型	可为空	说明
name	String	True	附件名称
url	String	True	附件地址
LogisticTicketDetailLogInfo数据结构

参数名	数据类型	可为空	说明
list	Object[]	False	参见LogisticTicketDetailLogInfoItem类型
LogisticTicketDetailLogInfoItem数据类型

参数名	数据类型	可为空	说明
handle_user	String	True	附件操作人
io_status_text	String	False	状态查件状态文本
add_time	String	True	操作时间
