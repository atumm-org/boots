from buti import BootableComponent, ButiStore
from decouple import config as cfg
from pydantic import BaseSettings

from ids import ObjectIds


class Config(BaseSettings):
    MONGO_URL: str = cfg("MONGO_URL")


class ConfigComponent(BootableComponent):
    async def boot(self, object_store: ButiStore):
        config: Config = object_store.get(ObjectIds.config)
        object_store.set(ObjectIds.config, config)
