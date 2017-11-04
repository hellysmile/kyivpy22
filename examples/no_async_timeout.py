import asyncio

import async_timeout


async def _print(i):
    print(f'{i}')


async def worker():
    for i in range(100500):
        await _print(i)

    print('done')


async def main():
    async with async_timeout.timeout(0.0001):
        await worker()


if __name__ == '__main__':
    asyncio.ensure_future(main())

    loop = asyncio.get_event_loop()

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.close()
