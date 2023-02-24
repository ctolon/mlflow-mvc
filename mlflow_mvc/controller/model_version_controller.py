"""Mlflow MVC Model Version Controller Module"""

from typing import Optional
from dependency_injector.wiring import inject

from ..service.model_version_service import ModelVersionService


class ModelVersionController(object):
    """Mlflow MVC Model Version Controller Implementation"""

    @inject
    def __init__(self, model_version_service: ModelVersionService):
        self._model_version_service = model_version_service

    def download_latest_model(self, model_name: str, model_path: str, model_format: Optional[str] = ".bin") -> None:
        return self._model_version_service.download_latest_model(model_name, model_path, model_format)

    def latest_model_validator(self, model_name: str, criteria: str, selected_metric: str) -> bool:
        return self._model_version_service.latest_model_validator(model_name, criteria, selected_metric)
