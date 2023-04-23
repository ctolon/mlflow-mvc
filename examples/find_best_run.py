"""Example Script for Using Any Service for create web based controller with Dependency Injection implementation (find best run)."""

from dependency_injector.wiring import Provide
from mlflow_mvc.service.run_service import RunService
from mlflow_mvc.containers.run_container import RunContainer
from mlflow_mvc.config.core import Config


def find_best_run(run_service: RunService = (Provide[RunContainer.run_service])):
    run = run_service.get_best_run_by_all_experiments_and_selected_metric("epoch")
    print(run)
    

if __name__ == "__main__":
    
    # Container settings
    container = RunContainer()
    container.init_resources()
    container.config.from_yaml(Config.BASE_CONFIG_DIR)
    container.wire(modules=[__name__])
    
    # call function
    find_best_run()

                    
