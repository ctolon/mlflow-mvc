"""Mlflow MVC Model Version Controller Module"""

from ..service._model_version_service import ModelVersionService


class ModelVersionController(object):
    """Mlflow MVC Model Version Controller Implementation"""

    def __init__(self,model_version_service: ModelVersionService):
        self._model_version_service = model_version_service

    def download_latest_model(self, model_name: str, model_path: str) -> None:
        return self._model_version_service.download_latest_model(model_name, model_path)

    def latest_model_validator(self, model_name, criteria: str, selected_metric: str) -> bool:
        return self._model_version_service.latest_model_validator(model_name, criteria, selected_metric)
