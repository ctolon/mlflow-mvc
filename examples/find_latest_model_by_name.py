"""Example script for find latest model by name with repository methods."""

from mlflow_mvc.containers.model_version_container import ModelVersionContainer
from mlflow_mvc.config.core import Config

# Container settings
container = ModelVersionContainer()
container.init_resources()
container.config.from_yaml(Config.BASE_CONFIG_DIR)
container.wire(modules=[__name__])

# Repo instance
repo = container.model_version_repository()

latest_model = repo.find_latest_model_version_by_model_name("skbc")
print(latest_model)
