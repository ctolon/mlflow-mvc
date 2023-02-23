"""Mlflow MVC Experiment Service Module"""

from typing import Optional, List
from interface import implements

from .interface._i_experiment_service import IExperimentService
from ..repository._experiment_repository import ExperimentRepository
from ..util.master_logger import MasterLogger
from ..util.performance_analyze import timeit

# Global logger settings
logger = MasterLogger().get_logger


class ExperimentService(implements(IExperimentService)):
    """Mlflow MVC Experiment Service Implementation"""

    def __init__(self, experiment_repository: ExperimentRepository):
        self._experiment_repository = experiment_repository

    def list_all_experiments(self) -> List[dict]:
        """Get All Experiment Entities from Mlflow.

        Returns:
            List[dict]: All Experiments entities as a dict in List.
        """
        return self._experiment_repository.find_all_experiments()
