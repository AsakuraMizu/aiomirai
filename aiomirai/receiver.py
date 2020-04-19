"""
此模块提供了 Mirai API HTTP 事件接收相关类。
"""

from typing import Any, Dict

from quart import Quart, Response, abort, jsonify, request

from .bus import EventBus
from .event import from_payload
from .logger import Receiver as Logger

__all__ = ['HttpReceiver']


class Receiver(EventBus):
    async def _handle_event(self, payload: Dict[str, Any]) -> Any:
        ev = from_payload(payload)
        if not ev:
            return

        event_name = ev.type

        results = list(
            filter(lambda r: r is not None, await self.emit(event_name, ev)))
        # return the first non-none result
        return results[0] if results else None


class HttpReceiver(Receiver):
    def __init__(self, app: Quart, endpoint: str = '/mirai'):
        super().__init__()
        app.add_url_rule(path=endpoint,
                         endpoint=endpoint,
                         view_func=self._postreceive,
                         methods=['POST'])

    async def _postreceive(self) -> Response:
        payload = await request.json
        Logger.info('Received: %s', str(payload))
        if not isinstance(payload, dict):
            abort(400)

        response = await self._handle_event(payload)
        if isinstance(response, dict):
            return jsonify(response)
        return Response('', 204)
