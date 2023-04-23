"""Example Script for using service with container."""

from mlflow_mvc.containers.model_version_container import ModelVersionContainer
from mlflow_mvc.config.core import Config

container = ModelVersionContainer()
container.init_resources()
container.config.from_yaml(Config.BASE_CONFIG_DIR)
container.wire(modules=[__name__])

# Service initial
service = container.model_version_service()
a = service.latest_model_validator("skbc", "800", "epoch")
print(a)
