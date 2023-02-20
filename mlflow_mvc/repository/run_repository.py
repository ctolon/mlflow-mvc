import mlflow
from mlflow.tracking.client import MlflowClient
from mlflow.entities.run import Run
from mlflow.entities.view_type import ViewType
from mlflow.entities.metric import Metric
from typing import List, Optional

from mlflow_mvc.config.core import Config
from mlflow_mvc.util.generic_transformers import genericMultiTransformer

mlflow.set_tracking_uri(Config.get("TRACKING_SERVER_URI"))

class RunRepository(object):
    """MLflow Repository for Run.Data - Run.info Entity"""
    
    def __init__(self, client: MlflowClient = MlflowClient(), tracking_uri: str = None):
        if tracking_uri is not None:
            del client
            Config.set("TRACKING_SERVER_URI", tracking_uri)
            client = MlflowClient(tracking_uri=Config.get("TRACKING_SERVER_URI"))
        self._client = client
            
    def findRunByRunId(self, run_id: str) -> Run:
        return self._client.get_run(run_id=run_id)
    
    def findModelMetricByRunIdAndMetric(self, run_id: str, metric_name: str) -> List[Metric]:
        return self._client.get_metric_history(run_id, metric_name)
    
    ######### Fix İt!!!
    def findAllRuns(self) -> List[dict]:
        all_experiments = self._client.search_experiments(ViewType.ALL)
        #all_runs = self._client.search_runs(experiment_ids, ViewType.ALL)
        return genericMultiTransformer(all_experiments)
    