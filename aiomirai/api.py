"""
此模块提供了 Mirai API HTTP 的 API 调用相关类。
"""

from functools import partial
from typing import IO, Any, Awaitable, Callable, Dict, Optional, Union

import httpx

from .exception import *
from .logger import Api as Logger
from .utils import camelCase


class Api:
    def __init__(self, api_root: str):
        self._api_root = api_root.strip('/') + '/' if api_root else None

    async def call_action(self, action: str, **params) -> Any:

        Logger.info('Calling %s with params: %s', action, str(params))

        params = {camelCase(k): v for k, v in params.items()}
        if action.startswith(('get', 'fetch', 'peek')):
            action = action.split('get_', 1)[-1]
            method = 'GET'
            params = {'params': params}
        else:
            method = 'POST'
            params = {'json': params}
        url = self._api_root + camelCase(action)

        try:
            async with httpx.AsyncClient() as client:
                resp = await client.request(method, url, **params)
            if 200 <= resp.status_code < 300:
                return resp.json()
            elif resp.status_code == 400:
                res = resp.json()
                code = res.get('code')
                msg = res.get('msg')
                raise ActionFailed(code, msg)
            raise HttpFailed(resp.status_code)
        except httpx.InvalidURL:
            raise NetworkError('API root url invalid')
        except httpx.HTTPError:
            raise NetworkError('HTTP request failed')

    def __getattr__(self, item: str) -> Callable[..., Awaitable[Any]]:
        """获取一个可调用对象，用于调用对应 API。"""
        return partial(self.call_action, item)


class SessionApi(Api):
    def __init__(self, api_root: str, auth_key: str, qq: int):
        super().__init__(api_root)
        self._auth_key = auth_key
        self._qq = qq
        self._session_key = None

    async def call_action(self, action: str, **params) -> Any:
        if not self._session_key:
            raise Unauthenticated
        try:
            return await super().call_action(action,
                                             **params,
                                             session_key=self._session_key)
        except ActionFailed as _e:
            switcher = {
                1: InvalidAuthKey,
                2: InvaildBot,
                3: InvaildSession,
                4: Unverified
            }
            e = switcher.get(_e.code)
            if not e:
                raise _e
            raise e(_e.code, _e.msg)

    async def upload_image(self, type: str, img: IO) -> Dict[str, Any]:
        if not self._session_key:
            raise Unauthenticated
        try:
            Logger.info('Calling %s with params: %s', 'upload_image', {
                'type': type,
                'img': img
            })
            async with httpx.AsyncClient() as client:
                resp = await client.post(self._api_root + 'uploadImage',
                                         data={
                                             'type': type,
                                             'sessionKey': self._session_key
                                         },
                                         files={'img': img})
            if 200 <= resp.status_code < 300:
                return resp.json()
            elif resp.status_code == 400:
                res = resp.json()
                code = res.get('code')
                msg = res.get('msg')
                raise ActionFailed(code, msg)
            raise HttpFailed(resp.status_code)
        except ActionFailed as _e:
            switcher = {
                1: InvalidAuthKey,
                2: InvaildBot,
                3: InvaildSession,
                4: Unverified
            }
            e = switcher.get(_e.code)
            if not e:
                raise _e
            raise e(_e.code, _e.msg)
        except httpx.InvalidURL:
            raise NetworkError('API root url invalid')
        except httpx.HTTPError:
            raise NetworkError('HTTP request failed')

    async def auth(self) -> Dict[str, Any]:
        r = await super().call_action('auth', auth_key=self._auth_key)
        self._session_key = r.get('session')
        return r

    async def verify(self) -> Dict[str, Any]:
        return await self.call_action('verify', qq=self._qq)

    async def release(self) -> Dict[str, Any]:
        return await self.call_action('release', qq=self._qq)

    async def __aenter__(self) -> 'SessionApi':
        await self.auth()
        await self.verify()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.release()
