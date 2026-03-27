

from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel


T = TypeVar("T")


class ResponseBase(BaseModel, Generic[T]):
    code: int = 200
    message: str = "success"
    data: Optional[T] = None


class Response(ResponseBase, Generic[T]):
    """通用响应结构"""
    pass


class PaginatedData(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    page_size: int
    total_pages: int


class PaginatedResponse(BaseModel, Generic[T]):
    code: int = 200
    message: str = "success"
    data: Optional[PaginatedData[T]] = None