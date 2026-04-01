-- 测试数据：订单表 (order) 和订单明细表 (order_item)

-- 订单1 - 美国订单
INSERT INTO "order" (reference_no, platform, shipping_method, warehouse_code, country_code, province, city, company, address1, address2, zipcode, doorplate, name, last_name, cell_phone, phone, email, order_desc, verify, is_shipping_method_not_allow_update, order_code, is_deleted)
VALUES 
    ('ORD20240301001', 'AMAZON', 'DHL_EPACKET', 'USWE', 'US', 'California', 'Los Angeles', NULL, '123 Main Street', 'Apt 5', '90001', '10', 'John Smith', 'Smith', NULL, '555-1234', 'john@example.com', 'Please handle with care', 1, 1, 'GC-ORD-001', 0);

-- 订单2 - 英国订单
INSERT INTO "order" (reference_no, platform, shipping_method, warehouse_code, country_code, province, city, company, address1, address2, zipcode, doorplate, name, last_name, cell_phone, phone, email, order_desc, verify, is_shipping_method_not_allow_update, order_code, is_deleted)
VALUES 
    ('ORD20240301002', 'EBAY', 'UK_EXPRESS', 'UKLD', 'GB', 'London', 'London', 'ABC Ltd', '456 Oxford Street', NULL, 'SW1A 1AA', NULL, 'Emma Johnson', 'Johnson', NULL, '44-20-1234', 'emma@example.com', 'Gift box required', 1, 1, 'GC-ORD-002', 0);

-- 订单3 - 美东仓库
INSERT INTO "order" (reference_no, platform, shipping_method, warehouse_code, country_code, province, city, company, address1, address2, zipcode, doorplate, name, last_name, cell_phone, phone, email, order_desc, verify, is_shipping_method_not_allow_update, order_code, is_deleted)
VALUES 
    ('ORD20240301003', 'SHOPIFY', 'USPS_PRIORITY', 'USEA', 'US', 'New York', 'New York', NULL, '789 Broadway', 'Suite 100', '10001', '20', 'Michael Brown', 'Brown', NULL, '555-5678', 'michael@example.com', NULL, 1, 1, 'GC-ORD-003', 0);

-- 订单4 - 英国仓库
INSERT INTO "order" (reference_no, platform, shipping_method, warehouse_code, country_code, province, city, company, address1, address2, zipcode, doorplate, name, last_name, cell_phone, phone, email, order_desc, verify, is_shipping_method_not_allow_update, order_code, is_deleted)
VALUES 
    ('ORD20240301004', 'AMAZON', 'ROYAL_MAIL', 'UKLD', 'GB', 'Manchester', 'Manchester', NULL, '10 Downing Street', NULL, 'M1 1AA', NULL, 'David Wilson', 'Wilson', NULL, '44-161-1234', 'david@example.com', 'Fragile items inside', 1, 1, 'GC-ORD-004', 0);

-- 订单5 - 美西仓库
INSERT INTO "order" (reference_no, platform, shipping_method, warehouse_code, country_code, province, city, company, address1, address2, zipcode, doorplate, name, last_name, cell_phone, phone, email, order_desc, verify, is_shipping_method_not_allow_update, order_code, is_deleted)
VALUES 
    ('ORD20240301005', 'WISH', 'FEDEX_GROUND', 'USWE', 'US', 'Washington', 'Seattle', 'Tech Corp', '1 Microsoft Way', NULL, '98052', NULL, 'Lisa Taylor', 'Taylor', NULL, '555-9999', 'lisa@example.com', 'Business address', 1, 1, 'GC-ORD-005', 0);

-- 订单明细1 - 订单1的商品
INSERT INTO order_item (order_id, product_sku, quantity, transaction_id, item_id, product_declared_value, hs_code)
VALUES 
    (1, 'SKU001', 2, 'TXN001', 'ITEM001', 59.98, '85183000'),
    (1, 'SKU002', 1, 'TXN001', 'ITEM002', 49.99, '85176200');

-- 订单明细2 - 订单2的商品
INSERT INTO order_item (order_id, product_sku, quantity, transaction_id, item_id, product_declared_value, hs_code)
VALUES 
    (2, 'SKU003', 3, 'TXN002', 'ITEM001', 59.97, '85078000'),
    (2, 'SKU004', 5, 'TXN002', 'ITEM002', 29.95, '85444200');

-- 订单明细3 - 订单3的商品
INSERT INTO order_item (order_id, product_sku, quantity, transaction_id, item_id, product_declared_value, hs_code)
VALUES 
    (3, 'SKU005', 2, 'TXN003', 'ITEM001', 25.98, '85183000'),
    (3, 'SKU006', 1, 'TXN003', 'ITEM002', 89.99, '84716000');

-- 订单明细4 - 订单4的商品
INSERT INTO order_item (order_id, product_sku, quantity, transaction_id, item_id, product_declared_value, hs_code)
VALUES 
    (4, 'SKU007', 2, 'TXN004', 'ITEM001', 51.98, '84716000'),
    (4, 'SKU008', 1, 'TXN004', 'ITEM002', 59.99, '84717000');

-- 订单明细5 - 订单5的商品
INSERT INTO order_item (order_id, product_sku, quantity, transaction_id, item_id, product_declared_value, hs_code)
VALUES 
    (5, 'SKU009', 1, 'TXN005', 'ITEM001', 35.99, '85258900'),
    (5, 'SKU010', 3, 'TXN005', 'ITEM002', 47.97, '85176200');
