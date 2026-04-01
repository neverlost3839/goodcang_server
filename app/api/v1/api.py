from fastapi import APIRouter

from app.api.v1.endpoints import (
    order,
    product,
    inventory,
    inbound_order,
    return_order,
    test,
    base_data,
    assistant,
    finance,
    plan_order,
)

api_router = APIRouter()

api_router.include_router(product.router, prefix="/product", tags=["商品管理"])
api_router.include_router(order.router, prefix="/order", tags=["订单管理"])
api_router.include_router(inventory.router, prefix="/inventory", tags=["库存管理"])
api_router.include_router(
    inbound_order.router, prefix="/inbound_order", tags=["入库单管理"]
)
api_router.include_router(
    return_order.router, prefix="/return_order", tags=["退货单管理"]
)
api_router.include_router(base_data.router, prefix="/base_data", tags=["基础数据"])
api_router.include_router(test.router, prefix="/test", tags=["接口测试"])
api_router.include_router(assistant.router, prefix="/assistant", tags=["查件助手"])
api_router.include_router(finance.router, prefix="/finance", tags=["财务"])
api_router.include_router(plan_order.router, prefix="/plan_order", tags=["计划单"])
