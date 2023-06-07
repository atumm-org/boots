from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Dict, List, Optional


class ComponentOptions(Enum):
    """
    ComponentOptions is an Enum that defines the keys used to store and retrieve data in the BootImage.

    Each option represents a piece of data that a BootableComponent might need during the booting process.
    The options are defined as enum members, and they can be used as keys to set and get data in the BootImage.

    see: examples/
    """

    pass


class BootImage:
    """
    This is what glues everything together, a Context if you will, to safely reference other dependent _components or
    wait for the app to boot, and then in the post-boot have access to all the _components with all the options

    For instance, you can have a FastAPI Component, that depends on a BeanieComponent, and uses it to assign variables
    inside the app object

    see: examples/
    """

    def __init__(self) -> None:
        self.vars: Dict[ComponentOptions, Any] = {}

    def set(self, option: ComponentOptions, value: Any) -> None:
        self.vars[option] = value

    def get(self, key: ComponentOptions) -> Any:
        return self.vars[key]


class BootableComponent(ABC):
    """
    An application component, that is bootable (can be Beanie ODM, DependencyInjector, WebFramework... etc)

    see: examples/
    """

    @abstractmethod
    async def boot(self, boot_image: BootImage) -> None:
        raise NotImplementedError("Component not implemented")

    async def post_boot(self, boot_image: BootImage) -> None:
        pass


class BootLoader:
    """
    The BootLoader is responsible for managing the boot process of the application.

    It maintains a list of BootableComponent instances, each representing a part of the application that needs to be
     initialized during the booting process. The BootLoader ensures that each component's boot method is called,
     in the order the components were added.

    The post_boot method is called after all the components have been booted. To do any exta work needed after boot

    The BootLoader uses a BootImage instance as a shared context for the components during the booting process.
    Components can store and retrieve data in the BootImage, allowing them to share data and resources.

    see: examples/
    """

    def __init__(self, boot_image: Optional[BootImage] = None):
        self.boot_image = boot_image if boot_image is not None else BootImage()
        self._components: List[BootableComponent] = []

    def add_component(self, component: BootableComponent) -> None:
        self._components.append(component)

    async def boot(self) -> BootImage:
        for component in self._components:
            await component.boot(self.boot_image)

        for component in self._components:
            await component.post_boot(self.boot_image)

        return self.boot_image
