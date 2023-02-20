from typing import Optional

from mlflow_mvc.repository.experiment_repository import ExperimentRepository
from mlflow_mvc.util.master_logger import MasterLogger
from mlflow_mvc.config.core import Config

# Global logger settings
logger = MasterLogger().get_logger

class ExperimentService(object):
    """MLflow Experiment Service Implementation"""
    
    def __init__(
        self,
        experiment_repository = ExperimentRepository(),
        tracking_uri: Optional[str] = None
        ):
        if tracking_uri is not None:
            Config.set("TRACKING_SERVER_URI", tracking_uri)
            
        self._experiment_repository = experiment_repository
        
    def listAllExperiments(self):
        return self._experiment_repository.findAllExperiments()