from typing import Optional

from mlflow_mvc.service.run_service import RunService
from mlflow_mvc.config.core import Config

class RunController(object):
    """MLflow Run Controller Implementation"""
    
    def __init__(self, run_service = RunService(), tracking_uri: Optional[str] = None):
        if tracking_uri is not None:
            Config.set("TRACKING_SERVER_URI", tracking_uri)
        self._run_service = run_service
            
    def getBestRun(self, criteria: str, selected_metric: str, query: str):
        criteria = "700"
        selected_metric = "epoch"
        query = f"metrics.{selected_metric} > {criteria}"
        return self._run_service.getBestRun(criteria, selected_metric, query)
        
    