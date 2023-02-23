"Mlflow MVC Model Version Repository Module"

from typing import List

import mlflow
from mlflow.entities.model_registry.model_version import ModelVersion
from mlflow.tracking.client import MlflowClient

from ..util.generic_transformers import generic_multi_transformer


class ModelVersionRepository(MlflowClient):
    """Mlflow MVC Repository for Model Version Entity"""

    def __init__(self, tracking_server_url: str, *args, **kwargs):
        mlflow.tracking.set_tracking_uri(tracking_server_url)
        super().__init__()

    def find_latest_model_version_by_model_name(self, model_name: str) -> ModelVersion:
        latest_models = self.get_latest_versions(model_name)
        latest_model = latest_models[-1]
        return latest_model

    def find_all_model_versions(self) -> List[dict]:
        all_models_versions = self.search_model_versions(filter_string="")
        return generic_multi_transformer(all_models_versions)

    def find_all_model_versions_by_name(self, model_name: str) -> List[dict]:
        all_models_versions = self.search_model_versions(filter_string="name = " + model_name)
        return generic_multi_transformer(all_models_versions)
