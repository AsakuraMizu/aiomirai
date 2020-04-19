from quart import Quart

from aiomirai import Event, HttpReceiver, HttpSessionApi, MessageChain

app = Quart(__name__)
rec = HttpReceiver(app)
api = HttpSessionApi('http://localhost:14253/', 'mirai', 10000)


@app.before_serving
async def _():
    await api.auth()
    await api.verify()


@rec.on('FriendMessage')
async def _(ev: Event):
    await api.send_friend_message(target=ev.sender['id'],
                                  message_chain=MessageChain('qwq'),
                                  quote=ev.message_chain[0]['id'])


if __name__ == "__main__":
    app.run()
