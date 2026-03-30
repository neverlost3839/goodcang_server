from typing import Any, Optional
import httpx

from app.config.settings import settings


class GoodCangBase:
    """GoodCang API 基础客户端"""

    def __init__(self):
        self.base_url = settings.GOODCANG_API_HOST
        self.api_key = settings.GOODCANG_API_KEY
        self.client_code = settings.GOODCANG_CLIENT_CODE

    def _get_headers(self) -> dict:
        """获取请求头"""
        return {
            "Content-Type": "application/json",
            "clientCode": self.client_code,
            "apiKey": self.api_key,
        }

    async def _post(
        self,
        endpoint: str,
        data: Optional[dict] = None,
    ) -> dict[str, Any]:
        """发送POST请求"""
        url = f"{self.base_url}{endpoint}"
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                url,
                json=data,
                headers=self._get_headers(),
            )
            response.raise_for_status()
            return response.json()

    async def _get(
        self,
        endpoint: str,
        params: Optional[dict] = None,
    ) -> dict[str, Any]:
        """发送GET请求"""
        url = f"{self.base_url}{endpoint}"
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(
                url,
                params=params,
                headers=self._get_headers(),
            )
            response.raise_for_status()
            return response.json()
