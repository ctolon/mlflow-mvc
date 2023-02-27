"""Mlflow MVC Run Controller Module"""

from typing import Optional
from dependency_injector.wiring import inject

from ..service.run_service import RunService


class RunController(object):
    """Mlflow MVC Run Controller Implementation"""

    @inject
    def __init__(self, run_service: RunService):
        self._run_service = run_service

    def get_best_run_by_experiment_name_and_selected_metric(
            self,
            experiment_name: str,
            selected_metric: str,
            query: Optional[str] = ""
    ):
        return self._run_service.get_best_run_by_experiment_name_and_selected_metric(
            experiment_name,
            selected_metric,
            query
        )

    def get_best_run_by_experiment_id_and_selected_metric(
            self,
            experiment_id: str,
            selected_metric: str,
            query: Optional[str] = ""
    ):
        return self._run_service.get_best_run_by_experiment_id_and_selected_metric(
            experiment_id,
            selected_metric,
            query
        )

    def get_best_run_by_all_experiments_and_selected_metric(
            self,
            selected_metric: str,
            query: Optional[str] = "",
    ):
        return self._run_service.get_best_run_by_all_experiments_and_selected_metric(
            selected_metric,
            query
        )
