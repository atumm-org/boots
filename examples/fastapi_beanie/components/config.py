from typing import Literal

from ids import ObjectIds
from pydantic import BaseSettings

from buti import BootableComponent, ButiStore


class Config(BaseSettings):
    STAGE: Literal["dev", "test", "prod"] = "dev"
    DEBUG: bool = False
    MONGO_URL: str
    MONGO_DB_NAME: str


class ConfigComponent(BootableComponent):
    def boot(self, object_store: ButiStore):
        config: Config = Config(_env_file=".env", _env_file_encoding="utf-8")
        object_store.set(ObjectIds.config, config)
