import time

import anyio
import asyncer
from asyncer import asyncify


def do_sync_work(name: str):
    time.sleep(1)
    return f"Hello, {name}"


async def do_work(name: str):
    await anyio.sleep(1)
    return f"Hello, {name}"


async def get_data():

    async with asyncer.create_task_group() as task_group:
        task_group.soonify(do_work)("Levy")
        task_group.soonify(do_work)("Marques")
        task_group.soonify(do_work)("Nunes")


async def main():
    await get_data()


if __name__ == "__main__":
    anyio.run(main)
