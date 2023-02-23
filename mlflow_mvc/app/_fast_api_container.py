"""FastAPI Container Module"""


from dependency_injector import containers, providers
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mlflow_mvc.containers._controller_container import ControllersContainer



class FastAPIContainer(containers.DeclarativeContainer):
    
    container = ControllersContainer()
    
    experiment_controller = container.experiment_controller
    run_controller = container.run_controller
    model_version_controller = container.model_version_controller
    registered_models_controller = container.registered_model_controller
    
    # Endpoint path of modules
    MODULES = [
        "app._experiment_endpoint",
        "app._model_version_endpoint",
        "app._run_endpoint",
        "app._registered_model_endpoint"
        ]

    # Wiring Dependencies
    wiring_config = containers.WiringConfiguration(modules=MODULES)