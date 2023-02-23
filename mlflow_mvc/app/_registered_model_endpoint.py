"""Endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from ._fast_api_container import FastAPIContainer
from ..controller._registered_model_controller import RegisteredModelController
from ..util.exceptions import NotFoundError

router = APIRouter(prefix="/api/v1")

@router.get("/registered-models")
@inject
def get_list(
    registered_model_controller: RegisteredModelController = Depends(Provide[FastAPIContainer.registered_models_controller]),
):
    #return experiment_service.__name__
    return registered_model_controller.list_all_registered_models()

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