"""Mlflow MVC Model Version Service Interface"""

from interface import Interface
from typing import List
import os


class IModelVersionService(Interface):
    """Mlflow MVC Experiment Service Interface Class"""

    def download_latest_model(self, model_name: str, model_path_name: str, output_dir: str = os.getcwd(), model_format: str = ".bin") -> None:
        pass
    
    def latest_model_validator(self, model_name: str, criteria: str, selected_metric: str) -> bool:
        pass
    
    def list_all_model_versions(self) -> List[dict]:
        pass
