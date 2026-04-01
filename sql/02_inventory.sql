-- 测试数据：库存表 (inventory)
-- 仓库: USWE(美西仓), USEA(美东仓), UKLD(英国仓)

-- 美西仓 USWE 库存
INSERT INTO inventory (product_sku, product_barcode, warehouse_code, warehouse_desc, onway, pending, sellable, unsellable, reserved, shipped, stocking, pi_no_stock, pi_freeze, product_sales_value, is_deleted)
VALUES 
    ('SKU001', 'BAR001', 'USWE', '美西仓', 50, 20, 100, 5, 10, 200, 30, 0, 5, 29.99, 0),
    ('SKU002', 'BAR002', 'USWE', '美西仓', 30, 10, 80, 3, 5, 150, 20, 0, 3, 49.99, 0),
    ('SKU003', 'BAR003', 'USWE', '美西仓', 20, 15, 150, 8, 12, 300, 40, 0, 8, 19.99, 0),
    ('SKU004', 'BAR004', 'USWE', '美西仓', 100, 50, 500, 20, 30, 1000, 100, 0, 20, 5.99, 0),
    ('SKU005', 'BAR005', 'USWE', '美西仓', 10, 5, 60, 2, 5, 100, 15, 0, 2, 12.99, 0)
ON CONFLICT DO NOTHING;

-- 美东仓 USEA 库存
INSERT INTO inventory (product_sku, product_barcode, warehouse_code, warehouse_desc, onway, pending, sellable, unsellable, reserved, shipped, stocking, pi_no_stock, pi_freeze, product_sales_value, is_deleted)
VALUES 
    ('SKU001', 'BAR001', 'USEA', '美东仓', 40, 15, 80, 4, 8, 180, 25, 0, 4, 29.99, 0),
    ('SKU002', 'BAR002', 'USEA', '美东仓', 25, 8, 60, 2, 4, 120, 15, 0, 2, 49.99, 0),
    ('SKU003', 'BAR003', 'USEA', '美东仓', 15, 10, 120, 6, 10, 250, 35, 0, 6, 19.99, 0),
    ('SKU006', 'BAR006', 'USEA', '美东仓', 20, 10, 70, 3, 5, 100, 20, 0, 3, 89.99, 0),
    ('SKU007', 'BAR007', 'USEA', '美东仓', 30, 12, 90, 4, 6, 150, 25, 0, 4, 25.99, 0)
ON CONFLICT DO NOTHING;

-- 英国仓 UKLD 库存
INSERT INTO inventory (product_sku, product_barcode, warehouse_code, warehouse_desc, onway, pending, sellable, unsellable, reserved, shipped, stocking, pi_no_stock, pi_freeze, product_sales_value, is_deleted)
VALUES 
    ('SKU001', 'BAR001', 'UKLD', '英国仓', 20, 8, 40, 2, 4, 80, 12, 0, 2, 29.99, 0),
    ('SKU002', 'BAR002', 'UKLD', '英国仓', 15, 5, 30, 1, 2, 60, 8, 0, 1, 49.99, 0),
    ('SKU003', 'BAR003', 'UKLD', '英国仓', 10, 5, 60, 3, 5, 120, 18, 0, 3, 19.99, 0),
    ('SKU008', 'BAR008', 'UKLD', '英国仓', 15, 8, 50, 2, 3, 80, 15, 0, 2, 59.99, 0),
    ('SKU009', 'BAR009', 'UKLD', '英国仓', 8, 4, 35, 1, 2, 50, 10, 0, 1, 35.99, 0),
    ('SKU010', 'BAR010', 'UKLD', '英国仓', 20, 10, 100, 5, 8, 200, 30, 0, 5, 15.99, 0)
ON CONFLICT DO NOTHING;
