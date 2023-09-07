from buti.core import ButiKeys, ButiStore


class DemoKeys(ButiKeys):
    any_object_key: str = "any_object_key"


class TestButiStore:
    def test_set_and_get(self):
        buti_store = ButiStore()
        buti_store.set(DemoKeys.any_object_key, "any_value")
        assert buti_store.get(DemoKeys.any_object_key) == "any_value"
