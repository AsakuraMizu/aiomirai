from quart import Quart

from aiomirai import Event, HttpReceiver, MessageChain, SessionApi

app = Quart(__name__)
rec = HttpReceiver(app)
api = SessionApi('http://localhost:8080', 'authKey', 10000)

@rec.on('FriendMessage')
async def _(ev: Event):
    async with api:
        await api.send_friend_message(
            target=ev['sender']['id'],
            message_chain=MessageChain('qwq'),
        )


if __name__ == "__main__":
    app.run()
