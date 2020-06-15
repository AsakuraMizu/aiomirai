"""
此模块提供了异常类。
"""


class Error(Exception):
    """`aiomirai` 所有异常的基类。"""
    pass


class ApiError(Error, RuntimeError):
    """调用 API 发生错误。"""
    pass


class Unauthenticated(ApiError):
    """未认证。"""
    pass


class ActionFailed(ApiError):
    """
    Mirai API HTTP 已收到 API 请求，但执行失败。
    """
    def __init__(self, code: int, msg: str):
        self.code = code
        self.msg = msg

    def __repr__(self):
        return f'<{self.__class__.__name__}, code={self.code}, msg={self.msg}>'

    def __str__(self):
        return self.__repr__()


class AuthenticateError(ActionFailed):
    """认证相关错误。"""
    pass


class InvalidAuthKey(AuthenticateError):
    """Auth Key错误。"""
    pass


class InvalidBot(AuthenticateError):
    """指定的 Bot 不存在。"""
    pass


class InvalidSession(AuthenticateError):
    """Session 失效或不存在。"""
    pass


class Unverified(AuthenticateError):
    """Session 未认证（未激活）。"""
    pass


class UnknownTarget(ActionFailed):
    """发送消息目标不存在(指定对象不存在)"""
    pass


class FileNotFound(ActionFailed):
    """指定文件不存在，出现于发送本地图片"""
    pass


class NoPermission(ActionFailed):
    """无操作权限，指Bot没有对应操作的限权"""
    pass


class BotMuted(ActionFailed):
    """Bot被禁言，指Bot当前无法向指定群发送消息"""
    pass


class MessageTooLong(ActionFailed):
    """消息过长"""
    pass


class HttpFailed(ApiError):
    """HTTP 请求响应码不是 2xx。"""
    def __init__(self, status_code: int):
        self.status_code = status_code
        """HTTP 响应码。"""

    def __repr__(self):
        return f'<HttpFailed, status_code={self.status_code}>'

    def __str__(self):
        return self.__repr__()


class NetworkError(Error, IOError):
    """网络错误。"""
    pass
