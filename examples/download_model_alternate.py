"""Example Script for initalize container and use Experiment Controller for list all experiments."""

from mlflow_mvc.containers.model_version_container import ModelVersionContainer
from mlflow_mvc.config.core import Config

container = ModelVersionContainer() # Initial Container
container.init_resources() # Init Resource
container.config.from_yaml(Config.BASE_CONFIG_DIR) # Config Settings (defaults to application_properties.yaml)
container.wire(modules=[__name__]) # Wire container Modules

controller = container.model_version_controller() # Controller instance from container
controller.download_model_by_run_uuid("2fc1141d586e41f1ace034398ca99942", "fasttext_model_path")
