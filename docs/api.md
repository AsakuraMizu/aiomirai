---
sider: auto
---

# API

## `aiomirai.api` 模块

### _class_ `Api`

API 基类。
实现通过 HTTP 调用 Mirai API HTTP。

## `aiomirai.log` 模块

### _object_ `logger`

类型: `logging.Logger`

`aiomirai` 全局的 logger.

~~如果你看过 `nonebot` 源代码的话你会发现它俩一模一样~~

## `aiomirai.utils` 模块

此模块提供了工具函数。

### _function_ `camelCase`

将下划线命名法(snake_case)转换为小驼峰式命名法(camelCase).

用于构造 API 调用.

### _function_ `snake_case`

将小驼峰式命名法(camelCase)转换为下划线命名法(snake_case).

用于解析 API 返回的数据和接收到的事件.

### Example

```python
from aiomirai.utils import *
assert camelCase('send_friend_message') == 'sendFriendMessage'
assert 'send_friend_message' == snake_case('sendFriendMessage')
```