from quart import Quart

from aiomirai import Event, HttpReceiver, MessageChain, SessionApi

app = Quart(__name__)
rec = HttpReceiver(app)
api = SessionApi('http://localhost:8080', 'AuthKey', 10000)

@app.before_serving
async def _():
    await api.auth()
    await api.verify()

@app.after_serving
async def _():
    await api.release()

@rec.on('FriendMessage')
async def _(ev: Event):
    await api.send_friend_message(
        target=ev.sender['id'],
        message_chain=MessageChain('qwq'),
    )


if __name__ == "__main__":
    app.run()
