from beanie import init_beanie
from components.config import Config
from ids import ObjectIds
from motor.motor_asyncio import AsyncIOMotorClient

from buti import BootableComponent, ButiStore


class BeanieComponent(BootableComponent):
    async def boot(self, object_store: ButiStore):
        # get the configuration manager from the store
        config: Config = object_store.get(ObjectIds.config)

        # Initialize the database connection
        beanie_db = AsyncIOMotorClient(config.MONGO_URL).db
        await init_beanie(db=beanie_db, document_models=[])

        # Store the database connection in the ButiStore
        object_store.set(ObjectIds.beanie, beanie_db)
