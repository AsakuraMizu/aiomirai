---
sidebar: auto
---

# API

## `aiomirai.api` 模块

### _class_ `Api`

API 基类.
实现通过 HTTP 调用 Mirai API HTTP.

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

**异常:**

+ **`NetworkError`**
+ **`HttpFailed`**
+ **`ActionFailed`**

#### _function_ `get_about()`

调用 `/about` API.

### _class_ `SessionApi`

会话相关 API 实现类. 是 `Api` 的子类.

#### _function_ `__init__(api_root, auth_key, qq)`

**参数:**

+ `api_root: str`: Mirai API HTTP 服务地址.
+ `auth_key: str`: auth key
+ `qq: int` 要绑定的 Bot 的 qq 号

#### _function_ `call_action(action, method, format, *, data, files, json, params, **kwargs)`

调用指定 API.

相比基类 `Api` 的 `call_action` 方法, 该方法会自动传入 `session_key` 作为请求的参数之一.

**异常:**

+ `NetworkError`
+ `HttpFailed`
+ `ActionFailed`
+ **`Unauthenticated`**
+ **`InvalidAuthKey`**
+ **`InvalidBot`**
+ **`InvalidSession`**: 
+ **`Unverified`**
+ **`UnknownTarget`**
+ **`FileNotFound`**
+ **`NoPermission`**
+ **`BotMuted`**
+ **`MessageTooLong`**

#### _function_ `auth()`
#### _function_ `verify()`
#### _function_ `release()`
#### _function_ `send_friend_message(*, target, quote, message_chain)`
#### _function_ `send_temp_message(*, qq, group, quote, message_chain)`
#### _function_ `send_group_message(*, target, quote, message_chain)`
#### _function_ `send_image_message(*, urls, target, qq, group)`
#### _function_ `upload_image(*, type, img)`
#### _function_ `recall(*, target)`
#### _function_ `fetch_message(*, count)`
#### _function_ `fetch_latest_message(*, count)`
#### _function_ `peek_message(*, count)`
#### _function_ `peek_latest_message(*, count)`
#### _function_ `get_message_from_id(*, id)`
#### _function_ `get_count_message()`
#### _function_ `get_friend_list()`
#### _function_ `get_group_list()`
#### _function_ `get_member_list(*, target)`
#### _function_ `mute_all(*, target)`
#### _function_ `unmute_all(*, target)`
#### _function_ `mute(*, target, member_id, time)`
#### _function_ `unmute(*, target, member_id)`
#### _function_ `kick(*, target, member_id, msg)`
#### _function_ `quit(*, target)`
#### _function_ `group_config(*, target, config)`
#### _function_ `get_group_config(*, target)`
#### _function_ `member_info(*, target, member_id, info)`
#### _function_ `get_member_info(*, target, member_id)`
#### _function_ `config(*, cache_size, enable_websocket)`
#### _function_ `get_config()`
#### _function_ `resp_new_friend(*, event_id, from_id, group_id, operate, message)`
#### _function_ `resp_member_join(*, event_id, from_id, group_id, operate, message)`
#### _function_ `resp_bot_invited_join_group(*, event_id, from_id, group_id, operate, message)`

注意:
+ 这些函数都必须以具名参数的方式传参(就像 [aiocqhttp](https://github.com/cqmoe/python-aiocqhttp) 中那样). 
  例如, 你应该使用 `api.recall(target=-123456)` 而不是 `api.recall(-123456)`
+ 形如 `get_xxx` 的函数, 实际上会调用 `[GET] /xxx` 而不是 `[POST] /get_xxx`
+ 形如 `fetch_xxx` 和 `peek_yyy` 的函数, 实际上会调用 `[GET] /fetch_xxx`  `[GET] /peek_xxx`
+ 三个 `resp_xxx` 函数为事件响应函数, 实际上调用的是 `/resp/xxx`

## `aiomirai.receiver` 模块

### _class_ `PollingReceiver`

### _class_ `ReportReceiver`

### _class_ `WsReceiver`

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