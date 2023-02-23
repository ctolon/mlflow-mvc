"""Mlflow MVC Experiment Service Interface"""

from typing import List
from interface import  Interface

class IExperimentService(Interface):
    """Mlflow MVC Experiment Service Interface Class"""

    def list_all_experiments(self) -> List[dict]:
        pass