import asyncio

import aiohttp
import async_timeout


async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:
            print(response)


async def main():
    async with async_timeout.timeout(0):
        await fetch()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
