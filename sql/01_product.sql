-- 测试数据：商品表 (product)
-- 仓库: USWE(美西仓), USEA(美东仓), UKLD(英国仓)

INSERT INTO product (product_sku, reference_no, product_name_cn, product_name_en, product_weight, product_length, product_width, product_height, cat_id_level2, product_link, verify, is_deleted)
VALUES 
    ('SKU001', 'REF001', '无线蓝牙耳机', 'Wireless Bluetooth Headphones', 0.15, 15, 10, 8, 1001, 'https://example.com/product1', 1, 0),
    ('SKU002', 'REF002', '智能手表', 'Smart Watch', 0.08, 5, 4, 2, 1002, 'https://example.com/product2', 1, 0),
    ('SKU003', 'REF003', '充电宝 10000mAh', 'Power Bank 10000mAh', 0.20, 14, 7, 2, 1003, 'https://example.com/product3', 1, 0),
    ('SKU004', 'REF004', 'USB-C 数据线', 'USB-C Cable', 0.03, 15, 10, 1, 1004, 'https://example.com/product4', 1, 0),
    ('SKU005', 'REF005', '手机支架', 'Phone Stand', 0.05, 10, 8, 5, 1005, 'https://example.com/product5', 1, 0),
    ('SKU006', 'REF006', '键盘套装', 'Keyboard Set', 0.50, 30, 20, 5, 1006, 'https://example.com/product6', 1, 0),
    ('SKU007', 'REF007', '鼠标无线', 'Wireless Mouse', 0.08, 10, 6, 4, 1007, 'https://example.com/product7', 1, 0),
    ('SKU008', 'REF008', '移动固态硬盘', 'Portable SSD 500GB', 0.10, 8, 5, 1, 1008, 'https://example.com/product8', 1, 0),
    ('SKU009', 'REF009', '摄像头 1080P', 'Webcam 1080P', 0.15, 8, 5, 5, 1009, 'https://example.com/product9', 1, 0),
    ('SKU010', 'REF010', '运动手环', 'Fitness Band', 0.03, 4, 2, 1, 1010, 'https://example.com/product10', 1, 0)
ON CONFLICT (product_sku) DO NOTHING;
