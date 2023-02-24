"""Endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide
from pydantic import BaseModel
from typing import Optional

from ._fast_api_container import FastAPIContainer
from ..entities._model_version_entity import ModelVersionEntity
from ..controller._model_version_controller import ModelVersionController
from ..util.exceptions import NotFoundError

router = APIRouter()


class DownloadLatestModelBody(BaseModel):
    model_name: str
    model_path: str
    model_format: Optional[str]


@router.get("/model-versions")
@inject
def list_all_registered_models(
        model_version_controller: ModelVersionController = Depends(Provide[FastAPIContainer.model_version_controller]),
):
    return model_version_controller.list_all_model_versions()


@router.post("/model-versions/download-latest-model")
@inject
def download_latest_model(
        body: DownloadLatestModelBody,
        model_version_controller: ModelVersionController = Depends(Provide[FastAPIContainer.model_version_controller]),
):
    return model_version_controller.download_latest_model(
        model_name=body.model_name,
        model_path=body.model_path,
        model_format=body.model_format
    )


@router.get("/status")
@inject
def get_status():
    return {"status": "OK"}


"""
@router.get("/experiments")
@inject
def get_list(
        experiment_service: ExperimentService2 = Depends(Provide[Container.experiment_service]),
):
    return experiment_service.get_users()


@router.get("/experiments/{experiment_id}")
@inject
def get_by_id(
        experiment_id: int,
        experiment_service: ExperimentService2 = Depends(Provide[Container.experiment_service]),
):
    try:
        return experiment_service.get_experiment_by_id(experiment_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/experiments", status_code=status.HTTP_201_CREATED)
@inject
def add(
        experiment_service: ExperimentService2 = Depends(Provide[Container.experiment_service]),
):
    return experiment_service.create_user()


@router.delete("/experiments/{experiment_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def remove(
        experiment_id: int,
        experiment_service: ExperimentService2 = Depends(Provide[Container.experiment_service]),
):
    try:
        experiment_service.delete_experiment_by_id(experiment_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
"""
