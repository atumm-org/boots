from boots import ComponentOptions, BootableComponent, BootImage
from fastapi import FastAPI, APIRouter


class FastAPIComponentOptions(ComponentOptions):
    APP = "APP"


class FastAPIComponent(BootableComponent):
    async def boot(self, boot_image: BootImage):
        app = FastAPI()

        # Store the FastAPI app in the BootImage
        boot_image.set(FastAPIComponentOptions.APP, app)


class RouterComponent(BootableComponent):
    async def boot(self, boot_image: BootImage):
        # Retrieve the FastAPI app from the BootImage
        app = boot_image.get(FastAPIComponentOptions.APP)

        # Initialize an APIRouter
        router = APIRouter()

        # Set up a route that will be added to the FastAPI app
        @router.get("/additional_route")
        async def additional_route():
            return {"message": "This is an additional route"}

        # Add the router to the FastAPI app
        app.include_router(router)
