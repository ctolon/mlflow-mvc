"""Mlflow MVC Model Version Controller Module"""

from typing import Optional, Union
from dependency_injector.wiring import inject
from pathlib import Path
import os

from ..service.model_version_service import ModelVersionService


class ModelVersionController(object):
    """Mlflow MVC Model Version Controller Implementation"""

    @inject
    def __init__(self, model_version_service: ModelVersionService):
        self._model_version_service = model_version_service

    def download_latest_model(self, model_name: str, model_path: str, output_dir: Union[str, Path] = os.getcwd(), model_format: Optional[str] = ".bin") -> None:
        return self._model_version_service.download_latest_model(model_name, model_path, output_dir, model_format)
    
    def download_model_by_run_uuid(self, run_uuid: str, model_path_name: str, output_dir: Union[str, Path] = os.getcwd()) -> None:
        return self._model_version_service.download_model_by_run_uuid(run_uuid, model_path_name, output_dir)

    def latest_model_validator(self, model_name: str, criteria: str, selected_metric: str) -> bool:
        return self._model_version_service.latest_model_validator(model_name, criteria, selected_metric)
