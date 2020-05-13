---
sidebar: auto
---

# 更新日志

## v0.3.2
### API
+ 使用 `quit` 方法退出群聊
+ `api_root`, `auth_key`, `qq`, `session_key` 修改为公共属性, 并添加至 `api.pyi`
+ **BREAKING CHANGE:** 调用 API 的返回值也应 `snake_case` 化

## v0.3.0
**此版本存在严重 BUG, 请使用 v0.3.1 代替**
+ 重写了 `call_action` 方法, 目前理论上可以支持任意 API 调用
+ `Plain` 类型的消息段在转化为字符串时会返回 `text` 字段的内容而不是 `[Plain::text=context]`
+ 调用 `release` 方法后将自动重置 `_session_key`
+ 增加对 `resp/*RequestEvent` 的支持
+ 说明文档!
+ **BREAKING CHANGE:** `HttpReceiver` 重命名为 `ReportReceiver`, 并在将来会支持更多的 `Receiver`