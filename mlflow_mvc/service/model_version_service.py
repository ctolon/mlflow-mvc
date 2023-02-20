from mlflow.store.entities.paged_list import PagedList
from pathlib import Path
import pathlib
import requests
from typing import Optional

from mlflow_mvc.entities.run_data_entity import RunDataEntity
from mlflow_mvc.repository.run_repository import RunRepository
from mlflow_mvc.repository.model_version_repository import ModelVersionRepository
from mlflow_mvc.config.core import Config, ApiPath
from mlflow_mvc.util.master_logger import MasterLogger

# Global logger settings
logger = MasterLogger().get_logger

class ModelVersionService(object):
    """MLflow Model Version Service Implementation"""
    
    def __init__(
        self,
        run_repository = RunRepository(),
        model_version_repository = ModelVersionRepository(),
        tracking_uri: Optional[str] = None
        ):
        if tracking_uri is not None:
            Config.set("TRACKING_SERVER_URI", tracking_uri)
            
        self._run_repository = run_repository
        self._model_version_repository = model_version_repository

    def downloadLatestModel(self, model_name: str, model_path: str, model_format: str = ".bin"):
    
        logger.info(Path(__file__).name + " execution start..")

        # Fetch latest model
        logger.info("latest model is fetching now..")
        latest_model = self._model_version_repository.findLatestModelVersionByModelName(model_name)
        run_uuid = latest_model.run_id
        model_version = latest_model.version
        logger.info(f"Model run id : {run_uuid}")
        logger.info(f"Model version : {model_version}")
                    
        # Get Model Run by Run Id
        model = self._run_repository._client.get_run(run_id=run_uuid)
        run_data_model = RunDataEntity(model, model_path)

        # Get model path and uri with repository methods
        model_path = run_data_model.getModelPath 
        model_uri = run_data_model.getModelUri
        print(run_data_model.getFlavors)
        
        PATH_TO_DOWNLOAD = f"{model_uri}/{model_path}"
        logger.info(f"Path to download: {PATH_TO_DOWNLOAD}")
            
        OUTPUT_DIR = pathlib.Path(__file__).resolve().parent # Current path
        logger.info(f"Output Directory : {OUTPUT_DIR}")
        
        tracking_server_url = Config.get("TRACKING_SERVER_URI")
        
        BASE_URL = f"{tracking_server_url}{ApiPath.GET_ARTIFACT_PATH}" 
        
        
        # Send HTTP Params as JSON
        params = {
            "path": PATH_TO_DOWNLOAD,
            "run_uuid": run_uuid
        }
        
        logger.info(f"GET Request to -> {BASE_URL}?path={PATH_TO_DOWNLOAD}&run_uuid={run_uuid}, params: {params.items()}")
        
        # Send GET Request and retrieve model from MLflow Artifact server
        r = requests.get(url = BASE_URL, params=params)
        open(f'{model_name}{model_format}', 'wb').write(r.content)
        
        
    def latestModelValidator(self, model_name: str, criteria: str, selected_metric: str) -> bool:
        """Main Model validation function """

        logger.info(Path(__file__).name + " execution start..")

        # Fetch latest model
        latest_model = self._model_version_repository.findLatestModelVersionByModelName(model_name)
        
        # Log model properties
        logger.info(f"Registered Model Name: {latest_model.name}")
        logger.info(f"Registered Model Description: {latest_model.description}")
        logger.info(f"Registered Model Run id: {latest_model.run_id}")
        logger.info(f"Registered Model Creation Timestamp: {latest_model.creation_timestamp}")
        logger.info(f"Registered Model Version: {latest_model.version}")
        logger.info(f"Registered Model Tags: {latest_model.tags}")
        logger.info(f"Registered Model Stage: {latest_model.current_stage}")
        #logger.info(f"Registered Model Source: {latest_model.source}")

        # Get Model Metrics for latest run with transformers due to datatype issues
        model_metric: PagedList = self._run_repository._client.get_metric_history(latest_model.run_id, selected_metric)
        
        metric_dict = dict((x, y) for x, y in tuple(model_metric[0]))
        metric_key, metric_value = metric_dict["key"], metric_dict["value"]
        logger.info(f"Metric for latest run --> {metric_key} : {metric_value}")

        # Decision of model validation
        if metric_value < float(criteria):
            logger.error("Model Validation Failed!")
            logger.info("Execution finished")
            return False 
        logger.info("Model Validation Successful")
        logger.info("Execution finished")
        return True
        
    def listAllModelVersions(self):
        return self._model_version_repository.findAllModelVersions()