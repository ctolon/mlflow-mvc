"""Mlflow MVC Run Service Interface"""

from interface import implements, Interface
from typing import List, Optional
from mlflow.entities.run import Run


class IRunService(Interface):
    """Mlflow MVC Run Service Interface Class"""

    def get_best_run_by_all_experiments_and_selected_metric(
        self,
        selected_metric: str,
        query: Optional[str] = ""
        ) -> Run:
        pass
    def get_best_run_by_experiment_name_and_selected_metric(
        self, experiment_name: str,
        selected_metric: str,
        query: Optional[str] = ""
        ) -> Run:
        pass
    def get_best_run_by_experiment_id_and_selected_metric(
        self, experiment_id: str,
        selected_metric: str,
        query: Optional[str] = ""
        ) -> Run:
        pass
    def list_all_runs(self) -> List[dict]:
        pass