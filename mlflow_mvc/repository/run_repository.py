"Mlflow MVC Run Repository Module"

from typing import List
import mlflow
from mlflow.entities.metric import Metric
from mlflow.entities.run import Run
from mlflow.entities.view_type import ViewType
from mlflow.tracking.client import MlflowClient

from ..util.generic_transformers import generic_multi_transformer


class RunRepository(MlflowClient):
    """Mlflow MVC Repository for Run.Data - Run.info Entity"""

    def __init__(self, tracking_server_url: str, *args, **kwargs):
        mlflow.tracking.set_tracking_uri(tracking_server_url)
        super().__init__()

    def find_run_by_run_id(self, run_id: str) -> Run:
        return self.get_run(run_id=run_id)

    def find_metric_by_run_id_and_metric_name(self, run_id: str, metric_name: str) -> List[Metric]:
        return self.get_metric_history(run_id, metric_name)

    def find_all_runs(self) -> List[dict]:
        all_experiments = self.search_experiments(ViewType.ALL)
        all_experiment_ids = [x.experiment_id for x in all_experiments]
        all_runs = self.search_runs(experiment_ids=all_experiment_ids, run_view_type=ViewType.ALL)
        return generic_multi_transformer(all_runs)