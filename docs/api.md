---
sidebar: auto
---

# API

## `aiomirai.api` 模块

### _class_ `Api`

API 基类。
实现通过 HTTP 调用 Mirai API HTTP。

#### _function_ `__init__(api_root)`

**参数:**

+ `api_root: str`: Mirai API HTTP 服务地址.
  
#### _function_ `call_action(action, method, format, *, data, files, json, params, **kwargs)`

调用指定 API.

**参数:**

+ `action: str`: 要调用的 API 的名称. 可以直接传入名称, 也可以传入`snake_case`化的名称.
+ `method: Optional[str] = 'POST'`: 调用 API 所使用的 http method.
+ `format: Optional[str] = 'json`: 上报格式（可选的值有：data / json / params）
+ `data: Optional[RequestData] = None`
+ `files: Optional[RequestFiles] = None`
+ `json: Optional[Any] = None`
+ `params: Optional[QueryParamTypes] = None`: 这四个参数传入的数据将会在上报时**强制**使用该格式
+ `**kwargs`: 这部分传入的数据将会按照`format`中选择的格式上报

## `aiomirai.log` 模块

### _object_ `logger`

+ 类型: `logging.Logger`

+ `aiomirai` 全局的 logger.

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