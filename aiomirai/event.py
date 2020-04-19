"""
此模块提供了 Mirai API HTTP 事件相关的类。
"""

from typing import Any, Dict, Optional

from .utils import snake_case

__all__ = ['Event']

# TODO: Event Parser
# class Group(dict):
#     """事件发生所在的群。"""
#     def __init__(self, data: Dict[str, Any]):
#         super().__init__(data)

#     @property
#     def id(self) -> int:
#         """群号。"""
#         return self['id']

#     @property
#     def name(self) -> str:
#         """群名。"""
#         return self['name']

#     @property
#     def permission(self) -> str:
#         """Bot在群中的权限，OWNER、ADMINISTRATOR或MEMBER。"""
#         return self['permission']

# class Operator(dict):
#     """
#     群事件中的操作者。

#     应当注意好友消息撤回事件也使用 operator 字段。
#     """
#     def __init__(self, data: Optional[Dict[str, Any]]):


class Event(dict):
    def __init__(self, data: Dict[str, Any]):
        _data = {snake_case(k): v for k, v in data.items()}
        super().__init__(_data)

    @property
    def type(self) -> str:
        """
        事件类型，详见 https://github.com/mamoe/mirai-api-http/blob/master/EventType.md
        """
        return self['type']

    def __repr__(self) -> str:
        return f'<Event, {super().__repr__()}>'

    def __getattr__(self, item: str) -> Any:
        return self.get(item)


def from_payload(payload: Dict[str, Any]) -> Optional[Event]:
    """
    从 Mirai API HTTP 事件数据构造 `Event` 对象。
    """
    try:
        e = Event(payload)
        _ = e.type
        return e
    except KeyError:
        return None
