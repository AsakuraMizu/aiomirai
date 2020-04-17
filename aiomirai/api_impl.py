"""
此模块提供了 Mirai API HTTP 相关的实现类。
"""

import abc
import asyncio
from typing import Any, Awaitable, Callable, Dict, Optional, Union

import httpx
from quart import websocket

from .api import Api, AsyncApi, AsyncSessionApi
from .exception import ActionFailed, ApiNotAvailable, HttpFailed, NetworkError
from .utils import camelCase, sync_wait

try:
    import ujson as json
except:
    import json


def _handle_api_result(res: Optional[Dict[str, Any]]) -> Any:
    if isinstance(res, dict):
        if not res.get('code') == 0:
            raise ActionFailed(res.get('code'), res.get('msg'))
        return res


class HttpApi(AsyncApi):
    """
    HTTP API 实现类。
    实现通过 HTTP 调用 CQHTTP API。
    """
    def __init__(self, api_root: str, auth_key: str):
        self._api_root = api_root.strip('/') + '/' if api_root else None
        self._auth_key = auth_key

    async def call_action(self, action: str, **params) -> Any:
        if not self._api_root:
            raise ApiNotAvailable

        params = {camelCase(k): v for k, v in params.items()}
        if action.startswith(('get', 'fetch', 'peek')):
            action = action.split('get_', 1)[-1]
            method = 'GET'
            data = None
        else:
            method = 'POST'
            data = params
            params = None
        url = self._api_root + camelCase(action)

        try:
            async with httpx.AsyncClient() as client:
                resp = await client.request(method,
                                            url,
                                            json=data,
                                            params=params)
            print(resp.request.stream.body)
            if 200 <= resp.status_code < 300 or resp.status_code == 400:
                return _handle_api_result(json.loads(resp.text))
            raise HttpFailed(resp.status_code)
        except httpx.InvalidURL:
            raise NetworkError('API root url invalid')
        except httpx.HTTPError:
            raise NetworkError('HTTP request failed')


class HttpSessionApi(AsyncSessionApi, HttpApi):
    """
    HTTP API 实现类，提供会话接口。
    实现通过 HTTP 调用 CQHTTP API。
    """
    def __init__(self, api_root: str, auth_key: str, qq: int):
        super().__init__(api_root, auth_key)
        self._qq = qq

    async def call_action(self, action: str, **params) -> Any:
        return await super().call_action(action,
                                         **params,
                                         session_key=self._session_key)

    async def auth(self) -> Any:
        r = await super().call_action('auth', auth_key=self._auth_key)
        self._session_key = r.get('session')
        return r

    async def verify(self) -> Any:
        return await self.call_action('verify', qq=self._qq)


class SyncApi(Api):
    """
    封装 `AsyncApi` 对象，使其可同步地调用。
    """
    def __init__(self, async_api: AsyncApi, loop: asyncio.AbstractEventLoop):
        """
        `async_api` 参数为 `AsyncApi` 对象，`loop` 参数为用来执行 API
        调用的 event loop。
        """
        self._async_api = async_api
        self._loop = loop

    def call_action(self, action: str, **params) -> Any:
        """同步地调用 Mirai API HTTP。"""
        return sync_wait(coro=self._async_api.call_action(action, **params),
                         loop=self._loop)


class LazyApi(Api):
    """
    延迟获取 `Api` 对象。
    """
    def __init__(self, api_getter: Callable[[], Union[Api]]):
        self._api_getter = api_getter

    def call_action(self, action: str, **params) -> Union[Awaitable[Any], Any]:
        """获取 `Api` 对象，并调用 Mirai API HTTP。"""
        api = self._api_getter()
        return api.call_action(action, **params)
