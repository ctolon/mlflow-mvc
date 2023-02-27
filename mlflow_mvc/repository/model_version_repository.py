"Mlflow MVC Model Version Repository Module"

from typing import List
from dependency_injector.wiring import inject

import mlflow
from mlflow.tracking.client import MlflowClient

from ..entities.model_version_entity import ModelVersionEntity
from ..util.generic_transformers import generic_multi_transformer


class ModelVersionRepository(MlflowClient):
    """Mlflow MVC Repository for Model Version Entity"""

    @inject
    def __init__(self, tracking_server_url: str, *args, **kwargs):
        mlflow.tracking.set_tracking_uri(tracking_server_url)
        super().__init__()

    def find_latest_model_version_by_model_name(self, model_name: str) -> ModelVersionEntity:
        latest_models = self.get_latest_versions(model_name)
        latest_model = latest_models[-1]
        return ModelVersionEntity(latest_model)

    def find_all_model_versions(self) -> List[dict]:
        all_models_versions = self.search_model_versions(filter_string="")
        return generic_multi_transformer(all_models_versions)

    def find_all_model_versions_by_name(self, model_name: str) -> List[dict]:
        all_models_versions = self.search_model_versions(filter_string="name = " + model_name)
        return generic_multi_transformer(all_models_versions)

    def find_model_version_by_name_and_version(self, name: str, version: str) -> ModelVersionEntity:
        model_version = self.get_model_version(name, version)
        return ModelVersionEntity(model_version)
