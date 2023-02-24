"""Mlflow MVC Experiment Controller Module"""

from dependency_injector.wiring import inject, Provide
from typing import List

from ..service._experiment_service import ExperimentService


class ExperimentController(object):
    """Mlflow MVC Experiment Controller Implementation"""

    def __init__(self, experiment_service: ExperimentService):
        self._experiment_service = experiment_service

    def list_all_experiments(self) -> List[dict]:
        return self._experiment_service.list_all_experiments()
