"""Mlflow MVC Model Version Service Module"""

import pathlib
from pathlib import Path
import os
from typing import List, Union
import requests
from mlflow.entities.metric import Metric
from interface import implements
from dependency_injector.wiring import inject

from .interface.i_model_version_service import IModelVersionService
from ..config.core import ApiPath
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

    def _pathdir_creator(self, output_dir: str) -> Union[str, Path]:
        """This function allows to create directory if not exist.

        Args:
            output_dir (str): Path to output directory. If not current path, it will automatically convert to 'Path'

        Returns:
            Path | str: Abs path of directory.
        """
        # Create output_dir if not exist
        if output_dir != os.getcwd():
            pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)
            output_dir: Path = pathlib.Path(output_dir)
            logger.info(output_dir.resolve())
        else:
            logger.info(f"Output Directory : {output_dir}")
        return output_dir

    def _retrive_model_path_and_uri(self, run_data_entity: RunDataEntity, model_path_name: str):
        """Retrive model path and uri by path name.

        Args:
            run_data_entity (RunDataEntity): RunDataEntity
            path_name (str): model path name (ex. fasttext_model_path)

        Returns:
            str, str: model path and model URI as string.
        """
        model_path: str = run_data_entity.get_artifacts.get(model_path_name).get("path")
        model_uri: str = run_data_entity.get_artifacts.get(model_path_name).get("uri")

        return model_path, model_uri

    def download_latest_model(
            self, model_name: str, model_path_name: str, output_dir: str = os.getcwd(), model_format: str = ".bin"
            ):
        """Download Latest Model from Mlflow Artifact Server.

        Args:
            model_name (str): Model Name.
            model_path (str): Model Path as a Key.
            output_dir (str): Output directory for save model.
            model_format (str, optional): Model format. Defaults to ".bin".
        """

        if model_format.startswith(".") is False:
            raise TypeError("Model Format parameter must be started with .")

        logger.info(Path(__file__).name + " execution start..")

        # Fetch latest model
        logger.info("latest model is fetching now..")
        latest_model_version = self._model_version_repository.find_latest_model_version_by_model_name(
            model_name)
        run_uuid = latest_model_version.get_run_id
        model_version = latest_model_version.get_version
        logger.info(f"Model run id : {run_uuid}")
        logger.info(f"Model version : {model_version}")

        # Get Model Run by Run Id
        run_data_model = self._run_repository.find_run_data_by_run_id(run_id=run_uuid)

        # Get model path and uri with repository methods
        model_path, model_uri = self._retrive_model_path_and_uri(run_data_model, model_path_name)
        print(run_data_model.get_flavors)

        path_to_download = f"{model_uri}/{model_path}"
        logger.info(f"Path to download: {path_to_download}")

        # Get tracking server URI from Generic CRUD repository
        tracking_server_url = self._model_version_repository.tracking_uri

        # Base URL With GET_ARTIFACT Endpoint
        base_url = f"{tracking_server_url}{ApiPath.GET_ARTIFACT}"
        
        # Create output_dir if not exist
        output_dir = self._pathdir_creator(output_dir)
        # Send HTTP Params as JSON
        params = {
            "path": path_to_download,
            "run_uuid": run_uuid
        }

        logger.info(
            f"GET Request to -> {base_url}?path={path_to_download}&run_uuid={run_uuid}, params: {params.items()}")

        # Send GET Request and retrieve model from MLflow Artifact server
        r = requests.get(url=base_url, params=params)
        open(f'{output_dir}/{model_name}{model_format}', 'wb').write(r.content)

        logger.info(f"{model_name} download success!")
        
    def download_model_by_run_uuid(
            self, run_uuid: str, model_path_name: str, output_dir: Union[str, Path] = os.getcwd()
            ):
        """Download Model by run id from Mlflow Artifact Server.

        Args:
            run_uuid (str): Run uuid of model.
            model_path (str): Model Path as a Key.
            output_dir (str): Output directory for save model.
        """

        logger.info(Path(__file__).name + " execution start..")

        # Get Model Run by Run Id
        run_data_model = self._run_repository.find_run_data_by_run_id(run_id=run_uuid)
        
        # Get model path and uri with repository methods
        model_path, model_uri = self._retrive_model_path_and_uri(run_data_model, model_path_name)
        print(run_data_model.get_flavors)
        
        # Retrieve model name and format
        model_name_with_format = model_path.split("/")[-1]
        model_name = model_name_with_format.split(".")[0]
        model_format = f".{model_name_with_format.split('.')[1]}"
        logger.info(f"Model Name: {model_name}")
        logger.info(f"Model Format: {model_format}")
        
        if model_format.startswith(".") is False:
            raise TypeError("Model Format parameter must be started with .")

        path_to_download = f"{model_uri}/{model_path}"
        logger.info(f"Path to download: {path_to_download}")

        # Get tracking server URI from Generic CRUD repository
        tracking_server_url = self._model_version_repository.tracking_uri

        # Base URL With GET_ARTIFACT Endpoint
        base_url = f"{tracking_server_url}{ApiPath.GET_ARTIFACT}"
        
        # Create output_dir if not exist
        output_dir = self._pathdir_creator(output_dir)
        # Send HTTP Params as JSON
        params = {
            "path": path_to_download,
            "run_uuid": run_uuid
        }

        logger.info(
            f"GET Request to -> {base_url}?path={path_to_download}&run_uuid={run_uuid}, params: {params.items()}")

        # Send GET Request and retrieve model from MLflow Artifact server
        r = requests.get(url=base_url, params=params)
        open(f'{output_dir}/{model_name}{model_format}', 'wb').write(r.content)

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
        logger.info(f"Registered Model Name: {latest_model_version.get_name}")
        logger.info(f"Registered Model Description: {latest_model_version.get_description}")
        logger.info(f"Registered Model Run id: {latest_model_version.get_run_id}")
        logger.info(f"Registered Model Creation Timestamp: {latest_model_version.get_creation_timestamp}")
        logger.info(f"Registered Model Version: {latest_model_version.get_version}")
        logger.info(f"Registered Model Tags: {latest_model_version.get_tags}")
        logger.info(f"Registered Model Stage: {latest_model_version.get_current_stage}")
        # logger.info(f"Registered Model Source: {latest_model_version.source}")

        # Get Model Metrics for latest run with transformers due to datatype issues
        model_metric: List[Metric] = self._run_repository.get_metric_history(latest_model_version.get_run_id,
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
