from dependency_injector import containers, providers

from ..repository.run_repository import RunRepository
from ..repository.model_version_repository import ModelVersionRepository
from ..service.model_version_service import ModelVersionService
from ..controller.model_version_controller import ModelVersionController
from ..config.core import Config


class ModelVersionContainer(containers.DeclarativeContainer):
    config = providers.Configuration(Config.BASE_CONFIG_DIR)

    model_version_repository = providers.Singleton(
        ModelVersionRepository,
        tracking_server_url=config.tracking_server.url
    )

    run_repository = providers.Singleton(
        RunRepository,
        tracking_server_url=config.tracking_server.url
    )

    model_version_service = providers.Factory(
        ModelVersionService,
        model_version_repository=model_version_repository,
        run_repository=run_repository
    )

    model_version_controller = providers.Factory(
        ModelVersionController,
        model_version_service=model_version_service
    )
