-- 测试数据：入库单表 (inbound_order) 和入库单明细表 (inbound_order_item)

-- 入库单1 - 美西仓自发入库
INSERT INTO inbound_order (receiving_code, reference_no, transit_type, receiving_shipping_type, warehouse_code, sm_code, tracking_number, eta_date, receiving_desc, verify, weight, volume, is_delay, is_rollover, is_deleted)
VALUES 
    ('GRN-USWE-001', 'IN20240301001', 0, 0, 'USWE', NULL, 'TRK20240301001', '2024-03-15', '第一批蓝牙耳机到货', 1, 5.5, 0.02, 0, 0, 0);

-- 入库单2 - 美东仓自发入库
INSERT INTO inbound_order (receiving_code, reference_no, transit_type, receiving_shipping_type, warehouse_code, sm_code, tracking_number, eta_date, receiving_desc, verify, weight, volume, is_delay, is_rollover, is_deleted)
VALUES 
    ('GRN-USEA-001', 'IN20240301002', 0, 2, 'USEA', NULL, 'TRK20240301002', '2024-03-18', '键盘套装到货', 1, 10.0, 0.05, 0, 0, 0);

-- 入库单3 - 英国仓自发入库
INSERT INTO inbound_order (receiving_code, reference_no, transit_type, receiving_shipping_type, warehouse_code, sm_code, tracking_number, eta_date, receiving_desc, verify, weight, volume, is_delay, is_rollover, is_deleted)
VALUES 
    ('GRN-UKLD-001', 'IN20240301003', 0, 1, 'UKLD', NULL, 'TRK20240301003', '2024-03-20', '摄像头到货', 1, 3.0, 0.01, 0, 0, 0);

-- 入库单4 - 美西仓FBA入库
INSERT INTO inbound_order (receiving_code, reference_no, transit_type, receiving_shipping_type, warehouse_code, sm_code, tracking_number, eta_date, receiving_desc, verify, weight, volume, is_delay, is_rollover, is_deleted)
VALUES 
    ('GRN-USWE-002', 'IN20240301004', 5, 0, 'USWE', NULL, 'TRK20240301004', '2024-03-25', 'FBA换标商品', 1, 2.0, 0.01, 0, 1, 0);

-- 入库单5 - 英国仓中转入库
INSERT INTO inbound_order (receiving_code, reference_no, transit_type, receiving_shipping_type, warehouse_code, sm_code, transit_warehouse_code, tracking_number, eta_date, receiving_desc, verify, weight, volume, is_delay, is_rollover, is_deleted)
VALUES 
    ('GRN-UKLD-002', 'IN20240301005', 3, 2, 'UKLD', 'TRANSIT_CN_UK', 'CNWH', 'TRK20240301005', '2024-03-28', '中转仓货物', 1, 8.0, 0.03, 0, 0, 0);

-- 入库单明细1 - 入库单1的商品
INSERT INTO inbound_order_item (inbound_order_id, box_no, reference_box_no, product_sku, quantity, fba_product_code, is_deleted)
VALUES 
    (1, 1, 'BOX001', 'SKU001', 50, NULL, 0),
    (1, 2, 'BOX002', 'SKU001', 50, NULL, 0),
    (1, 3, 'BOX003', 'SKU002', 30, NULL, 0);

-- 入库单明细2 - 入库单2的商品
INSERT INTO inbound_order_item (inbound_order_id, box_no, reference_box_no, product_sku, quantity, fba_product_code, is_deleted)
VALUES 
    (2, 1, 'BOX001', 'SKU006', 20, NULL, 0),
    (2, 2, 'BOX002', 'SKU007', 30, NULL, 0);

-- 入库单明细3 - 入库单3的商品
INSERT INTO inbound_order_item (inbound_order_id, box_no, reference_box_no, product_sku, quantity, fba_product_code, is_deleted)
VALUES 
    (3, 1, 'BOX001', 'SKU009', 35, NULL, 0),
    (3, 2, 'BOX002', 'SKU010', 100, NULL, 0);

-- 入库单明细4 - 入库单4的商品(FBA)
INSERT INTO inbound_order_item (inbound_order_id, box_no, reference_box_no, product_sku, quantity, fba_product_code, is_deleted)
VALUES 
    (4, 1, 'BOX001', 'SKU001', 100, 'FBA-SKU001', 0);

-- 入库单明细5 - 入库单5的商品(中转)
INSERT INTO inbound_order_item (inbound_order_id, box_no, reference_box_no, product_sku, quantity, fba_product_code, is_deleted)
VALUES 
    (5, 1, 'BOX001', 'SKU003', 60, NULL, 0),
    (5, 2, 'BOX002', 'SKU004', 150, NULL, 0),
    (5, 3, 'BOX003', 'SKU005', 60, NULL, 0);
