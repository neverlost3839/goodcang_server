-- Create product table
CREATE TABLE IF NOT EXISTS product (
    id BIGSERIAL PRIMARY KEY,
    sku VARCHAR(256) NOT NULL,
    name VARCHAR(256) NOT NULL,
    description VARCHAR(256) NOT NULL,
    price NUMERIC(10, 2),
    category VARCHAR(256) NOT NULL,
    brand VARCHAR(256) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'scraped',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_product_sku ON product(sku);
CREATE INDEX IF NOT EXISTS idx_product_category ON product(category);
CREATE INDEX IF NOT EXISTS idx_product_brand ON product(brand);
CREATE INDEX IF NOT EXISTS idx_product_status ON product(status);
