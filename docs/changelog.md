---
sidebar: false
---

# 更新日志

## v0.3.7 (WIP)
+ API 调用 和 事件接收 的日志改为默认隐藏，可以通过 `aiomirai.logger.Api/Receiver.setLevel(logging.DEBUG)` 的方法重新启用
+ 新功能：支持通过 Http Polling 接收事件
+ 支持处理 Bot 被邀请入群请求

## v0.3.6
+ 如果未认证时（包括认证失败）调用 `release` 会伪造成功结果而不是抛出异常
+ 适配了 Quart v0.12.0
+ 更多的异常类型

## v0.3.5
+ 修复了“如果不使用事件接收器将无法运行”的问题
+ 新功能：支持通过 WebSocket 接收事件

## v0.3.4
+ 修复了 `MessageChain` 中几处关于 `Plain` 的错误

## v0.3.3 (bug fix)
## ~~v0.3.2~~
+ 使用 `quit` 方法退出群聊
+ `api_root`, `auth_key`, `qq`, `session_key` 修改为公共属性, 并添加至 `api.pyi`
+ **BREAKING CHANGE:** 调用 API 的返回值也应 `snake_case` 化

## v0.3.1 (bug fix)
## ~~v0.3.0~~
+ 重写了 `call_action` 方法, 目前理论上可以支持任意 API 调用
+ `Plain` 类型的消息段在转化为字符串时会返回 `text` 字段的内容而不是 `[Plain::text=context]`
+ 调用 `release` 方法后将自动重置 `_session_key`
+ 增加对 `resp/*RequestEvent` 的支持
+ 说明文档!
+ **BREAKING CHANGE:** `HttpReceiver` 重命名为 `ReportReceiver`, 并在将来会支持更多的 `Receiver`