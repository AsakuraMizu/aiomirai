"""
此模块提供了异常类。
"""

__all__ = [
    'Error', 'ApiNotAvailable', 'ApiError',
    'HttpFailed', 'ActionFailed', 'NetworkError', 'TimingError',
]


class Error(Exception):
    """`aiomirai` 所有异常的基类。"""
    pass


class ApiNotAvailable(Error):
    """Mirai API HTTP 不可用。"""
    pass


class ApiError(Error, RuntimeError):
    """调用 Mirai API HTTP 发生错误。"""
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


class ActionFailed(ApiError):
    """
    Mirai API HTTP 已收到 API 请求，但执行失败。
    """

    def __init__(self, retcode: int, msg: str):
        self.retcode = retcode
        self.msg = msg

    def __repr__(self):
        return f'<ActionFailed, retcode={self.retcode}, msg={self.msg}>'

    def __str__(self):
        return self.__repr__()


class NetworkError(Error, IOError):
    """网络错误。"""
    pass


class TimingError(Error):
    """时机错误。"""
    pass