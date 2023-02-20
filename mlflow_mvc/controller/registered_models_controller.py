from typing import Optional

from mlflow_mvc.service.registered_models_service import RegisteredModelsService
from mlflow_mvc.config.core import Config

class RegisteredModelsController(object):
    """MLflow Registered Models Controller Implementation"""
    
    def __init__(self, registered_models_service = RegisteredModelsService(), tracking_uri: Optional[str] = None):
        if tracking_uri is not None:
            Config.set("TRACKING_SERVER_URI", tracking_uri)
        self._registered_models_service = registered_models_service
        
    