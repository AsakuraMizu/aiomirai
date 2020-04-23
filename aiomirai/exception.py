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


class InvaildBot(AuthenticateError):
    """指定的 Bot 不存在。"""
    pass


class InvaildSession(AuthenticateError):
    """Session 失效或不存在。"""
    pass


class Unverified(AuthenticateError):
    """Session 未认证（未激活）。"""
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
