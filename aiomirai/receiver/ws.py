import asyncio
import json
import re
import socket
from typing import Optional

import websockets

from . import Receiver
from ..api import SessionApi
from ..exception import Unauthenticated
from ..logger import Receiver as Logger


class WsReceiver(Receiver):
    def __init__(self, api: SessionApi, ping_timeout: Optional[float] = 5, sleep_time: Optional[float] = 3):
        super().__init__()
        self.api = api
        self.api_root = re.sub(r'^http', 'ws', api.api_root)
        self.ping_timeout = ping_timeout
        self.sleep_time = sleep_time

    async def run(self):
        if self.api.session_key is None:
            raise Unauthenticated

        while True:
            try:
                async with websockets.connect(f'{self.api_root}all?sessionKey={self.api.session_key}') as ws:
                    while True:
                        try:
                            res = json.loads(await ws.recv())
                        except websockets.exceptions.ConnectionClosed:
                            try:
                                pong = await ws.ping()
                                await asyncio.wait_for(pong, timeout=self.ping_timeout)
                                Logger.debug('Ping OK, keeping connection alive...')
                                continue
                            except:
                                Logger.warning('Ping error - retrying connection in {} sec(s)'.format(self.sleep_time))
                                await asyncio.sleep(self.sleep_time)
                                break
                        if res.get('code') == 10:
                            Logger.error('Websocket is not enabled!')
                            Logger.error('Retrying connection in {} sec(s)'.format(self.sleep_time))
                            await asyncio.sleep(self.sleep_time)
                            break
                        await self._handle_event(res)
            except socket.gaierror:
                Logger.error('Socket error - retrying connection in {} sec(s)'.format(self.sleep_time))
                await asyncio.sleep(self.sleep_time)
                break
            except ConnectionRefusedError:
                Logger.error('Can NOT connect to Mirai API HTTP. Check if Mirai API HTTP is running.')
                Logger.error('Retrying connection in {} sec(s)'.format(self.sleep_time))
                await asyncio.sleep(self.sleep_time)
                break
