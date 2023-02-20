import mlflow
from mlflow.tracking.client import MlflowClient
from mlflow.entities.experiment import Experiment
from mlflow.entities.view_type import ViewType
from typing import Optional, List

from mlflow_mvc.config.core import Config
from mlflow_mvc.util.generic_transformers import genericMultiTransformer

mlflow.set_tracking_uri(Config.get("TRACKING_SERVER_URI"))

class ExperimentRepository(object):
    """MLflow Repository for Experiment Entity"""
    
    def __init__(self, client: MlflowClient = MlflowClient(), tracking_uri: Optional[str] = None):
        if tracking_uri is not None:
            del client
            Config.set("TRACKING_SERVER_URI", tracking_uri)
            client = MlflowClient(tracking_uri=Config.get("TRACKING_SERVER_URI"))
        self._client = client
            
    def findExperimentByName(self, experiment_name: str) -> Optional[Experiment]:
        return mlflow.get_experiment_by_name(experiment_name).experiment_id
            
    def findExperimentByExperimentId(self, experiment_id: str) -> Experiment:
        return self._client.get_experiment(experiment_id)
        
    def findAllExperiments(self) -> List[dict]:
        all_experiments = self._client.search_experiments(ViewType.ALL)
        return genericMultiTransformer(all_experiments)