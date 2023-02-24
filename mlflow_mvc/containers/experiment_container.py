from dependency_injector import containers, providers

from ..repository.experiment_repository import ExperimentRepository
from ..service.experiment_service import ExperimentService
from ..controller.experiment_controller import ExperimentController
from ..config.core import Config


class ExperimentContainer(containers.DeclarativeContainer):
    config = providers.Configuration(Config.BASE_CONFIG_DIR)

    experiment_repository = providers.Singleton(
        ExperimentRepository,
        tracking_server_url=config.tracking_server.url
    )

    experiment_service = providers.Factory(
        ExperimentService,
        experiment_repository=experiment_repository,
    )

    experiment_controller = providers.Factory(
        ExperimentController,
        experiment_service=experiment_service
    )
