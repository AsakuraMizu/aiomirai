from aiomirai import MessageChain, Poke, SessionApi


async def main():
    async with SessionApi(
            'http://localhost:8080/',
            'AuthKey',
            10000
        ) as api:
        await api.send_group_message(
            target=10000,
            message_chain=MessageChain(Poke('SixSixSix')),
        )


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
