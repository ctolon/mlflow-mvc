import mlflow
from mlflow.tracking.client import MlflowClient
from mlflow.entities.model_registry.model_version import ModelVersion
from typing import List, Optional

from mlflow_mvc.config.core import Config
from mlflow_mvc.util.generic_transformers import genericMultiTransformer

mlflow.set_tracking_uri(Config.get("TRACKING_SERVER_URI"))

class ModelVersionRepository(object):
    """MLflow Repository for Model Version Entity"""
    
    def __init__(self, client: MlflowClient = MlflowClient(), tracking_uri: Optional[str] = None):
        if tracking_uri is not None:
            del client
            Config.set("TRACKING_SERVER_URI", tracking_uri)
            client = MlflowClient(tracking_uri=Config.get("TRACKING_SERVER_URI"))
        self._client = client

    def findLatestModelVersionByModelName(self, model_name: str) -> ModelVersion:
        latest_models = self._client.get_latest_versions(model_name)
        latest_model = latest_models[-1]
        return latest_model
                            
    def findAllModelVersions(self) -> List[dict]:
        all_models_versions = self._client.search_model_versions(filter_string="")
        return genericMultiTransformer(all_models_versions)