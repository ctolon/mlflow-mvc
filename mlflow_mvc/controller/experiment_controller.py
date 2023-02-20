from typing import Optional

from mlflow_mvc.service.experiment_service import ExperimentService
from mlflow_mvc.config.core import Config

class ExperimentController(object):
    """MLflow Experiment Controller Implementation"""
    
    def __init__(self, experiment_service = ExperimentService(), tracking_uri: Optional[str] = None):
        if tracking_uri is not None:
            Config.set("TRACKING_SERVER_URI", tracking_uri)
        self._experiment_service = experiment_service
        
    