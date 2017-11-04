import asyncio


fut = asyncio.Future()
fut.set_result(None)

async def _print(i, x):
    await fut
    print(f'{i} from worker {x}')


async def worker(x):
    print(f'worker {x}')

    for i in range(20):
        await _print(i, x)

if __name__ == '__main__':
    asyncio.ensure_future(worker(1))
    asyncio.ensure_future(worker(2))
    asyncio.ensure_future(worker(3))

    loop = asyncio.get_event_loop()

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.close()
