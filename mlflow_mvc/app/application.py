"""Application module."""

from fastapi import FastAPI

#from ._containers import Container # must be strong
#from . import _fast_api_container
from . import _fast_api_container
from . import _experiment_endpoint # must be strong
from . import _model_version_endpoint
from . import _registered_model_endpoint
from . import _run_endpoint

def create_app() -> FastAPI:
    container = _fast_api_container.FastAPIContainer()

    # FastAPI Instance
    app = FastAPI()
    
    # DI for FastAPI
    app.container = container
    
    app.include_router(_model_version_endpoint.router)
    app.include_router(_registered_model_endpoint.router)
    app.include_router(_experiment_endpoint.router)
    app.include_router(_run_endpoint.router)
    
    # Return as FastAPI Backend Server
    return app

# Create App
app = create_app()