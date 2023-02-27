"""Mlflow MVC Run Service Module"""

from pathlib import Path
from typing import Optional, List
from mlflow.entities import ViewType
from mlflow.entities.run import Run
from mlflow.store.entities import PagedList
from interface import implements
from dependency_injector.wiring import inject

from .interface.i_run_service import IRunService
from ..repository.experiment_repository import ExperimentRepository
from ..repository.run_repository import RunRepository
from ..entities.run_data_entity import RunDataEntity
from ..util.master_logger import MasterLogger

# Global logger settings
logger = MasterLogger().get_logger


class RunService(implements(IRunService)):
    """Mlflow MVC Run.data - Run.info Service Implementation"""

    @inject
    def __init__(
            self, run_repository: RunRepository, experiment_repository: ExperimentRepository
    ):
        self._run_repository = run_repository
        self._experiment_repository = experiment_repository

    def select_best_run_by_metric(
            self,
            runs: PagedList[Run],
            selected_metric: str
    ) -> Run:
        """Loop over runs and selects best run based on selected metric.

        Args:
            runs (PagedList[List]): Runs.
            selected_metric (str): Selected Metric.

        Returns:
            Run: Best Run Entity
        """
        accuracy_high = None
        best_run = None
        for run in runs:
            if selected_metric in run.data.metrics:
                if (accuracy_high is None or run.data.metrics[selected_metric] > accuracy_high):
                    accuracy_high = run.data.metrics[selected_metric]
                    best_run = run
            else:
                logger.warning(f"{selected_metric} not found for {run.info.run_id} skipped..")
        print('Highest Accuracy: ', accuracy_high)
        return best_run

    def get_best_run_by_all_experiments_and_selected_metric(
            self,
            selected_metric: str,
            query: Optional[str] = ""
    ) -> Run:
        """This function Searches all of Experiments and find all ML models then decides
        to best model based on selected metric criteria.

        Args:
            selected_metric (str): Metric.
            query (Optional[str], optional): Mlflow Query String for specialized search. Defaults to "".

        Raises:
            ValueError: If no Experiment Found.

        Returns:
            Run: Best Run Entity.
        """

        logger.info(Path(__file__).name + " execution start..")
        logger.info(self._experiment_repository.tracking_uri)

        # Parametrizing the right experiment path using widgets
        experiments = self._experiment_repository.find_all_experiments_as_paged_list()
        if experiments is None:
            logger.error("No experiment Found!")
            raise ValueError("Experiments returns as None type. No experience has recorded.")
        print(experiments)

        experiment_ids: List[str] = []
        for experiment in experiments:
            experiment_ids.append(experiment.experiment_id)
        print("Experiment IDs:", experiment_ids)

        # Setting the decision criteria for a best run
        runs = self._run_repository.search_runs(experiment_ids, query, ViewType.ALL)

        # Searching throught filtered runs to identify the best_run and build the model URI to programmatically reference later
        best_run = self.select_best_run_by_metric(runs, selected_metric)
        best_run_id = best_run.info.run_id
        print('Run ID: ', best_run_id)

        model_uri = "runs:/" + best_run_id + "/model"
        logger.info(model_uri)
        best_run_data_entity = RunDataEntity(best_run)
        # best_run_info_entity = RunInfoEntity(best_run)
        logger.info(f"Best Run Creation time in UTC: {best_run_data_entity.get_utc_time_created}")
        return best_run

    def get_best_run_by_experiment_name_and_selected_metric(
            self, experiment_name: str, selected_metric: str,
            query: Optional[str] = ""
    ) -> Run:
        """This function Searches run by experiment name and find all ML models then decides
        to best model based on selected metric criteria.

        Args:
            experiment_name (str): Mlflow Experiment Name.
            selected_metric (str): Metric.
            query (Optional[str], optional): Mlflow Query String for specialized search. Defaults to "".

        Raises:
            ValueError: If no Experiment Found.

        Returns:
            Run: Best Run Entity.
        """

        logger.info(Path(__file__).name + " execution start..")

        # Parametrizing the right experiment path using widgets
        experiment = self._run_repository.get_experiment_by_name(experiment_name)
        if experiment is None:
            logger.error(f"No experiment Found in name: {experiment_name}")
            raise ValueError("Experiment returns as None type. Check your experiment name.")
        print(experiment)

        experiment_ids = [experiment.experiment_id]
        print("Experiment ID:", experiment_ids)
        print("Experiment Name: ", experiment.name)

        # Setting the decision criteria for a best run
        runs = self._run_repository.search_runs(experiment_ids, query, ViewType.ALL)

        # Searching throught filtered runs to identify the best_run and build the model URI to programmatically reference later
        best_run = self.select_best_run_by_metric(runs, selected_metric)
        best_run_id = best_run.info.run_id
        print('Run ID: ', best_run_id)

        model_uri = "runs:/" + best_run_id + "/model"
        logger.info(model_uri)
        return best_run

    def get_best_run_by_experiment_id_and_selected_metric(
            self,
            experiment_id: str,
            selected_metric: str,
            query: Optional[str] = ""
    ) -> Run:
        """This function Searches run by experiment id and find all ML models then decides
        to best model based on selected metric criteria.

        Args:
            experiment_id (str): Mlflow Experiment id.
            selected_metric (str): Metric.
            query (Optional[str], optional): Mlflow Query String for specialized search. Defaults to "".

        Raises:
            ValueError: If no Experiment Found.

        Returns:
            Run: Best Run Entity.
        """

        logger.info(Path(__file__).name + " execution start..")

        # Parametrizing the right experiment path using widgets
        experiment = self._run_repository.get_experiment(experiment_id)
        if experiment is None:
            logger.error(f"No experiment Found in name: {experiment_id}")
            raise ValueError("Experiment returns as None type. Check your experiment name.")
        print(experiment)

        experiment_ids = [experiment.experiment_id]
        print("Experiment ID:", experiment_ids)
        print("Experiment Name: ", experiment.name)

        # Setting the decision criteria for a best run
        runs = self._run_repository.search_runs(experiment_ids, query, ViewType.ALL)

        # Searching throught filtered runs to identify the best_run and build the model URI to programmatically reference later
        best_run = self.select_best_run_by_metric(runs, selected_metric)
        best_run_id = best_run.info.run_id
        print('Run ID: ', best_run_id)

        model_uri = "runs:/" + best_run_id + "/model"
        logger.info(model_uri)
        return best_run

    def list_all_runs(self) -> List[dict]:
        """Get All Run Entities from Mlflow.

        Returns:
            List[dict]: All Run entities as a dict in List.
        """
        return self._run_repository.find_all_runs()
