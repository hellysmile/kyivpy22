import asyncio

import aiohttp


async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:
            print(response)


async def main():
    await asyncio.wait_for(fetch(), 10)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
