"""CLI Script for model validation"""
import argparse
import yaml
from dependency_injector.wiring import inject, Provide
from mlflow_mvc.containers.model_version_container import ModelVersionContainer, ModelVersionController
from mlflow_mvc.config.core import Config


@inject
def latest_model_validation(
        args,
        model_version_ctrl: ModelVersionController =
        Provide[ModelVersionContainer.model_version_controller],
):
    model_version_ctrl.latest_model_validator(
        model_name=args.model_name,
        criteria=args.criteria,
        selected_metric=args.selected_metric
    )


if __name__ == '__main__':

    # CLI Options
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-name", "-mn", help="Model name", type=str, required=True)
    parser.add_argument("--criteria", "-cr", help="Metric criteria (ex: 700)", type=str, required=True)
    parser.add_argument("--selected-metric", "-sm", help="Selected Metric (ex: epoch)", type=str, required=True)
    parser.add_argument("--config", "-c", help="path and to config yaml file (ex. config.yml)", type=str)
    args = parser.parse_args()
    config_file = args.config

    # Init container
    container = ModelVersionContainer()
    container.init_resources()
    container.config.from_yaml(Config.BASE_CONFIG_DIR)
    container.wire(modules=[__name__])

    # Open new config file
    if args.config:
        with open(config_file, "r") as f:
            new_config = yaml.safe_load(f)
        container.config.override(new_config)
        print(f"New Config: {new_config}")

    print(container.config())
    # Call main function
    latest_model_validation(args=args)
