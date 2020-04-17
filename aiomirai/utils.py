"""
此模块提供了工具函数。
"""

import asyncio
import re
from typing import Any, Awaitable, Callable

from quart.utils import run_sync


def ensure_async(func: Callable[..., Any]) -> Callable[..., Awaitable[Any]]:
    """
    确保可调用对象 `func` 为异步函数，如果不是，则使用 `run_sync`
    包裹，使其在 asyncio 的默认 executor 中运行。
    """
    if asyncio.iscoroutinefunction(func):
        return func
    else:
        return run_sync(func)


def camelCase(name: str) -> str:
    """
    将下划线命名法(snake_case)转换为小驼峰式命名法(camelCase)。
    """
    return re.sub(r'(.*?)_([a-z])', lambda m: m.group(1) + m.group(2).upper(),
                  name)


def snake_case(name: str) -> str:
    """
    将小驼峰式命名法(camelCase)转换为下划线命名法(snake_case)。
    """
    return re.sub(r'(.*?)([A-Z])',
                  lambda m: m.group(1) + '_' + m.group(2).lower(), name)


def sync_wait(coro: Awaitable[Any], loop: asyncio.AbstractEventLoop) -> Any:
    """
    在 `loop` 中线程安全地运行 `coro`，并同步地等待其运行完成，返回运行结果。
    """
    fut = asyncio.run_coroutine_threadsafe(coro, loop)
    return fut.result()
