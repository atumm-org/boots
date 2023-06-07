from boots import ComponentOptions, BootableComponent, BootImage
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient


class BeanieComponentOptions(ComponentOptions):
    DATABASE_CONNECTION: str = "DATABASE_CONNECTION"


class BeanieComponent(BootableComponent):
    async def boot(self, boot_image: BootImage):
        # Initialize the database connection
        db = AsyncIOMotorClient("mongodb://localhost:27017").db
        await init_beanie(YourModel, db=db)

        # Store the database connection in the BootImage
        boot_image.set(BeanieComponentOptions.DATABASE_CONNECTION, db)
