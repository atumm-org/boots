import asyncio
from typing import List

from boots import BootLoader, BootableComponent
from components.fastapi import FastAPIComponent, RouterComponent
from components.beanie import BeanieComponent

components: List[BootableComponent] = [
    BeanieComponent(),
    FastAPIComponent(),
    RouterComponent()
]


async def main():
    # here we can ptionally passing a BootImage
    boot_loader = BootLoader()

    for component in components:
        boot_loader.add_component(component)

    # this returns a generated BootImage
    await boot_loader.boot()


# Run the main function
asyncio.run(main())
