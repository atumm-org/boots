from ids import ObjectIds
from pydantic import BaseSettings

from buti import BootableComponent, ButiStore


class Config(BaseSettings):
    APP_ENV: str = "development"
    DEBUG: bool = False
    APP_HOST: str
    APP_PORT: int


class ConfigComponent(BootableComponent):
    async def boot(self, object_store: ButiStore):
        config: Config = Config(_env_file=".env", _env_file_encoding="utf-8")
        object_store.set(ObjectIds.config, config)
