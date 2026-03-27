from datetime import datetime

from sqlalchemy import BigInteger, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(64), nullable=False, unique=True, index=True, comment="用户名")
    password: Mapped[str] = mapped_column(String(128), nullable=False, comment="登录密码（明文示例）")
    nickname: Mapped[str] = mapped_column(String(64), nullable=False, default="", comment="昵称")
    email: Mapped[str] = mapped_column(String(128), nullable=False, default="", comment="邮箱")
    phone: Mapped[str] = mapped_column(String(32), nullable=False, default="", comment="手机号")
    avatar: Mapped[str] = mapped_column(String(512), nullable=False, default="", comment="头像URL")
    gender: Mapped[str] = mapped_column(String(16), nullable=False, default="unknown", comment="性别")
    bio: Mapped[str] = mapped_column(String(512), nullable=False, default="", comment="个人简介")
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow, comment="创建时间")
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow, comment="更新时间")
