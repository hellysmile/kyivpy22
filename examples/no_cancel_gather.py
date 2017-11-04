import asyncio
import logging

logging.basicConfig(level=logging.DEBUG)


async def coro1():
    await asyncio.sleep(1)
    print(1)


async def coro2():
    print(2)
    1 / 0


async def coro3():
    await asyncio.sleep(3)
    print(3)


async def waiter():
    await asyncio.gather(coro1(), coro2(), coro3())

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(waiter())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.close()
