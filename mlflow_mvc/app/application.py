"""Application module."""

from fastapi import FastAPI

from . import fast_api_container
from . import experiment_endpoint
from . import model_version_endpoint
from . import registered_model_endpoint
from . import run_endpoint


def create_app() -> FastAPI:
    # Container Instance
    container = fast_api_container.FastAPIContainer()

    # FastAPI Instance
    app = FastAPI()

    # Set IoC Container to FastAPI for Dependency Injection
    app.container = container

    # Merge all routing options
    app.include_router(model_version_endpoint.router)
    app.include_router(registered_model_endpoint.router)
    app.include_router(experiment_endpoint.router)
    app.include_router(run_endpoint.router)

    # Return as FastAPI Backend Server
    return app


# Create App
app = create_app()
