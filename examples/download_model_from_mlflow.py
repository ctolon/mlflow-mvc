"""Example CLI Script preparation with DI for latest download model."""
import argparse
import yaml
from dependency_injector.wiring import inject, Provide
import os

from mlflow_mvc.containers.model_version_container import ModelVersionContainer, ModelVersionController
from mlflow_mvc.config.core import Config


@inject
def download_model(
        args,
        model_version_ctrl: ModelVersionController =
        Provide[ModelVersionContainer.model_version_controller]
):
    model_version_ctrl.download_latest_model(
        model_name=args.model_name,
        model_path=args.model_path,
        output_dir=args.output_dir,
        model_format=args.model_format
    )


if __name__ == '__main__':

    # CLI Options
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-name", "-n", help="Model name", type=str, required=True)
    parser.add_argument("--model-path", "-p", help="Model path", type=str, required=True)
    parser.add_argument("--model-format", "-f", help="Model format", type=str, default=".bin")
    parser.add_argument("--output-dir", "-o", help="Output directory", type=str, default=os.getcwd())
    parser.add_argument("--config", "-c", help="path and to config yaml file (ex. config.yml)", type=str)
    args = parser.parse_args()
    config_file = args.config

    # Container Instance
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

    # Call Main Function
    download_model(args=args)
