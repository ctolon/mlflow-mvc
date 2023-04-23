"""Example for find run entity by id with just repository method."""

from mlflow_mvc.containers.run_container import RunContainer
from mlflow_mvc.config.core import Config

container = RunContainer()
container.init_resources()
container.config.from_yaml(Config.BASE_CONFIG_DIR)
container.wire(modules=[__name__])

# Repo instance
repo = container.run_repository()

# Harcoded run_id
run_id = "2fc1141d586e41f1ace034398ca99942"
run_data = repo.find_run_data_by_run_id(run_id)
print(run_data)
