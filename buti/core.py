from abc import ABC, abstractmethod
from collections import UserDict
from enum import Enum
from typing import Any, Dict, List, Optional, overload


class ButiKeys(Enum):
    """
    ButiKeys is an Enum that defines the keys used to store and retrieve data in the ButiStore.

    Each option represents a piece of data that a BootableComponent might need during the booting process.
    The options are defined as enum members, and they can be used as keys to set and get data in the ButiStore.

    see: examples/
    """

    pass


class ButiStore(UserDict):
    """
    The Buti Context, made to safely reference other dependent components
     or wait for the app to boot, and then in the post-boot have access to all the assigned built components

    see: examples/
    """

    def set(self, key: ButiKeys, value: Any) -> None:
        self.data[key] = value

    def get(self, key: ButiKeys, default: Any = None) -> Any:
        return self.data.get(key, default)


class BootableComponent(ABC):
    """
    An application component, that is bootable (can be an ORM/ODM, DependencyInjector, WebFramework... etc)

    see: examples/
    """

    @abstractmethod
    def boot(self, boot_image: ButiStore) -> None:
        raise NotImplementedError("Component not implemented")

    def post_boot(self, boot_image: ButiStore) -> None:
        pass


class Bootloader:
    """
    The Bootloader is responsible for managing the boot process of the application.

    It maintains a dictionary of BootableComponent instances, each representing a part of the application that needs to be
     initialized during the booting process. The BootLoader ensures that each component's boot method is called,
     in the order the components were added.

    The post_boot method is called after all the components have been booted. To do any extra work needed after boot

    The BootLoader uses a ButiStore instance as a shared context for the components during the booting process.
    Components can store and retrieve data in the ButiStore, allowing them to share data and resources.

    see: examples/
    """

    def __init__(self, buti_store: Optional[ButiStore] = None) -> None:
        self.buti_store = buti_store if buti_store is not None else ButiStore()
        self._components: Dict[str, BootableComponent] = {}

    def add_component(self, component: BootableComponent) -> None:
        self._components[component.__class__.__name__] = component

    def add_components(self, components: List[BootableComponent]) -> None:
        for component in components:
            self.add_component(component)

    def has_component(self, component: BootableComponent) -> bool:
        return component.__class__.__name__ in self._components

    def boot(self) -> ButiStore:
        for component in self._components.values():
            component.boot(self.buti_store)

        for component in self._components.values():
            component.post_boot(self.buti_store)

        return self.buti_store


class AsyncBootableComponent(ABC):
    """
    same as BootableComponent, see above
    """

    @abstractmethod
    async def boot(self, boot_image: ButiStore) -> None:
        raise NotImplementedError("Component not implemented")

    async def post_boot(self, boot_image: ButiStore) -> None:
        pass


class AsyncBootloader:
    """
    Same as Bootloader, see above
    """

    def __init__(self, buti_store: Optional[ButiStore] = None) -> None:
        self.buti_store = buti_store if buti_store is not None else ButiStore()
        self._components: Dict[str, AsyncBootableComponent] = {}

    def add_component(self, component: AsyncBootableComponent) -> None:
        self._components[component.__class__.__name__] = component

    def add_components(self, components: List[AsyncBootableComponent]) -> None:
        for component in components:
            self.add_component(component)

    def has_component(self, component: AsyncBootableComponent) -> bool:
        return component.__class__.__name__ in self._components

    async def boot(self) -> ButiStore:
        for component in self._components.values():
            await component.boot(self.buti_store)

        for component in self._components.values():
            await component.post_boot(self.buti_store)

        return self.buti_store
