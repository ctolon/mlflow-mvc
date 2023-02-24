"""Mlflow MVC Model Version Service Module"""

import pathlib
from pathlib import Path
from typing import List
import requests
from mlflow.store.entities.paged_list import PagedList
from mlflow.entities.metric import Metric
from interface import implements
from dependency_injector.wiring import inject

from .interface.i_model_version_service import IModelVersionService
from ..config.core import Config, ApiPath
from ..entities.run_data_entity import RunDataEntity
from ..repository.model_version_repository import ModelVersionRepository
from ..repository.run_repository import RunRepository
from ..util.master_logger import MasterLogger

# Global logger settings
logger = MasterLogger().get_logger


class ModelVersionService(implements(IModelVersionService)):
    """Mlflow MVC Model Version Service Implementation"""

    @inject
    def __init__(self, run_repository: RunRepository, model_version_repository: ModelVersionRepository):
        self._run_repository = run_repository
        self._model_version_repository = model_version_repository

    def download_latest_model(self, model_name: str, model_path: str, model_format: str = ".bin"):
        """Download Latest Model from Mlflow Artifact Server.

        Args:
            model_name (str): Model Name.
            model_path (str): Model Path as a Key.
            model_format (str, optional): Model format. Defaults to ".bin".
        """

        if model_format.startswith(".") is False:
            raise TypeError("Model Format parameter must be started with .")

        logger.info(Path(__file__).name + " execution start..")

        # Fetch latest model
        logger.info("latest model is fetching now..")
        latest_model_version = self._model_version_repository.find_latest_model_version_by_model_name(
            model_name)
        run_uuid = latest_model_version.run_id
        model_version = latest_model_version.version
        logger.info(f"Model run id : {run_uuid}")
        logger.info(f"Model version : {model_version}")

        # Get Model Run by Run Id
        model = self._run_repository.get_run(run_id=run_uuid)
        run_data_model = RunDataEntity(model, model_path, strict_return=True)

        # Get model path and uri with repository methods
        model_path = run_data_model.get_model_path
        model_uri = run_data_model.get_model_uri
        print(run_data_model.get_flavors)

        path_to_download = f"{model_uri}/{model_path}"
        logger.info(f"Path to download: {path_to_download}")

        output_dir = pathlib.Path(__file__).resolve().parent  # Current path
        logger.info(f"Output Directory : {output_dir}")

        tracking_server_url = Config.get("TRACKING_SERVER_URI")

        base_url = f"{tracking_server_url}{ApiPath.GET_ARTIFACT_PATH}"

        # Send HTTP Params as JSON
        params = {
            "path": path_to_download,
            "run_uuid": run_uuid
        }

        logger.info(
            f"GET Request to -> {base_url}?path={path_to_download}&run_uuid={run_uuid}, params: {params.items()}")

        # Send GET Request and retrieve model from MLflow Artifact server
        r = requests.get(url=base_url, params=params)
        open(f'{model_name}{model_format}', 'wb').write(r.content)

        logger.info(f"{model_name} download success!")

    def latest_model_validator(self, model_name: str, criteria: str, selected_metric: str) -> bool:
        """Fetch Latest model and validate based on selected metric criteria. 

        Args:
            model_name (str): Name of model.
            criteria (str): Metric Criteria.
            selected_metric (str): Name of metric.

        Returns:
            bool: True if model validation success else False.
        """

        logger.info(Path(__file__).name + " execution start..")

        # Fetch latest model
        latest_model_version = self._model_version_repository.find_latest_model_version_by_model_name(model_name)

        # Log model properties
        logger.info(f"Registered Model Name: {latest_model_version.name}")
        logger.info(f"Registered Model Description: {latest_model_version.description}")
        logger.info(f"Registered Model Run id: {latest_model_version.run_id}")
        logger.info(f"Registered Model Creation Timestamp: {latest_model_version.creation_timestamp}")
        logger.info(f"Registered Model Version: {latest_model_version.version}")
        logger.info(f"Registered Model Tags: {latest_model_version.tags}")
        logger.info(f"Registered Model Stage: {latest_model_version.current_stage}")
        # logger.info(f"Registered Model Source: {latest_model_version.source}")

        # Get Model Metrics for latest run with transformers due to datatype issues
        model_metric: List[Metric] = self._run_repository.get_metric_history(latest_model_version.run_id,
                                                                             selected_metric)

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

    def list_all_model_versions(self) -> List[dict]:
        """Get All Model version Entities from Mlflow.

        Returns:
            List[dict]: All Model Version entities as a dict in List.
        """

        return self._model_version_repository.find_all_model_versions()
