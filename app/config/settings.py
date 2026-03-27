from pydantic import computed_field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    
    # 项目信息
    PROJECT_NAME: str = "Goodcang Server"
    API_V1_STR: str = "/api/v1"

    # 数据库配置
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "goodcang"

    # Redis 配置
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 6

    # 服务配置
    SERVICE_NAME: str = "goodcang_server"
    SERVICE_PORT: int = 8010

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        """异步数据库连接字符串"""
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    @computed_field
    @property
    def REDIS_URL(self) -> str:
        """Redis 连接字符串"""
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
