"""
此模块提供了 Mirai API HTTP 事件接收相关类。
"""

from typing import Any, Dict

from ..bus import EventBus
from ..event import from_payload
from ..logger import Receiver as Logger

__all__ = ['Receiver']


class Receiver(EventBus):
    async def _handle_event(self, payload: Dict[str, Any]) -> Any:
        Logger.debug('Received: %s', str(payload))
        ev = from_payload(payload)
        if not ev:
            return

        event_name = ev.type

        results = list(
            filter(lambda r: r is not None, await self.emit(event_name, ev)))
        # return the first non-none result
        return results[0] if results else None


try:
    from .report import ReportReceiver
    __all__ += ['ReportReceiver']
except ImportError:
    pass

try:
    from .ws import WsReceiver
    __all__ += ['WsReceiver']
except ImportError:
    pass

try:
    from .polling import PollingReceiver
    __all__ += ['PollingReceiver']
except ImportError:
    pass
