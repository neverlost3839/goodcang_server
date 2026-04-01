from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field


class PlanOrderProductItem(BaseModel):
    product_name: str = Field(..., description="商品名称")
    product_sku: str = Field(..., description="商品编码")
    quantity: int = Field(..., description="商品数量")

    class Config:
        from_attributes = True


class PlanOrderBoxProductItem(BaseModel):
    product_sku: str = Field(..., description="商品编码")
    quantity: int = Field(..., description="商品数量")

    class Config:
        from_attributes = True


class PlanOrderBoxItem(BaseModel):
    box_no: str = Field(..., description="箱号")
    box_mark: str = Field(..., description="箱唛号")
    quantity: int = Field(..., description="总数量")
    type_quantity: int = Field(..., description="商品种类")
    product_list: List[PlanOrderBoxProductItem] = Field(
        default_factory=list, description="商品信息"
    )

    class Config:
        from_attributes = True


class PlanOrderItem(BaseModel):
    plan_order_code: str = Field(..., description="计划单号")
    reference_no: Optional[str] = Field(None, description="参考号")
    warehouse_code: str = Field(..., description="区域仓")
    dest_warehouse_type: int = Field(..., description="目的仓类型")
    label_replacement_option: int = Field(..., description="换标要求")
    is_change_label: int = Field(..., description="换标服务")
    is_stick_label: int = Field(..., description="贴标服务")
    actual_fee_estimate: str = Field(..., description="费用总额")
    currency_code: str = Field(..., description="币种")
    order_status: int = Field(..., description="状态")
    abnormal_reason: Optional[str] = Field(None, description="异常原因")
    create_time: str = Field(..., description="创建时间")
    update_time: Optional[str] = Field(None, description="更新时间")
    submit_time: Optional[str] = Field(None, description="提交时间")
    finish_time: Optional[str] = Field(None, description="完成时间")
    product_list: List[PlanOrderProductItem] = Field(
        default_factory=list, description="商品信息"
    )
    box_list: Optional[List[PlanOrderBoxItem]] = Field(None, description="暂存箱信息")

    class Config:
        from_attributes = True


class PlanOrderListData(BaseModel):
    total: int = Field(..., description="总数量")
    list: List[PlanOrderItem] = Field(default_factory=list, description="计划单列表")

    class Config:
        from_attributes = True


class PlanOrderListOut(BaseModel):
    code: int = Field(..., description="0成功,其它值失败")
    message: str = Field(..., description="文本消息")
    data: Optional[PlanOrderListData] = Field(None, description="数据")

    class Config:
        from_attributes = True


class BoxListSkuItem(BaseModel):
    fnsku: Optional[str] = Field(None, description="FNSKU")
    product_sku: str = Field(..., description="商品编码")
    quantity: int = Field(..., description="数量")
    product_sku_name: Optional[str] = Field(None, description="商品名称")

    class Config:
        from_attributes = True


class BoxListItem(BaseModel):
    box_no: str = Field(..., description="箱号")
    plan_order_code: str = Field(..., description="计划单号")
    relation_order_code: Optional[str] = Field(None, description="关联单号")
    warehouse_code: str = Field(..., description="仓库代码")
    temp_total_amount: str = Field(..., description="费用总额")
    currency_code: Optional[str] = Field(None, description="币种")
    is_change_label: int = Field(..., description="换标服务")
    label_replacement_option: int = Field(..., description="换标要求")
    is_stick_label: int = Field(..., description="贴标服务")
    officer_no: Optional[str] = Field(None, description="操作人")
    box_status: int = Field(..., description="箱状态")
    length: str = Field(..., description="长(CM)")
    width: str = Field(..., description="宽(CM)")
    height: str = Field(..., description="高(CM)")
    weight: str = Field(..., description="重量(KG)")
    pack_time: str = Field(..., description="装箱时间")
    sku_list: List[BoxListSkuItem] = Field(default_factory=list, description="SKU列表")

    class Config:
        from_attributes = True


class BoxListData(BaseModel):
    total: int = Field(..., description="总数量")
    list: List[BoxListItem] = Field(default_factory=list, description="装箱列表")

    class Config:
        from_attributes = True


class BoxListOut(BaseModel):
    code: int = Field(..., description="0成功,其它值失败")
    message: str = Field(..., description="文本消息")
    data: Optional[BoxListData] = Field(None, description="数据")

    class Config:
        from_attributes = True
