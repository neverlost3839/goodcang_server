from fastapi import APIRouter, Query
from typing import Optional, List
from app.schemas.common import Response

router = APIRouter(prefix="/test", tags=["接口测试"])


@router.get("/inventory", response_model=Response[dict])
async def test_inventory(
    product_sku: Optional[str] = Query(None, description="商品SKU"),
    warehouse_code: Optional[str] = Query(None, description="仓库代码"),
):
    """测试库存查询API"""
    from app.client.inventory import goodcang_inventory

    result = await goodcang_inventory.get_product_inventory(
        page=1,
        page_size=10,
        product_sku=product_sku,
        warehouse_code=warehouse_code,
    )
    return Response(data=result)


@router.get("/inventory/list", response_model=Response[dict])
async def test_inventory_list(
    product_sku_arr: Optional[List[str]] = Query(None, description="多个商品SKU数组"),
    warehouse_code_arr: Optional[List[str]] = Query(
        None, description="多个仓库代码数组"
    ),
):
    """测试库存列表查询API（批量）"""
    from app.client.inventory import goodcang_inventory

    result = await goodcang_inventory.get_product_inventory(
        page=1,
        page_size=10,
        product_sku_arr=product_sku_arr,
        warehouse_code_arr=warehouse_code_arr,
    )
    return Response(data=result)


@router.get("/order/create", response_model=Response[dict])
async def test_order_create():
    """测试创建订单API（模拟测试）"""
    from app.client.order import goodcang_order

    result = await goodcang_order.create_order(
        shipping_method="DHL",
        warehouse_code="USEA",
        country_code="US",
        province="California",
        city="Los Angeles",
        address1="123 Main Street",
        zipcode="90001",
        name="John Doe",
        items=[
            {
                "product_sku": "TEST_SKU_001",
                "quantity": 1,
            }
        ],
    )
    return Response(data=result)


@router.get("/product/add", response_model=Response[dict])
async def test_product_add():
    """测试创建商品API（模拟测试）"""
    from app.client.product import goodcang_product

    result = await goodcang_product.add_product(
        product_sku="TEST_SKU_001",
        product_name_cn="测试商品中文名称",
        product_name_en="Test Product English Name",
        product_weight=0.5,
        product_length=10.0,
        product_width=10.0,
        product_height=10.0,
        contain_battery=0,
        type_of_goods=0,
        cat_id_level2=1,
        product_declared_name_cn="测试申报品名",
        product_material="塑料",
        branded=0,
        product_link="https://example.com/product",
        export_country=[{"country_code": "CN", "country_name": "中国"}],
        import_country=[{"country_code": "US", "country_name": "美国"}],
    )
    return Response(data=result)
