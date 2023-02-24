"""Application module."""

from fastapi import FastAPI

from . import fast_api_container
from . import experiment_endpoint  # must be strong
from . import model_version_endpoint
from . import registered_model_endpoint
from . import run_endpoint


def create_app() -> FastAPI:
    container = fast_api_container.FastAPIContainer()

    # FastAPI Instance
    app = FastAPI()

    # DI for FastAPI
    app.container = container

    app.include_router(model_version_endpoint.router)
    app.include_router(registered_model_endpoint.router)
    app.include_router(experiment_endpoint.router)
    app.include_router(run_endpoint.router)

    # Return as FastAPI Backend Server
    return app


# Create App
app = create_app()
