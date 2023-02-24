"""Endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from ._fast_api_container import FastAPIContainer
from app.controller._experiment_controller import ExperimentController
from ..util.exceptions import NotFoundError

router = APIRouter()


@router.get("/experiments")
@inject
def list_all_experiments(
        experiment_controller: ExperimentController = Depends(Provide[FastAPIContainer.experiment_controller]),
):
    return experiment_controller.list_all_experiments()


@router.get("/status")
@inject
def get_status():
    return {"status": "OK"}
