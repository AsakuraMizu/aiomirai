# 安装

## Mirai, Mirai API HTTP

首先你需要搭建起一个 mirai 的运行环境.

你可以参考 `python-mirai` 的说明文档 [使用 mirai-console](https://mirai-py.originpages.com/mirai/use-console.html) 和 [启动无头客户端](https://mirai-py.originpages.com/tutorial/hello-world.html#%E5%90%AF%E5%8A%A8%E6%97%A0%E5%A4%B4%E5%AE%A2%E6%88%B7%E7%AB%AF)

## aiomirai

### 安装

#### 从 PyPI 安装

<Terminal :content="[
  { content: [{ text: 'pip', class: 'input' }, ' install aiomirai'] },
]" static title="命令行" />

#### 从 Github 源代码仓库安装

<Terminal :content="[
  { content: [{ text: 'pip', class: 'input' }, ' install git+git://github.com/AsakuraMizu/aiomirai.git#egg=aiomirai'] },
]" static title="命令行" />

#### 手动安装

<Terminal :content="[
  { content: [{ text: 'git', class: 'input' }, ' clone https://github.com/AsakuraMizu/aiomirai.git'] },
  { content: [{ text: 'cd', class: 'input' }, ' aiomirai'] },
  { content: [{ text: 'pip', class: 'input' }, ' install -p'] },
  { content: [{ text: 'python', class: 'input' }, ' setup.py install'] },
]" static title="命令行" />

### 使用其他工具

如果您是 Python 开发者, 您或许会使用 [`virtualenv`](https://github.com/pypa/virtualenv), [`pipenv`](https://github.com/pypa/pipenv), [`poetry`](https://github.com/python-poetry/poetry) 等工具.

### 可选功能

<Terminal :content="[
  { content: [{ text: '# 全部功能', class: 'hint' }] },
  { content: [{ text: 'pip', class: 'input' }, ' install aiomirai[all]'] },
  { content: [{ text: '# 事件接收: 通过 HTTP POST 上报', class: 'hint' }] },
  { content: [{ text: 'pip', class: 'input' }, ' install aiomirai[report]'] },
  { content: [{ text: '# 事件接收: 通过 HTTP 轮询', class: 'hint' }] },
  { content: [{ text: 'pip', class: 'input' }, ' install aiomirai[poll]'] },
  { content: [{ text: '# 事件接收: 通过 WebSocket', class: 'hint' }] },
  { content: [{ text: 'pip', class: 'input' }, ' install aiomirai[ws]'] },
]" static title="命令行" />
