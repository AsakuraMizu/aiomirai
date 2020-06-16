import asyncio
from typing import Optional

import httpx

from . import Receiver
from ..api import SessionApi
from ..exception import ApiError
from ..logger import Receiver as Logger


class PollingReceiver(Receiver):
    def __init__(self, api: SessionApi, count: Optional[int] = 10, sleep_time: Optional[float] = 0.5,
                 delay_time: Optional[float] = 3):
        super().__init__()
        self.api = api
        self.count = count
        self.sleep_time = sleep_time
        self.delay_time = delay_time

    async def run(self):
        while True:
            try:
                res = await self.api.fetch_message(count=self.count)
                for ev in res['data']:
                    await self._handle_event(ev)
            except ApiError:
                Logger.exception('Failed to fetch message.')
                Logger.error('Retrying in {} sec(s)', self.delay_time)
                await asyncio.sleep(self.delay_time)
            else:
                await asyncio.sleep(self.sleep_time)
