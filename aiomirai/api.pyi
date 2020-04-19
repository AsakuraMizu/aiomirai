from typing import Union, Awaitable, Any, Optional, Dict, List

from .message import MessageChain


class Api:
    """
    API 接口类。
    继承此类的具体实现类应实现 `call_action` 方法。
    """

    def call_action(
            self,
            action: str,
            **params
        ) -> Union[Awaitable[Any], Any]:
        """
        调用 Mirai API，`action` 为要调用的 API 动作名，`**params`
        为 API 所需参数。
        根据实现类的不同，此函数可能是异步也可能是同步函数。
        """
        ...

    def get_about(
            self
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        获取插件的信息，如版本号。
        """
        ...


class SessionApi(Api):
    """
    API 接口类，继承自 `Api`，提供会话相关接口。
    继承此类的具体实现类应实现 `call_action` 和 `auth` 方法。
    """

    def auth(
            self
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        验证身份，开始与 Mirai API 的会话。
        根据实现类的不同，此函数可能是异步也可能是同步函数。
        """
        ...

    def verify(
            self
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        校验并激活 Session，同时将 Session 与 Bot 绑定
        """
        ...

    def release(
            self
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        释放 session 及其相关资源
        """
        ...

    def send_friend_message(
            self, *,
            target: int,
            message_chain: MessageChain,
            quote: Optional[int] = None
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        发送好友消息

        Args:
            target: 目标好友的 QQ 号
            message: 消息链
            quote: 引用消息的 messageId
        """
        ...

    def send_temp_message(
            self, *,
            target: int,
            message_chain: MessageChain,
            quote: Optional[int] = None
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        发送临时会话消息

        Args:
            target: 临时会话对象 QQ 号
            message: 消息链
            quote: 引用消息的 messageId
        """
        ...

    def send_group_message(
            self, *,
            target: int,
            message_chain: MessageChain,
            quote: Optional[int] = None
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        发送群消息

        Args:
            target: 目标群的群号
            message: 消息链
            quote: 引用消息的 messageId
        """
        ...

    def send_image_message(
            self, *,
            urls: List[str],
            target: Optional[int],
            qq: Optional[int],
            group: Optional[int]
        ) -> Union[Awaitable[List[str]], List[str]]:
        """
        发送图片消息（通过URL）
        除非需要通过此手段获取imageId，否则不推荐使用该接口

        Args:
            urls: 由 url 字符串构成的数组
            target: 发送对象的 QQ 号或群号，可能存在歧义
            qq: 发送对象的 QQ 号
            group: 发送对象的群号
        """
        ...

    def upload_image(
            self, *,
            type: str,
            img: bytes
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        上传图片文件

        Args:
            type: 类型（"friend" 或 "group"）
            img: 图片文件
        """
        ...
    
    def recall(
            self, *,
            target: int
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        撤回消息

        Args:
            target: 要撤回的消息的 messageId
        """
        ...

    def fetch_message(
            self, *,
            count: int
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        获取接收到的最老消息和最老各类事件（会从 MiraiApiHttp 消息记录中删除）

        Args:
            count: 获取消息和事件的数量
        """
        ...

    def fetch_latest_message(
            self, *,
            count: int
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        获取接收到的最新消息和最新各类事件（会从 MiraiApiHttp 消息记录中删除）

        Args:
            count: 获取消息和事件的数量
        """
        ...

    def peek_message(
            self, *,
            count: int
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        获取接收到的最老消息和最老各类事件（不会从 MiraiApiHttp 消息记录中删除）

        Args:
            count: 获取消息和事件的数量
        """
        ...

    def peek_latest_message(
            self, *,
            count: int
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        获取接收到的最新消息和最新各类事件（不会从 MiraiApiHttp 消息记录中删除）

        Args:
            count: 获取消息和事件的数量
        """
        ...

    def get_message_from_id(
            self, *,
            id: int
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        通过 messageId 获取一条被缓存的消息

        Args:
            id: 获取消息的 messageId
        """
        ...

    def get_count_message(
            self
        ) -> Union[Awaitable[int], int]:
        """
        查看缓存的消息总数
        """
        ...

    def get_friend_list(
            self
        ) -> Union[Awaitable[List[Dict[str, Any]]], List[Dict[str, Any]]]:
        """
        获取好友列表
        """
        ...

    def get_group_list(
            self
        ) -> Union[Awaitable[List[Dict[str, Any]]], List[Dict[str, Any]]]:
        """
        获取群列表
        """
        ...

    def get_member_list(
            self, *,
            target: int
        ) -> Union[Awaitable[List[Dict[str, Any]]], List[Dict[str, Any]]]:
        """
        获取指定群的群成员列表

        Args:
            target: 指定群的群号
        """
        ...

    def mute_all(
            self, *,
            target: int
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        指定群全体禁言（需要有相关限权）

        Args:
            target: 指定群的群号
        """
        ...

    def unmute_all(
            self, *,
            target: int
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        指定群解除全体禁言（需要有相关限权）

        Args:
            target: 指定群的群号
        """
        ...

    def mute(
            self, *,
            target: int,
            member_id: int,
            time: Optional[int]
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        指定群禁言指定群员（需要有相关限权）

        Args:
            target: 指定群的群号
            member_id: 指定群员QQ号
            time: 禁言时长，单位为秒，最多30天，默认为0
        """
        ...

    def unmute(
            self, *,
            target: int,
            member_id: int,
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        指定群解除指定群员禁言（需要有相关限权）

        Args:
            target: 指定群的群号
            member_id: 指定群员QQ号
        """
        ...

    def kick(
            self, *,
            target: int,
            member_id: int,
            msg: Optional[str]
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        移除指定群成员（需要有相关限权）

        Args:
            target: 指定群的群号
            member_id: 指定群员QQ号
            msg: 信息
        """
        ...

    def group_config(
            self, *,
            target: int,
            config: Dict[str, Union[str, bool]]
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        修改群设置（需要有相关限权）

        Args:
            target: 指定群的群号
            config: 群设置（见 https://github.com/mamoe/mirai-api-http#群设置 ）
        """
        ...

    def get_group_config(
            self, *,
            target: int
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        获取群设置

        Args:
            target: 指定群的群号
        """
        ...

    def member_info(
            self, *,
            target: int,
            member_id: int,
            info: Dict[str, str]
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        修改群员资料（需要有相关限权）

        Args:
            target: 指定群的群号
            member_id: 群员QQ号
            info: 群员资料（见 https://github.com/mamoe/mirai-api-http#修改群员资料 ）
        """
        ...

    def get_member_info(
            self, *,
            target: int,
            member_id: int
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        获取群员资料

        Args:
            target: 指定群的群号
            member_id: 群员QQ号
        """
        ...

    def get_config(
            self
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        获取当前Session的配置信息，注意该配置是Session范围有效
        """
        ...

    def config(
            self, *,
            cache_size: Optional[int],
            enable_websocket: Optional[bool]
        ) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        """
        设置当前Session的配置信息，注意该配置是Session范围有效

        Args:
            cache_size: 缓存大小
            enable_websocket: 是否开启Websocket
        """
        ...

class AsyncApi(Api):
    """
    异步 API 接口类。
    继承此类的具体实现类应实现异步的 `call_action` 方法。
    """
    async def call_action(
            self,
            action: str,
            **params
        ) -> Any:
        """
        异步地调用 Mirai API，`action` 为要调用的 API 动作名，`**params`
        为 API 所需参数。
        """
        ...


class AsyncSessionApi(SessionApi, AsyncApi):
    """
    异步 API 接口类，提供会话相关接口。
    继承此类的具体实现类应实现异步的 `call_action` 方法。
    """
    ...
