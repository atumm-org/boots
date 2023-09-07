from unittest import TestCase
from unittest.mock import Mock

from buti.core import Bootloader


class MockComponent1(Mock):
    pass


class MockComponent2(Mock):
    pass


class TestBootloader(TestCase):
    def setUp(self):
        self.bootloader = Bootloader()

    def test_add_component(self):
        component = MockComponent1()
        self.bootloader.add_component(component)
        self.assertTrue(self.bootloader.has_component(component))

    def test_add_components(self):
        components = [MockComponent1(), MockComponent2()]
        self.bootloader.add_components(components)
        self.assertTrue(self.bootloader.has_component(components[0]))
        self.assertTrue(self.bootloader.has_component(components[1]))

    def test_add_components_constructor(self):
        components = [MockComponent1(), MockComponent2()]
        bootloader = Bootloader(components)
        self.assertTrue(bootloader.has_component(components[0]))
        self.assertTrue(bootloader.has_component(components[1]))

    def test_boot(self):
        component = MockComponent1()
        component.boot = Mock()
        self.bootloader.add_component(component)
        store = self.bootloader.boot()
        component.boot.assert_called_once()

    def test_boot_calls_boot_and_post_boot_on_components(self):
        component = MockComponent1()
        component.boot = Mock()
        component.post_boot = Mock()
        self.bootloader.add_component(component)
        self.bootloader.boot()
        component.boot.assert_called_once()
        component.post_boot.assert_called_once()
