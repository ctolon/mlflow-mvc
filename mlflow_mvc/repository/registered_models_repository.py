import mlflow
from mlflow.tracking.client import MlflowClient
from typing import List, Optional

from mlflow_mvc.config.core import Config
from mlflow_mvc.util.generic_transformers import genericMultiTransformer

mlflow.set_tracking_uri(Config.get("TRACKING_SERVER_URI"))

class RegisteredModelsRepository(object):
    """MLflow Repository for Registered Models Entity"""
    
    def __init__(self, client: MlflowClient = MlflowClient(), tracking_uri: Optional[str] = None):
        if tracking_uri is not None:
            del client
            Config.set("TRACKING_SERVER_URI", tracking_uri)
            client = MlflowClient(tracking_uri=Config.get("TRACKING_SERVER_URI"))
        self._client = client
            
    def findAllRegisteredModels(self) -> List[dict]:
        all_registered_models = self._client.search_registered_models()
        return genericMultiTransformer(all_registered_models)