from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field


class ReplyAttachmentItem(BaseModel):
    url: str = Field(..., description="链接")
    name: str = Field(..., description="名称")

    class Config:
        from_attributes = True


class LogisticTicketListItem(BaseModel):
    io_code: str = Field(..., description="查件号")
    order_code: str = Field(..., description="订单号")
    tracking_no: str = Field(..., description="跟踪号")
    it_type_name: Optional[str] = Field(None, description="查件类型名")
    warehouse_code: str = Field(..., description="仓库代码")
    warehouse_name: str = Field(..., description="仓库名称")
    sm_name: Optional[str] = Field(None, description="物流产品")
    add_time: Optional[str] = Field(None, description="创建时间")
    commit_time: Optional[str] = Field(None, description="提交时间")
    last_handle_time: Optional[str] = Field(None, description="处理时间")
    reply_time: Optional[str] = Field(None, description="回复时间")
    io_status: Optional[int] = Field(None, description="查件状态")
    io_status_text: Optional[str] = Field(None, description="查件状态文本")
    trail_status: Optional[str] = Field(None, description="物流状态")
    trail_status_text: Optional[str] = Field(None, description="物流状态文本")
    customer_service_reply: Optional[str] = Field(None, description="客服回复")
    replay_attachment_file_list: List[ReplyAttachmentItem] = Field(
        default_factory=list, description="回复附件列表"
    )

    class Config:
        from_attributes = True


class LogisticTicketListData(BaseModel):
    total: int = Field(..., description="总数量")
    list: List[LogisticTicketListItem] = Field(..., description="列表数据")

    class Config:
        from_attributes = True


class LogisticTicketListOut(BaseModel):
    code: int = Field(..., description="0成功,其它值失败")
    message: str = Field(..., description="文本消息")
    data: Optional[LogisticTicketListData] = Field(None, description="数据")

    class Config:
        from_attributes = True


class IOTypeItem(BaseModel):
    name: str = Field(..., description="类型名称")
    value: int = Field(..., description="值")

    class Config:
        from_attributes = True


class LogisticTicketTypeListOut(BaseModel):
    code: int = Field(..., description="0成功,其它值失败")
    message: str = Field(..., description="文本消息")
    data: List[IOTypeItem] = Field(default_factory=list, description="查件类型列表")

    class Config:
        from_attributes = True


class InvestigateDetailServiceReplyItem(BaseModel):
    handle_result: Optional[str] = Field(None, description="回复结果")
    handle_user: str = Field(..., description="处理人")
    attachment_file_list: List[ReplyAttachmentItem] = Field(
        default_factory=list, description="回复附件"
    )

    class Config:
        from_attributes = True


class LogisticTicketDetailBaseInfo(BaseModel):
    io_code: str = Field(..., description="查件号")
    io_status_text: str = Field(..., description="查件状态文本")
    customer_emails: str = Field(..., description="通知邮箱")
    add_time: str = Field(..., description="创建时间")
    io_desc: str = Field(..., description="查件需求")
    it_type_name: str = Field(..., description="查件类型名称")
    commit_time: Optional[str] = Field(None, description="提交时间")
    finish_time: Optional[str] = Field(None, description="完结时间")
    last_handle_time: Optional[str] = Field(None, description="处理时间")
    reply_time: Optional[str] = Field(None, description="回复时间")
    order_code: str = Field(..., description="订单号")
    tracking_no: str = Field(..., description="跟踪号")
    attachment_file_list: List[ReplyAttachmentItem] = Field(
        default_factory=list, description="提交附件"
    )
    service_reply_list: List[InvestigateDetailServiceReplyItem] = Field(
        default_factory=list, description="处理回复信息"
    )

    class Config:
        from_attributes = True


class LogisticTicketDetailOrderInfo(BaseModel):
    order_code: Optional[str] = Field(None, description="订单号")
    platform: Optional[str] = Field(None, description="销售平台")
    reference_no: Optional[str] = Field(None, description="参考号")
    is_return: Optional[int] = Field(None, description="是否退件")
    sm_name: Optional[str] = Field(None, description="物流方式名称")
    order_status_text: str = Field(..., description="订单状态文本")
    tracking_number: Optional[str] = Field(None, description="跟踪号")
    create_type_text: Optional[str] = Field(None, description="订单来源文本")
    warehouse_code: Optional[str] = Field(None, description="发货仓库编码")
    fba_shipment_id: Optional[str] = Field(None, description="发货仓库编码")
    real_weight: Optional[str] = Field(None, description="实际重(KG)")
    real_length: Optional[str] = Field(None, description="实际尺寸(CM)")

    class Config:
        from_attributes = True


class InvestigateHandleinfo(BaseModel):
    result: str = Field(..., description="回复结果信息")
    attachment_file_list: List[ReplyAttachmentItem] = Field(
        default_factory=list, description="回复附件"
    )

    class Config:
        from_attributes = True


class InvestigateListAttachmentItem(BaseModel):
    name: Optional[str] = Field(None, description="附件名称")
    url: Optional[str] = Field(None, description="附件地址")

    class Config:
        from_attributes = True


class LogisticTicketDetailRecheckAppealInfoItem(BaseModel):
    add_time: Optional[str] = Field(None, description="复查/申诉时间")
    attachment_file_list: List[InvestigateListAttachmentItem] = Field(
        default_factory=list, description="申诉附件"
    )
    io_desc: Optional[str] = Field(None, description="申诉需求")
    handle_info: List[InvestigateHandleinfo] = Field(
        default_factory=list, description="回复结果"
    )
    reply_time: Optional[str] = Field(None, description="回复时间")

    class Config:
        from_attributes = True


class LogisticTicketDetailRecheckAppealInfo(BaseModel):
    list: List[LogisticTicketDetailRecheckAppealInfoItem] = Field(
        default_factory=list, description="复查/申诉列表"
    )

    class Config:
        from_attributes = True


class LogisticTicketDetailLogInfoItem(BaseModel):
    handle_user: Optional[str] = Field(None, description="操作人")
    io_status_text: str = Field(..., description="状态查件状态文本")
    add_time: Optional[str] = Field(None, description="操作时间")

    class Config:
        from_attributes = True


class LogisticTicketDetailLogInfo(BaseModel):
    list: List[LogisticTicketDetailLogInfoItem] = Field(
        default_factory=list, description="日志列表"
    )

    class Config:
        from_attributes = True


class LogisticTicketDetailData(BaseModel):
    base_info: LogisticTicketDetailBaseInfo = Field(..., description="基本信息")
    order_info: LogisticTicketDetailOrderInfo = Field(..., description="订单信息")
    recheck_info: Optional[LogisticTicketDetailRecheckAppealInfo] = Field(
        None, description="复查信息"
    )
    appeal_info: Optional[LogisticTicketDetailRecheckAppealInfo] = Field(
        None, description="申诉信息"
    )
    log_info: LogisticTicketDetailLogInfo = Field(..., description="日志信息")

    class Config:
        from_attributes = True


class LogisticTicketDetailOut(BaseModel):
    code: int = Field(..., description="0成功,其它值失败")
    message: str = Field(..., description="文本消息")
    data: Optional[LogisticTicketDetailData] = Field(None, description="数据")

    class Config:
        from_attributes = True
