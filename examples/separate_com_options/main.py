import asyncio
from typing import List

from components.beanie import BeanieComponent
from components.fastapi import FastAPIComponent, RouterComponent

from buti import BootableComponent, BootLoader

components: List[BootableComponent] = [
    BeanieComponent(),
    FastAPIComponent(),
    RouterComponent(),
]


async def main():
    # here we can ptionally passing a ButiStore
    boot_loader = BootLoader()

    for component in components:
        boot_loader.add_component(component)

    # this returns a generated ButiStore
    await boot_loader.boot()


# Run the main function
asyncio.run(main())
