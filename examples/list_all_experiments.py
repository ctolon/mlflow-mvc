"""Example Script for initalize container and use Experiment Controller for list all experiments."""

from mlflow_mvc.containers.experiment_container import ExperimentContainer
from mlflow_mvc.config.core import Config

container = ExperimentContainer() # Initial Container
container.init_resources() # Init Resource
container.config.from_yaml(Config.BASE_CONFIG_DIR) # Config Settings (defaults to application_properties.yaml)
container.wire(modules=[__name__]) # Wire container Modules

controller = container.experiment_controller() # Controller instance from container
print(controller.list_all_experiments()) # Call one function from controller class
