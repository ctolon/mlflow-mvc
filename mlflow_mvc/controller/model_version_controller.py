from typing import Optional

from mlflow_mvc.service.model_version_service import ModelVersionService
from mlflow_mvc.config.core import Config

class ModelVersionController(object):
    """MLflow Model Version Controller Implementation"""
    
    def __init__(
        self,
        model_version_service = ModelVersionService(),
        tracking_uri: Optional[str] = None,
        ):
        if tracking_uri is not None:
            Config.set("TRACKING_SERVER_URI", tracking_uri)
    
        self._model_version_service = model_version_service
    
    def downloadLatestModel(self, model_name: str, model_path: str) -> None:
        return self._model_version_service.downloadLatestModel(model_name, model_path)
        
    def latestModelValidator(self, model_name, criteria: str, selected_metric: str) -> bool:
        model_name = Config.MODEL_NAME
        criteria = "700"
        selected_metric = "epoch"
        return self._model_version_service.latestModelValidator(model_name, criteria, selected_metric)
        
    