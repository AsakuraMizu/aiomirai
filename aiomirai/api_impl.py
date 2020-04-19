"""
此模块提供了 Mirai API HTTP 相关的实现类。
"""

import abc
import asyncio
from typing import Any, Awaitable, Callable, Dict, Optional, Union

import httpx

from .api import Api, AsyncApi, AsyncSessionApi
from .exception import (ActionFailed, ApiNotAvailable, AuthenticateError,
                        HttpFailed, NetworkError)
from .logger import Api as Logger
from .utils import camelCase, sync_wait

__all__ = [
    'HttpApi',
    'HttpSessionApi',
    'SyncApi',
    'LazyApi',
]


class HttpApi(AsyncApi):
    """
    HTTP API 实现类。
    实现通过 HTTP 调用 CQHTTP API。
    """
    def __init__(self, api_root: str):
        self._api_root = api_root.strip('/') + '/' if api_root else None

    async def call_action(self, action: str, **params) -> Any:
        if not self._api_root:
            raise ApiNotAvailable

        Logger.info('Calling %s with params: %s', action, str(params))

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
            if 200 <= resp.status_code < 300 or resp.status_code == 400:
                res = resp.json()
                if res.get('code') == 0:
                    return res
                raise ActionFailed(res.get('code'), res.get('msg'))
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
        super().__init__(api_root)
        self._auth_key = auth_key
        self._qq = qq

    async def call_action(self, action: str, **params) -> Any:
        if not self._auth_key:
            raise AuthenticateError
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
