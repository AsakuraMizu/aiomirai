"""
此模块提供了 Mirai API 的接口类。
"""

import abc
import functools
from typing import Callable, Any, Union, Awaitable, Dict


class Api:

    @abc.abstractmethod
    def call_action(self, action: str, **params) -> Union[Awaitable[Any], Any]:
        pass

    def __getattr__(self,
                    item: str) -> Callable[..., Union[Awaitable[Any], Any]]:
        """获取一个可调用对象，用于调用对应 API。"""
        return functools.partial(self.call_action, item)

class SessionApi(Api):

    @abc.abstractmethod
    def auth(self) -> Union[Awaitable[Dict[str, Any]], Dict[str, Any]]:
        pass

