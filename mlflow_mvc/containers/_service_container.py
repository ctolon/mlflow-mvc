"""Service Container Module"""

from dependency_injector import containers, providers

from ._repository_container import ExperimentRepositoryContainer, ModelVersionRepositoryContainer, \
    RegisteredModelRepositoryContainer, RunRepositoryContainer

from ..service._experiment_service import ExperimentService
from ..service._model_version_service import ModelVersionService
from ..service._registered_model_service import RegisteredModelService
from ..service._run_service import RunService


class ExperimentServiceContainer(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=["config.yml"])

    # Injection Repo
    experiment_repository = ExperimentRepositoryContainer().experiment_repository

    experiment_service = providers.Factory(
        ExperimentService,
        experiment_repository=experiment_repository,
    )


class ModelVersionServiceContainer(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=["config.yml"])

    # Injection Repo
    model_version_repository = ModelVersionRepositoryContainer().model_version_repository
    run_repository = RunRepositoryContainer().run_repository

    model_version_service = providers.Factory(
        ModelVersionService,
        model_version_repository=model_version_repository,
        run_repository=run_repository
    )


class RegisteredModelServiceContainer(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=["config.yml"])

    # Injection Repo
    registered_models_repository = RegisteredModelRepositoryContainer().registered_models_repository

    registered_model_service = providers.Factory(
        RegisteredModelService,
        registered_models_repository=registered_models_repository,
    )


class RunServiceContainer(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=["config.yml"])

    # Injection Repo
    run_repository = RunRepositoryContainer().run_repository
    experiment_repository = ExperimentRepositoryContainer().experiment_repository

    run_service = providers.Factory(
        RunService,
        run_repository=run_repository,
        experiment_repository=experiment_repository,
    )


class ServicesContainer(object):
    experiment_service = ExperimentServiceContainer().experiment_service
    model_version_service = ModelVersionServiceContainer().model_version_service
    registered_model_service = RegisteredModelServiceContainer().registered_model_service
    run_service = RunServiceContainer().run_service
