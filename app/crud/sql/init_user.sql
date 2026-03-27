-- Create user_account table
CREATE TABLE IF NOT EXISTS user_account (
    id BIGSERIAL PRIMARY KEY,
    username VARCHAR(64) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL,
    nickname VARCHAR(64) NOT NULL DEFAULT '',
    email VARCHAR(128) NOT NULL DEFAULT '',
    phone VARCHAR(32) NOT NULL DEFAULT '',
    avatar VARCHAR(512) NOT NULL DEFAULT '',
    gender VARCHAR(16) NOT NULL DEFAULT 'unknown',
    bio VARCHAR(512) NOT NULL DEFAULT '',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_user_account_username ON user_account(username);
CREATE INDEX IF NOT EXISTS idx_user_account_phone ON user_account(phone);
CREATE INDEX IF NOT EXISTS idx_user_account_email ON user_account(email);
