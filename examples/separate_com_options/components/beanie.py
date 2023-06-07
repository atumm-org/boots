from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from buti import BootableComponent, ButiKeys, ButiStore


class BeanieButiKeys(ButiKeys):
    DATABASE_CONNECTION: str = "DATABASE_CONNECTION"


class BeanieComponent(BootableComponent):
    async def boot(self, boot_image: ButiStore):
        # Initialize the database connection
        db = AsyncIOMotorClient("mongodb://localhost:27017").db
        await init_beanie(YourModel, db=db)

        # Store the database connection in the ButiStore
        boot_image.set(BeanieButiKeys.DATABASE_CONNECTION, db)
