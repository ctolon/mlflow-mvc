from dependency_injector import containers, providers

from ..repository.registered_model_repository import RegisteredModelRepository
from ..service.registered_model_service import RegisteredModelService
from ..controller.registered_model_controller import RegisteredModelController


class RegisteredModelContainer(containers.DeclarativeContainer):

    config = providers.Configuration(yaml_files=["config.yml"])

    registered_models_repository = providers.Singleton(
        RegisteredModelRepository,
        tracking_server_url=config.tracking_server.url
    )

    registered_model_service = providers.Factory(
        RegisteredModelService,
        registered_models_repository=registered_models_repository,
    )

    registered_model_controller = providers.Factory(
        RegisteredModelController,
        registered_model_service=registered_model_service
    )
