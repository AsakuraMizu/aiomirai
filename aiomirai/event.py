"""
此模块提供了事件相关类。
"""

import asyncio
from collections import defaultdict
from typing import Any, Awaitable, Callable, Dict, List, Optional

from .message import MessageChain
from .utils import snake_case

__all__ = ['Event', 'EventBus', 'from_payload']


class Event(dict):
    @property
    def type(self) -> str:
        return self['type']

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}, {super().__repr__()}>'


class EventBus:
    def __init__(self):
        self._subscribers = defaultdict(set)

    def subscribe(self, event: str, func: Callable[[Event], Awaitable]) -> None:
        self._subscribers[event].add(func)

    def unsubscribe(self, event: str, func: Callable[[Event], Awaitable]) -> None:
        if func in self._subscribers[event]:
            self._subscribers[event].remove(func)

    def on(self, event: str):
        def decorator(func: Callable[[Event], Awaitable]) -> Callable[[Event], Awaitable]:
            self.subscribe(event, func)
            return func

        return decorator

    async def emit(self, event: str, *args, **kwargs) -> List[Any]:
        results = []
        coros = []
        for f in self._subscribers[event]:
            coros.append(f(*args, **kwargs))
        if coros:
            results += await asyncio.gather(*coros)
        return results


def from_payload(payload: Dict[str, Any]) -> Optional[Event]:
    """
    从 Mirai API HTTP 事件数据构造 `Event` 对象。
    """

    def _parse(data):
        if isinstance(data, dict):
            return {
                snake_case(k):
                    MessageChain(v) if k == 'messageChain' else _parse(v)
                for k, v in data.items()
            }
        elif isinstance(data, list):
            return [_parse(x) for x in data]
        else:
            return data

    try:
        e = Event(_parse(payload))
        _ = e.type
        return e
    except KeyError:
        return None
