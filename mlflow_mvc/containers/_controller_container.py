from dependency_injector import containers, providers

from ._service_container import ExperimentServiceContainer, ModelVersionServiceContainer, \
    RegisteredModelServiceContainer, RunServiceContainer

from ..controller._experiment_controller import ExperimentController
from ..controller._model_version_controller import ModelVersionController
from ..controller._registered_model_controller import RegisteredModelController
from ..controller._run_controller import RunController


class ExperimentControllerContainer(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=["config.yml"])

    # Injection Service
    experiment_service = ExperimentServiceContainer().experiment_service

    experiment_controller = providers.Factory(
        ExperimentController,
        experiment_service=experiment_service
    )


class ModelVersionControllerContainer(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=["config.yml"])

    # Injection Service
    model_version_service = ModelVersionServiceContainer().model_version_service

    model_version_controller = providers.Factory(
        ModelVersionController,
        model_version_service=model_version_service
    )


class RegisteredModelControllerContainer(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=["config.yml"])

    # Injection Service
    registered_model_service = RegisteredModelServiceContainer().registered_model_service

    registered_model_controller = providers.Factory(
        RegisteredModelController,
        registered_model_service=registered_model_service
    )


class RunControllerContainer(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=["config.yml"])

    # Injection Service
    run_service = RunServiceContainer().run_service

    run_controller = providers.Factory(
        RunController,
        run_service=run_service
    )


class ControllersContainer(object):
    experiment_controller = ExperimentControllerContainer().experiment_controller
    model_version_controller = ModelVersionControllerContainer().model_version_controller
    registered_model_controller = RegisteredModelControllerContainer().registered_model_controller
    run_controller = RunControllerContainer().run_controller
