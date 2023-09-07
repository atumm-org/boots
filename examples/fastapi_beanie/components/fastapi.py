from fastapi import APIRouter, FastAPI
from ids import ObjectIds

from buti import BootableComponent, ButiStore


class FastAPIComponent(BootableComponent):
    def boot(self, object_store: ButiStore):
        app = FastAPI()

        # Store the FastAPI app in the ButiStore
        object_store.set(ObjectIds.app, app)


class RouterComponent(BootableComponent):
    def boot(self, object_store: ButiStore):
        # Retrieve the FastAPI app from the ButiStore
        app = object_store.get(ObjectIds.app)

        # Initialize an APIRouter
        router = APIRouter()

        # Set up a route that will be added to the FastAPI app
        @router.get("/additional_route")
        async def additional_route():
            return {"message": "This is an additional route"}

        # Add the router to the FastAPI app
        app.include_router(router)
