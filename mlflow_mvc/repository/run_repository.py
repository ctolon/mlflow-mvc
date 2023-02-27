"Mlflow MVC Run Repository Module"

from typing import List
from dependency_injector.wiring import inject
import mlflow
from mlflow.entities.metric import Metric
from mlflow.entities.view_type import ViewType
from mlflow.tracking.client import MlflowClient

from ..entities.run_data_entity import RunDataEntity
from ..entities.run_info_entity import RunInfoEntity
from ..util.generic_transformers import generic_multi_transformer


class RunRepository(MlflowClient):
    """Mlflow MVC Repository for Run.Data - Run.info Entity"""

    @inject
    def __init__(self, tracking_server_url: str, *args, **kwargs):
        mlflow.tracking.set_tracking_uri(tracking_server_url)
        super().__init__()

    def find_run_data_by_run_id(self, run_id: str) -> RunDataEntity:
        run_data = self.get_run(run_id=run_id)
        return RunDataEntity(run_data)

    def find_run_info_by_run_id(self, run_id: str) -> RunInfoEntity:
        run_info = self.get_run(run_id=run_id)
        return RunInfoEntity(run_info)

    def find_metric_by_run_id_and_metric_name(self, run_id: str, metric_name: str) -> List[Metric]:
        return self.get_metric_history(run_id, metric_name)

    def find_all_runs(self) -> List[dict]:
        all_experiments = self.search_experiments(ViewType.ALL)
        all_experiment_ids = [x.experiment_id for x in all_experiments]
        all_runs = self.search_runs(experiment_ids=all_experiment_ids, run_view_type=ViewType.ALL)
        return generic_multi_transformer(all_runs)
