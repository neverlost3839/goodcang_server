from typing import Any, Optional
import httpx

from app.config.settings import settings


class GoodCangBase:
    """GoodCang API 基础客户端"""

    def __init__(self):
        self.base_url = settings.GOODCANG_API_HOST
        self.app_key = settings.GOODCANG_APP_KEY
        self.app_token = settings.GOODCANG_APP_TOKEN

    def _get_headers(self) -> dict:
        """获取请求头"""
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "app-key": self.app_key,
            "app-token": self.app_token,
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
            if not response.status_code == 200:
                print(f"[DEBUG] API Error Response: {response.text}")
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
