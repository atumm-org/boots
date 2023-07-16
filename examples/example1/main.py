import asyncio
from typing import List

from components.beanie import BeanieComponent
from components.config import ConfigComponent
from components.fastapi import FastAPIComponent, RouterComponent

from buti import BootableComponent, Bootloader

components: List[BootableComponent] = [
    ConfigComponent(),
    BeanieComponent(),
    FastAPIComponent(),
    RouterComponent(),
]


def main():
    # here we can optionally pass a ButiStore
    bootloader = Bootloader()

    bootloader.add_components(components)

    # this returns a generated ButiStore
    object_store = bootloader.boot()


if __name__ == "__main__":
    main()
