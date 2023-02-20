from typing import Optional

from mlflow_mvc.repository.registered_models_repository import RegisteredModelsRepository
from mlflow_mvc.util.master_logger import MasterLogger
from mlflow_mvc.config.core import Config

# Global logger settings
logger = MasterLogger().get_logger

class RegisteredModelsService(object):
    """MLflow Registered Models Service Implementation"""
    
    def __init__(
        self,
        registered_models_repository = RegisteredModelsRepository(),
        tracking_uri: Optional[str] = None
        ):
        if tracking_uri is not None:
            Config.set("TRACKING_SERVER_URI", tracking_uri)
            
        self._registered_models_repository = registered_models_repository
    
    def listAllRegisteredModels(self):
        return self._registered_models_repository.findAllRegisteredModels()