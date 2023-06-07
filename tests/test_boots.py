from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock

import pytest

from boots import BootableComponent, BootImage, BootLoader, ComponentOptions

pytestmark = pytest.mark.anyio


class DemoOptions(ComponentOptions):
    ANY_OPTION = "ANY_OPTION"


class DemoComponent(BootableComponent):
    async def boot(self, boot_image: BootImage):
        pass


class TestBootImage:
    def test_set_and_get(self):
        boot_image = BootImage()
        boot_image.set(DemoOptions.ANY_OPTION, "any_value")
        assert boot_image.get(DemoOptions.ANY_OPTION) == "any_value"


class TestBootableComponent(IsolatedAsyncioTestCase):
    async def test_boot(self):
        try:
            bootable_component = AsyncMock()
            await bootable_component.boot(BootImage())
        except NotImplementedError:
            pytest.fail("NotImplementedError was raised")

    async def test_post_boot(self):
        pass


class TestBootLoader:
    def setup_method(self):
        self.boot_loader = BootLoader()

    def test_add_component(self):
        component = AsyncMock(spec=BootableComponent)
        self.boot_loader.add_component(component)
        assert component in self.boot_loader._components

    async def test_boot(self):
        component = AsyncMock(spec=BootableComponent)
        self.boot_loader.add_component(component)
        await self.boot_loader.boot()
        component.boot.assert_called_once()

    async def test_boot_calls_boot_and_post_boot_on_components(self):
        # Arrange
        boot_image = BootImage()
        boot_loader = BootLoader(boot_image)

        # Create mock components
        component1 = AsyncMock(BootableComponent)
        component2 = AsyncMock(BootableComponent)
        component1.post_boot = AsyncMock()
        component2.post_boot = AsyncMock()

        boot_loader.add_component(component1)
        boot_loader.add_component(component2)

        # Act
        await boot_loader.boot()

        # Assert
        component1.boot.assert_called_once_with(boot_image)
        component2.boot.assert_called_once_with(boot_image)

        component1.post_boot.assert_called_once_with(boot_image)
