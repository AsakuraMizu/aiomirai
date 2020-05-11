"""
此模块提供了 Mirai API HTTP 的事件相关类。
"""

from enum import Enum
from typing import Any, Dict, Optional, Union

from .message import MessageChain
from .utils import snake_case

__all__ = ['Event']


class Event(dict):
    @property
    def type(self) -> str:
        return self['type']

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}, {super().__repr__()}>'


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
