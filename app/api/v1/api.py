from fastapi import APIRouter

from app.api.v1.endpoints import auth, order, product

api_router = APIRouter()

api_router.include_router(product.router, prefix="/product", tags=["商品管理"])
api_router.include_router(order.router, prefix="/order", tags=["订单管理"])
api_router.include_router(auth.router, prefix="/auth", tags=["用户认证"])
