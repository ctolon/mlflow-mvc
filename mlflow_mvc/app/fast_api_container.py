"""FastAPI Container Module"""

from mlflow_mvc.containers.controller_container import ControllersContainer
from dependency_injector import containers, providers


class FastAPIContainer(containers.DeclarativeContainer):
    container = ControllersContainer()

    experiment_controller = container.experiment_controller
    run_controller = container.run_controller
    model_version_controller = container.model_version_controller
    registered_models_controller = container.registered_model_controller

    # Endpoint path of modules
    MODULES = [
        ".experiment_endpoint",
        ".model_version_endpoint",
        ".run_endpoint",
        ".registered_model_endpoint"
    ]

    # Wiring Dependencies
    wiring_config = containers.WiringConfiguration(modules=MODULES)
