import mlflow
from mlflow.entities import ViewType
from pathlib import Path
from typing import Optional

from mlflow_mvc.repository.run_repository import RunRepository
from mlflow_mvc.config.core import Config
from mlflow_mvc.util.master_logger import MasterLogger

# Global logger settings
logger = MasterLogger().get_logger

class RunService(object):
    """MLflow Run.data - Run.info Service Implementation"""
    
    def __init__(
        self,
        run_repository = RunRepository(),
        tracking_uri: Optional[str] = None
        ):
        if tracking_uri is not None:
            Config.set("TRACKING_SERVER_URI", tracking_uri)
            
        self._run_repository = run_repository
        
    def getBestRun(self, criteria: str, selected_metric: str, query: str):
        
        logger.info(Path(__file__).name + " execution start..")

        # Parametrizing the right experiment path using widgets
        experiment_name = Config.EXPERIMENT_NAME
        experiment = self._run_repository._client.get_experiment_by_name(experiment_name)
        print(experiment)

        experiment_ids = [experiment.experiment_id]
        print("Experiment IDs:", experiment_ids)

        # Setting the decision criteria for a best run
        runs = self._run_repository._client.search_runs(experiment_ids, query, ViewType.ALL)

        # Searching throught filtered runs to identify the best_run and build the model URI to programmatically reference later
        accuracy_high = None
        best_run = None
        for run in runs:
            if (accuracy_high == None or run.data.metrics[selected_metric] > accuracy_high):
                accuracy_high = run.data.metrics[selected_metric]
                best_run = run
        run_id = best_run.info.run_id
        print('Highest Accuracy: ', accuracy_high)
        print('Run ID: ', run_id)

        model_uri = "runs:/" + run_id + "/model"
        logger.info(model_uri)
    
    def listAllRuns(self):
        return self._run_repository.findAllRuns()