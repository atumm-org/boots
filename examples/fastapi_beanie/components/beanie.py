from beanie import init_beanie
from components.config import Config
from fastapi import FastAPI
from ids import ObjectIds
from motor.motor_asyncio import AsyncIOMotorClient

from buti import BootableComponent, ButiStore


class BeanieComponent(BootableComponent):
    def boot(self, object_store: ButiStore):
        # get the configuration manager and FastAPI from the store
        config: Config = object_store.get(ObjectIds.config)
        app: FastAPI = object_store.get(ObjectIds.app)

        # Initialize the database connection
        beanie_client = AsyncIOMotorClient(config.MONGO_DB_NAME)

        @app.on_event("startup")
        async def beanie_startup():
            await init_beanie(db=beanie_client[config.DB_NAME], document_models=[])

        @app.on_event("shutdown")
        async def beanie_shutdown():
            beanie_client.close()

        # Store the database connection in the ButiStore
        object_store.set(ObjectIds.beanie, beanie_client)
