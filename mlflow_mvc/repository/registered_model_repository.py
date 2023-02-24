"Mlflow MVC Registered Models Repository Module"

from typing import List
import mlflow
from mlflow.tracking.client import MlflowClient
from mlflow.entities.model_registry import RegisteredModel

from ..util.generic_transformers import generic_multi_transformer


class RegisteredModelRepository(MlflowClient):
    """Mlflow MVC Repository for Registered Models Entity"""

    def __init__(self, tracking_server_url: str, *args, **kwargs):
        mlflow.tracking.set_tracking_uri(tracking_server_url)
        super().__init__()

    def find_all_registered_models(self) -> List[dict]:
        all_registered_models = self.search_registered_models()
        return generic_multi_transformer(all_registered_models)

    def find_registered_model_by_name(self, name: str) -> RegisteredModel:
        return self.get_registered_model(name)
