import httpx

from .api import Api, SessionApi
from .utils import camelCase


class AsyncApi(Api):
    def __init__(self, api_root: str, auth_key: str):
        if not api_root.endswith('/'):
            api_root += '/'
        self.api_root = api_root
        self.auth_key = auth_key

    async def call_action(self, action: str, **params):
        params = {camelCase(k): v for k, v in params.items()}
        if action.startswith(('get', 'fetch', 'peek')):
            action = action.split('get_', 1)[-1]
            method = 'GET'
            json = None
        else:
            method = 'POST'
            json = params
            params = None
        url = self.api_root + camelCase(action)
        async with httpx.AsyncClient() as client:
            r = await client.request(method, url, json=json, params=params)
        return r.json()

class AsyncSessionApi(AsyncApi, SessionApi):
    def __init__(self, api_root: str, auth_key: str, qq: int):
        super().__init__(api_root, auth_key)
        self.qq = qq

    async def call_action(self, action: str, **params):
        return await super().call_action(action, **params, session_key=self.session_key)

    async def auth(self):
        r = await super().call_action('auth', auth_key=self.auth_key)
        self.session_key = r['session']
        return r

    async def verify(self):
        return await self.call_action('verify', qq=self.qq)
