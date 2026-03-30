from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=64, description="用户名")
    nickname: str = Field(default="", max_length=64, description="昵称")
    email: str = Field(default="", max_length=128, description="邮箱")
    phone: str = Field(default="", max_length=32, description="手机号")
    avatar: str = Field(default="", max_length=512, description="头像URL")
    gender: str = Field(default="unknown", max_length=16, description="性别")
    bio: str = Field(default="", max_length=512, description="个人简介")


class UserCreate(UserBase):
    password: str = Field(..., min_length=1, max_length=128, description="登录密码")


class UserRegister(BaseModel):
    username: str = Field(..., min_length=3, max_length=64, description="用户名")
    password: str = Field(..., min_length=1, max_length=128, description="密码（明文）")
    nickname: str = Field(default="", max_length=64, description="昵称")
    email: str = Field(default="", max_length=128, description="邮箱")
    phone: str = Field(default="", max_length=32, description="手机号")
    avatar: str = Field(default="", max_length=512, description="头像URL")
    gender: str = Field(default="unknown", max_length=16, description="性别")
    bio: str = Field(default="", max_length=512, description="个人简介")


class UserLogin(BaseModel):
    username: str = Field(..., min_length=3, max_length=64, description="用户名")
    password: str = Field(..., min_length=1, max_length=128, description="密码（明文）")


class UserUpdate(BaseModel):
    nickname: Optional[str] = Field(default=None, max_length=64, description="昵称")
    email: Optional[str] = Field(default=None, max_length=128, description="邮箱")
    phone: Optional[str] = Field(default=None, max_length=32, description="手机号")
    avatar: Optional[str] = Field(default=None, max_length=512, description="头像URL")
    gender: Optional[str] = Field(default=None, max_length=16, description="性别")
    bio: Optional[str] = Field(default=None, max_length=512, description="个人简介")


class UserOut(BaseModel):
    id: int = Field(..., description="用户ID")
    username: str = Field(..., description="用户名")
    nickname: str = Field(..., description="昵称")
    email: str = Field(..., description="邮箱")
    phone: str = Field(..., description="手机号")
    avatar: str = Field(..., description="头像URL")
    gender: str = Field(..., description="性别")
    bio: str = Field(..., description="个人简介")
    created_at: datetime = Field(..., description="创建时间")
    updated_at: datetime = Field(..., description="更新时间")

    class Config:
        from_attributes = True
