"""Endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from ._fast_api_container import FastAPIContainer
from ..service._run_service import RunService
from ..util.exceptions import NotFoundError

router = APIRouter(prefix="/api/v1")


@router.get("/runs")
@inject
def get_list(
        run_service: RunService = Depends(Provide[FastAPIContainer.run_controller]),
):
    # return experiment_service.__name__
    return run_service.list_all_runs()


@router.get("/status")
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
