from dependency_injector import containers, providers

from ..repository.run_repository import RunRepository
from ..repository.experiment_repository import ExperimentRepository
from ..service.run_service import RunService
from ..controller.run_controller import RunController


class RunContainer(containers.DeclarativeContainer):

    config = providers.Configuration(yaml_files=["config.yml"])

    run_repository = providers.Singleton(
        RunRepository,
        tracking_server_url=config.tracking_server.url
    )

    experiment_repository = providers.Singleton(
        ExperimentRepository,
        tracking_server_url=config.tracking_server.url
    )

    run_service = providers.Factory(
        RunService,
        run_repository=run_repository,
        experiment_repository=experiment_repository,
    )

    run_controller = providers.Factory(
        RunController,
        run_service=run_service
    )
