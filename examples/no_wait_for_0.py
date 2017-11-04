import asyncio


async def worker():
    await asyncio.sleep(0)
    print('done')


if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()

        loop.run_until_complete(asyncio.wait_for(worker(), 0))
    except asyncio.TimeoutError:
        print('TimeoutError')
