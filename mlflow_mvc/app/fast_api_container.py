"""FastAPI Container Module"""

from mlflow_mvc.containers.experiment_container import ExperimentContainer
from mlflow_mvc.containers.model_version_container import ModelVersionContainer
from mlflow_mvc.containers.registered_model_container import RegisteredModelContainer
from mlflow_mvc.containers.run_container import RunContainer
from dependency_injector import containers
import yaml


class FastAPIContainer(containers.DeclarativeContainer):
    # Main Config file
    CONFIG = "application_properties.yml"

    # Instance Container all we need
    experiment_cnt = ExperimentContainer()
    run_cnt = RunContainer()
    model_version_cnt = ModelVersionContainer()
    registered_model_cnt = RegisteredModelContainer()

    # Setup Config: Open Config file
    with open(CONFIG, "r") as f:
        new_config = yaml.safe_load(CONFIG)

    # Set Configs
    experiment_cnt.config.override(new_config)
    run_cnt.config.override(new_config)
    model_version_cnt.config.override(new_config)
    registered_model_cnt.config.override(new_config)

    # Controller Instance
    experiment_controller = experiment_cnt.experiment_controller
    run_controller = run_cnt.run_controller
    model_version_controller = model_version_cnt.model_version_controller
    registered_models_controller = registered_model_cnt.registered_model_controller

    # Endpoint path of modules
    MODULES = [
        ".experiment_endpoint",
        ".model_version_endpoint",
        ".run_endpoint",
        ".registered_model_endpoint"
    ]

    # Wiring Dependencies
    wiring_config = containers.WiringConfiguration(modules=MODULES)
