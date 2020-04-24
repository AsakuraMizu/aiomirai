from typing import Union, Awaitable, Any, Optional, Dict, List

from .message import MessageChain


class Api:
    """
    API 基类。
    实现通过 HTTP 调用 Mirai API HTTP。
    """
    async def call_action(
            self,
            action: str,
            **params
        ) -> Any:
        """
        调用 Mirai API HTTP。

        Args:
            action: 所要调用的 API 名。
            params: API 所需参数

        Returns:
            Mirai API HTTP 返回的结果。
        """
        ...

    async def get_about(
            self
        ) -> Dict[str, Any]:
        """
        获取插件的信息，如版本号。
        """
        ...


class SessionApi(Api):
    """
    会话相关 API 实现类。
    """

    async def auth(
            self
        ) -> Dict[str, Any]:
        """
        验证身份，开始与 Mirai API 的会话。
        根据实现类的不同，此函数可能是异步也可能是同步函数。
        """
        ...

    async def verify(
            self
        ) -> Dict[str, Any]:
        """
        校验并激活 Session，同时将 Session 与 Bot 绑定
        """
        ...

    async def release(
            self
        ) -> Dict[str, Any]:
        """
        释放 session 及其相关资源
        """
        ...

    async def send_friend_message(
            self, *,
            target: int,
            quote: Optional[int] = None,
            message_chain: MessageChain
        ) -> Dict[str, Any]:
        """
        发送好友消息

        Args:
            target: 目标好友的 QQ 号
            quote: 引用消息的 messageId
            message_chain: 消息链
        """
        ...

    async def send_temp_message(
            self, *,
            qq: int,
            group: int,
            quote: Optional[int] = None,
            message_chain: MessageChain
        ) -> Dict[str, Any]:
        """
        发送临时会话消息

        Args:
            qq: 临时会话对象QQ号
            group: 临时会话群号
            quote: 引用消息的 messageId
            message_chain: 消息链
        """
        ...

    async def send_group_message(
            self, *,
            target: int,
            quote: Optional[int] = None,
            message_chain: MessageChain
        ) -> Dict[str, Any]:
        """
        发送群消息

        Args:
            target: 目标群的群号
            quote: 引用消息的 messageId
            message_chain: 消息链
        """
        ...

    async def send_image_message(
            self, *,
            urls: List[str],
            target: Optional[int],
            qq: Optional[int],
            group: Optional[int]
        ) -> List[str]:
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

    async def upload_image(
            self, *,
            type: str,
            img: bytes
        ) -> Dict[str, Any]:
        """
        上传图片文件

        Args:
            type: 类型（"friend" 或 "group"）
            img: 图片文件
        """
        ...
    
    async def recall(
            self, *,
            target: int
        ) -> Dict[str, Any]:
        """
        撤回消息

        Args:
            target: 要撤回的消息的 messageId
        """
        ...

    async def fetch_message(
            self, *,
            count: int
        ) -> Dict[str, Any]:
        """
        获取接收到的最老消息和最老各类事件（会从 MiraiApiHttp 消息记录中删除）

        Args:
            count: 获取消息和事件的数量
        """
        ...

    async def fetch_latest_message(
            self, *,
            count: int
        ) -> Dict[str, Any]:
        """
        获取接收到的最新消息和最新各类事件（会从 MiraiApiHttp 消息记录中删除）

        Args:
            count: 获取消息和事件的数量
        """
        ...

    async def peek_message(
            self, *,
            count: int
        ) -> Dict[str, Any]:
        """
        获取接收到的最老消息和最老各类事件（不会从 MiraiApiHttp 消息记录中删除）

        Args:
            count: 获取消息和事件的数量
        """
        ...

    async def peek_latest_message(
            self, *,
            count: int
        ) -> Dict[str, Any]:
        """
        获取接收到的最新消息和最新各类事件（不会从 MiraiApiHttp 消息记录中删除）

        Args:
            count: 获取消息和事件的数量
        """
        ...

    async def get_message_from_id(
            self, *,
            id: int
        ) -> Dict[str, Any]:
        """
        通过 messageId 获取一条被缓存的消息

        Args:
            id: 获取消息的 messageId
        """
        ...

    async def get_count_message(
            self
        ) -> Union[Awaitable[int], int]:
        """
        查看缓存的消息总数
        """
        ...

    async def get_friend_list(
            self
        ) -> List[Dict[str, Any]]:
        """
        获取好友列表
        """
        ...

    async def get_group_list(
            self
        ) -> List[Dict[str, Any]]:
        """
        获取群列表
        """
        ...

    async def get_member_list(
            self, *,
            target: int
        ) -> List[Dict[str, Any]]:
        """
        获取指定群的群成员列表

        Args:
            target: 指定群的群号
        """
        ...

    async def mute_all(
            self, *,
            target: int
        ) -> Dict[str, Any]:
        """
        指定群全体禁言（需要有相关限权）

        Args:
            target: 指定群的群号
        """
        ...

    async def unmute_all(
            self, *,
            target: int
        ) -> Dict[str, Any]:
        """
        指定群解除全体禁言（需要有相关限权）

        Args:
            target: 指定群的群号
        """
        ...

    async def mute(
            self, *,
            target: int,
            member_id: int,
            time: Optional[int]
        ) -> Dict[str, Any]:
        """
        指定群禁言指定群员（需要有相关限权）

        Args:
            target: 指定群的群号
            member_id: 指定群员QQ号
            time: 禁言时长，单位为秒，最多30天，默认为0
        """
        ...

    async def unmute(
            self, *,
            target: int,
            member_id: int,
        ) -> Dict[str, Any]:
        """
        指定群解除指定群员禁言（需要有相关限权）

        Args:
            target: 指定群的群号
            member_id: 指定群员QQ号
        """
        ...

    async def kick(
            self, *,
            target: int,
            member_id: int,
            msg: Optional[str]
        ) -> Dict[str, Any]:
        """
        移除指定群成员（需要有相关限权）

        Args:
            target: 指定群的群号
            member_id: 指定群员QQ号
            msg: 信息
        """
        ...

    async def group_config(
            self, *,
            target: int,
            config: Dict[str, Union[str, bool]]
        ) -> Dict[str, Any]:
        """
        修改群设置（需要有相关限权）

        Args:
            target: 指定群的群号
            config: 群设置（见 https://github.com/mamoe/mirai-api-http#群设置 ）
        """
        ...

    async def get_group_config(
            self, *,
            target: int
        ) -> Dict[str, Any]:
        """
        获取群设置

        Args:
            target: 指定群的群号
        """
        ...

    async def member_info(
            self, *,
            target: int,
            member_id: int,
            info: Dict[str, str]
        ) -> Dict[str, Any]:
        """
        修改群员资料（需要有相关限权）

        Args:
            target: 指定群的群号
            member_id: 群员QQ号
            info: 群员资料（见 https://github.com/mamoe/mirai-api-http#修改群员资料 ）
        """
        ...

    async def get_member_info(
            self, *,
            target: int,
            member_id: int
        ) -> Dict[str, Any]:
        """
        获取群员资料

        Args:
            target: 指定群的群号
            member_id: 群员QQ号
        """
        ...

    async def get_config(
            self
        ) -> Dict[str, Any]:
        """
        获取当前Session的配置信息，注意该配置是Session范围有效
        """
        ...

    async def config(
            self, *,
            cache_size: Optional[int],
            enable_websocket: Optional[bool]
        ) -> Dict[str, Any]:
        """
        设置当前Session的配置信息，注意该配置是Session范围有效

        Args:
            cache_size: 缓存大小
            enable_websocket: 是否开启Websocket
        """
        ...
