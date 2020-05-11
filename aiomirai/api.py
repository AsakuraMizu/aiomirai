"""
此模块提供了 Mirai API HTTP 的 API 调用相关类。
"""

from functools import partial
from typing import IO, Any, Awaitable, Callable, Dict, Optional, Union

import httpx
from httpx._models import RequestData, RequestFiles, QueryParamTypes

from .exception import *
from .logger import Api as Logger
from .utils import camelCase

__all__ = ['Api', 'SessionApi']


class Api:
    def __init__(self, api_root: str):
        self._api_root = api_root.strip('/') + '/' if api_root else None

    async def call_action(self,
                          action: str,
                          method: Optional[str] = 'POST',
                          format: Optional[str] = 'json',
                          *,
                          data: Optional[RequestData] = None,
                          files: Optional[RequestFiles] = None,
                          json: Optional[Any] = None,
                          params: Optional[QueryParamTypes] = None,
                          **kwargs) -> Any:

        if method == 'GET':
            format = 'params'

        args = locals().copy()
        del args['self']
        del args['action']
        args = {k: v for k, v in args.items() if v}
        Logger.info('Calling %s with params: %s', action, repr(args))

        mix = {'data': data, 'files': files, 'json': json, 'params': params}

        def _parse(data):
            if isinstance(data, dict):
                return {camelCase(k): _parse(v) for k, v in data.items()}
            elif isinstance(data, list):
                return [_parse(x) for x in data]
            else:
                return data

        mix = _parse(mix)
        kwargs = _parse(kwargs)

        mix[format] = mix[format] or {}
        mix[format].update(kwargs)

        url = self._api_root + camelCase(action)

        try:
            async with httpx.AsyncClient() as client:
                resp = await client.request(method, url, **mix)
            try:
                res = resp.json()
            except Exception as e:
                if not 200 <= resp.status_code < 300:
                    raise HttpFailed(resp.status_code)
                raise e
            if not isinstance(res, dict):
                return res
            code = res.get('code')
            if code == 0 or code is None:
                return res
            msg = res.get('msg')
            raise ActionFailed(code, msg)
        except httpx.InvalidURL:
            raise NetworkError('API root url invalid')
        except httpx.HTTPError:
            raise NetworkError('HTTP request failed')

    def __getattr__(self, item: str) -> Callable[..., Awaitable[Any]]:
        """获取一个可调用对象，用于调用对应 API。"""
        if item.startswith(('get', 'fetch', 'peek')):
            return partial(self.call_action, item.split('get_', 1)[-1], 'GET')
        return partial(self.call_action, item)


class SessionApi(Api):
    def __init__(self, api_root: str, auth_key: str, qq: int):
        super().__init__(api_root)
        self._auth_key = auth_key
        self._qq = qq
        self._session_key = None

    async def call_action(self,
                          action: str,
                          method: Optional[str] = 'POST',
                          format: Optional[str] = 'json',
                          **params) -> Any:
        if not self._session_key:
            raise Unauthenticated
        try:
            return await super().call_action(action,
                                             method,
                                             format,
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
        return await self.call_action('upload_image',
                                      format='data',
                                      data={'type': type},
                                      files={'img': img})

    async def auth(self) -> Dict[str, Any]:
        r = await Api.call_action(self, 'auth', auth_key=self._auth_key)
        self._session_key = r.get('session')
        return r

    async def verify(self) -> Dict[str, Any]:
        return await self.call_action('verify', qq=self._qq)

    async def release(self) -> Dict[str, Any]:
        try:
            return await self.call_action('release', qq=self._qq)
        finally:
            self._session_key = None

    async def resp_new_friend(self,
                              *,
                              event_id: int,
                              from_id: int,
                              group_id: int,
                              operate: Optional[int] = 0,
                              message: Optional[str] = "") -> Dict[str, Any]:
        return await self.call_action('resp/new_friend_request_event',
                                      event_id=event_id,
                                      from_id=from_id,
                                      group_id=group_id,
                                      operate=operate,
                                      message=message)

    async def resp_member_join(self,
                               *,
                               event_id: int,
                               from_id: int,
                               group_id: int,
                               operate: Optional[int] = 0,
                               message: Optional[str] = "") -> Dict[str, Any]:
        return await self.call_action('resp/member_join_request_event',
                                      event_id=event_id,
                                      from_id=from_id,
                                      group_id=group_id,
                                      operate=operate,
                                      message=message)

    async def __aenter__(self) -> 'SessionApi':
        await self.auth()
        await self.verify()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.release()
