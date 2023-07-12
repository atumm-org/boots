import asyncio
from typing import List

from components.beanie import BeanieComponent
from components.config import ConfigComponent
from components.fastapi import FastAPIComponent, RouterComponent

from buti import BootableComponent, BootLoader

components: List[BootableComponent] = [
    ConfigComponent(),
    BeanieComponent(),
    FastAPIComponent(),
    RouterComponent(),
]


async def main():
    # here we can optionally pass a ButiStore
    bootloader = BootLoader()

    bootloader.add_components(components)

    # this returns a generated ButiStore
    object_store = await bootloader.boot()


# Run the main function
asyncio.run(main())
