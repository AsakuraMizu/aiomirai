---
sidebar: auto
---

# 更新日志

## v0.3.0

+ 重写了 `call_action` 方法, 目前理论上可以支持任意 API 调用
+ `Plain` 类型的消息段在转化为字符串时会返回 `text` 字段的内容而不是 `[Plain::text=context]`
+ 调用 `release` 方法后将自动重置 `_session_key`
+ 增加对 `resp/*RequestEvent` 的支持
+ 说明文档!
+ **BREAKING CHANGE:** `HttpReceiver` 重命名为 `ReportReceiver`, 并在将来会支持更多的 `Receiver`