import asyncio


async def _print(i):
    print(f'{i}')
    await asyncio.sleep(0)


async def worker():
    for i in range(100500):
        await _print(i)

    print('done')


if __name__ == '__main__':
    asyncio.ensure_future(asyncio.wait_for(worker(), timeout=0.0001))

    loop = asyncio.get_event_loop()

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.close()
