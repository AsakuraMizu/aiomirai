# 开始使用

## 示例 - 通过 HTTP POST 上报获取事件

使用你最熟悉的编辑器或 IDE, 创建一个名为 `bot.py` 的文件, 内容如下:

```python
from aiomirai import (Event,        # Mirai Api HTTP 上报的事件
                      MessageChain, # 消息链类型, 可用于构造消息链
                      SessionApi)   # 会话相关 API, 详见后文

# 需要安装 aiomirai[report]
from aiomirai import ReportReceiver
from quart import Quart

app = Quart(__name__)   # 使用 Quart 维护一个 Web 服务器
rec = ReportReceiver(app) # Mirai 消息接收器

api = SessionApi(
    'http://localhost:1080',    # Mirai API HTTP 所在主机的地址
    'authKey',                  # Mirai API HTTP 配置文件中的 authKey
    123456789                   # 登录 Bot 的 QQ 号
)

# 监听 FriendMessage 事件
@rec.on('FriendMessage')
async def _(ev: Event):
    # 使用 Async Context Manager (推荐)
    async with api:
        # 调用 sendFriendMessage
        await api.send_friend_message(
            target=ev['sender']['id'],
            message_chain=MessageChain('qwq'),
        )
    # 手动调用 (不推荐)
    # await api.auth()
    # await api.verify()
    # await api.send_friend_message(
    #     target=ev['sender']['id'],
    #     message_chain=MessageChain('qwq'),
    # )
    # await api.release()
```

在命令行里运行这段代码:

<Terminal :content="[
  { content: [{ text: 'python', class: 'input' }, ' bot.py'] },
]" static title="命令行" />

你将会看到类似下面这样的输出:

```
Running on http://0.0.0.0:5000 (CTRL + C to quit)
[2020-05-11 15:23:25,074] Running on 0.0.0.0:5000 over http (CTRL + C to quit)
```

## 配置 Mirai API HTTP

*[Mirai API HTTP 文档中关于上报服务的介绍](https://github.com/mamoe/mirai-api-http/blob/master/docs/report.md)*

为了使你的程序能够接收到 Mirai API HTTP 上报的消息, 你需要修改你的 Mirai API HTTP 插件的配置文件.

:::tip
如果你使用 [`mirai-docker`](https://github.com/AsakuraMizu/mirai-docker), 你只需要把你的 `docker-compose.yml` 文件中配置的环境变量 `MIRAI_HTTP_USE_REPORT` 改为 `"true"` 并把 `MIRAI_HTTP_REPORT_URL` 改为 `http://172.17.0.1:5000/mirai` 即可.

至于为什么是 `172.17.0.1` 而不是 `127.0.0.1`, 你可以参考 [Netwoking with standalone containers | Docker Documentation](https://docs.docker.com/network/network-tutorial-standalone/) 或自行谷歌.

同样的, 如果你的 Mirai API HTTP 与 `bot.py` 不是运行在同一台机器上的, 你应该把 `172.17.0.1` 改为运行 `bot.py` 的计算机的 ip.
:::

打开 `plugins/MiraiAPIHTTP/setting.yml`, 在文件最后加入下面这几行:
```yaml
report:
  enable: true
  groupMessage:
    report: true
  friendMessage:
    report: true
  eventMessage:
    report: true
  destinations:
    - http://127.0.0.1:5000/mirai
```

*提醒: 如果你的 Mirai API HTTP 与 `bot.py` 不是运行在同一台机器上的, 你应该把 `127.0.0.1` 改为运行 `bot.py` 的计算机的 ip.*

## 测试对话

给你的机器人发一段私聊消息, 如果一切正常, ta 应该会回复你"qwq"

<PanelView title="SiGNAL酱ᴮᴼᵀ">
  <ChatMessage nickname="water_lift" avatar="https://q1.qlogo.cn/g?b=qq&nk=2677294549&s=0">hello</ChatMessage>
  <ChatMessage nickname="SiGNAL酱ᴮᴼᵀ" avatar="https://q1.qlogo.cn/g?b=qq&nk=3021308132&s=0">qwq</ChatMessage>
</PanelView>

:::tip
如果没有回复, 请检查 `bot.py` 运行是否报错, mirai console日志是否报错. 如果都没有报错, 则可能是机器人账号被腾讯风控, 需要在同一环境中多登录一段时间.

如果你使用 [`mirai-docker`](https://github.com/AsakuraMizu/mirai-docker), 你可以将之前登陆过 bot 账号且能正常使用的 `device.json` 复制到 `docker-compose.yml` 所在文件夹, 即可伪装设备.
:::