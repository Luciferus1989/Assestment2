import asyncio
from pathlib import Path
import time
import aiohttp

URL = 'https://cataas.com/cat'
CATS_WE_WANT = 10
OUT_PATH = Path(__file__).parent / 'cats'
OUT_PATH.mkdir(exist_ok=True, parents=True)
OUT_PATH = OUT_PATH.absolute()


async def get_cat(client: aiohttp.ClientSession, idx: int) -> bytes:
    async with client.get(URL) as response:
        print(response.status)
        result = await response.read()
        await asyncio.to_thread(save_to_disk, result, idx)


def save_to_disk(content: bytes, id: int):
    file_path = "{}/{}.png".format(OUT_PATH, id)
    with open(file_path, mode='wb') as f:
        f.write(content)


async def get_all_cats():

    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(15)) as client:
        tasks = [get_cat(client, i) for i in range(CATS_WE_WANT)]
        return await asyncio.gather(*tasks)


def main():
    start_time = time.time()
    res = asyncio.run(get_all_cats())
    end_time = time.time()
    print(len(res))
    print(f"Downloaded {len(res)} cats in {end_time - start_time:.2f} seconds")


if __name__ == '__main__':
    print('Change from feature-z. Final changes')
    main()
