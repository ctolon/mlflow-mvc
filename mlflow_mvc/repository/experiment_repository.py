"Mlflow MVC Experiment Repository Module"

from typing import List
from dependency_injector.wiring import inject
import mlflow
from mlflow.entities.experiment import Experiment
from mlflow.entities.view_type import ViewType
from mlflow.store.entities import PagedList
from mlflow.tracking.client import MlflowClient

from ..util.generic_transformers import generic_multi_transformer
from ..entities.experiment_entity import ExperimentEntity


class ExperimentRepository(MlflowClient):
    """Mlflow MVC Repository for Experiment Entity"""

    @inject
    def __init__(self, tracking_server_url: str, *args, **kwargs):
        mlflow.tracking.set_tracking_uri(tracking_server_url)
        super().__init__()

    def find_all_experiments_as_paged_list(self) -> PagedList[Experiment]:
        return self.search_experiments(ViewType.ALL)

    def find_all_experiments(self) -> List[dict]:
        all_experiments = self.find_all_experiments_as_paged_list()
        return generic_multi_transformer(all_experiments)

    def find_all_experiment_ids(self) -> List[str]:
        all_experiments = self.find_all_experiments_as_paged_list()
        all_experiment_ids = [x.experiment_id for x in all_experiments]
        return all_experiment_ids

    def find_all_experiment_names(self) -> List[str]:
        all_experiments = self.find_all_experiments_as_paged_list()
        all_experiment_names = [x.name for x in all_experiments]
        return all_experiment_names

    def find_experiment_by_id(self, experiment_id: str) -> ExperimentEntity:
        experiment_by_id = self.get_experiment(experiment_id)
        return ExperimentEntity(experiment_by_id)

    def find_experiment_by_name(self, name: str) -> ExperimentEntity:
        experiment_by_name = self.get_experiment_by_name(name=name)
        return ExperimentEntity(experiment_by_name)
