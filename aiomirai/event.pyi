from typing import Any, Dict, Optional

from .message import MessageChain


class Event(dict):
    """
    封装从 Mirai API HTTP 收到的事件数据对象（字典），提供属性以获取其中的字段。
    除 `type` 属性对于任何事件都有效外，其它属性存在与否（不存在则返回`None`）依事件不同而不同。
    """
    def type(self) -> str:
        """
        事件类型，详见 https://github.com/mamoe/mirai-api-http/blob/master/EventType.md
        """
        ...

    def message_chain(self) -> MessageChain:
        """消息事件中的消息链。"""
        ...

    def sender(self) -> Dict[str, Any]:
        """消息事件中的发送者信息。"""
        ...

    def qq(self) -> int:
        """Bot QQ 号。"""
        ...

    def auther_id(self) -> int:
        """撤回事件中消息原作者的 QQ 号。"""
        ...

    def message_id(self) -> int:
        """撤回事件中消息原作者的 QQ 号。"""
        ...

    # TODO: more autocompletion helper
