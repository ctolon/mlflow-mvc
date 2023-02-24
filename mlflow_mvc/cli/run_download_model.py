"""CLI Script for download model by name, path and format"""
import argparse
from dependency_injector.wiring import inject, Provide
from mlflow_mvc.containers.controller_container import ModelVersionControllerContainer, ModelVersionController


@inject
def download_model(
        args,
        model_version_ctrl: ModelVersionController =
        Provide[ModelVersionControllerContainer.model_version_controller]
):
    model_version_ctrl.download_latest_model(
        model_name=args.model_name,
        model_path=args.model_path,
        model_format=args.model_format
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-name", "-n", help="Model name", type=str, required=True)
    parser.add_argument("--model-path", "-p", help="Model path", type=str, required=True)
    parser.add_argument("--model-format", "-f", help="Model format", type=str, default=".bin")
    args = parser.parse_args()
    container = ModelVersionControllerContainer()
    container.init_resources()
    container.wire(modules=[__name__])
    download_model(args=args)
