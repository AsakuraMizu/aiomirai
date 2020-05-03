"""
此模块提供了工具函数。
"""

import asyncio
import re
from typing import Any, Awaitable, Callable


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
