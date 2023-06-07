from fastapi import APIRouter, FastAPI

from buti import BootableComponent, ButiKeys, ButiStore


class FastAPIButiKeys(ButiKeys):
    APP = "APP"


class FastAPIComponent(BootableComponent):
    async def boot(self, boot_image: ButiStore):
        app = FastAPI()

        # Store the FastAPI app in the ButiStore
        boot_image.set(FastAPIButiKeys.APP, app)


class RouterComponent(BootableComponent):
    async def boot(self, boot_image: ButiStore):
        # Retrieve the FastAPI app from the ButiStore
        app = boot_image.get(FastAPIButiKeys.APP)

        # Initialize an APIRouter
        router = APIRouter()

        # Set up a route that will be added to the FastAPI app
        @router.get("/additional_route")
        async def additional_route():
            return {"message": "This is an additional route"}

        # Add the router to the FastAPI app
        app.include_router(router)
