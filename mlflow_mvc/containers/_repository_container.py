"""Repository Container Module"""

from dependency_injector import containers, providers

from ..repository._experiment_repository import ExperimentRepository
from ..repository._model_version_repository import ModelVersionRepository
from ..repository._registered_model_repository import RegisteredModelRepository
from ..repository._run_repository import RunRepository


class ExperimentRepositoryContainer(containers.DeclarativeContainer):
    # Injection Config
    config = providers.Configuration(yaml_files=["config.yml"])

    experiment_repository = providers.Singleton(
        ExperimentRepository,
        tracking_server_url=config.tracking_server.url
    )


class ModelVersionRepositoryContainer(containers.DeclarativeContainer):
    # Injection Config
    config = providers.Configuration(yaml_files=["config.yml"])

    model_version_repository = providers.Singleton(
        ModelVersionRepository,
        tracking_server_url=config.tracking_server.url
    )


class RegisteredModelRepositoryContainer(containers.DeclarativeContainer):
    # Injection Config
    config = providers.Configuration(yaml_files=["config.yml"])

    registered_models_repository = providers.Singleton(
        RegisteredModelRepository,
        tracking_server_url=config.tracking_server.url
    )


class RunRepositoryContainer(containers.DeclarativeContainer):
    # Injection Config
    config = providers.Configuration(yaml_files=["config.yml"])

    run_repository = providers.Singleton(
        RunRepository,
        tracking_server_url=config.tracking_server.url
    )


class RepositoriesContainer(object):
    experiment_repository = ExperimentRepositoryContainer().experiment_repository
    model_version_repository = ModelVersionRepositoryContainer().model_version_repository
    registered_model_repository = RegisteredModelRepositoryContainer().registered_models_repository
    run_repository = RunRepositoryContainer().run_repository
