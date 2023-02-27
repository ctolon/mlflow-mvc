"""Endpoints module."""

from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from .fast_api_container import FastAPIContainer

router = APIRouter()


@router.get("/experiments")
@inject
def list_all_experiments(
        experiment_ctrl=Depends(Provide[FastAPIContainer.experiment_controller]),
):
    return experiment_ctrl.list_all_experiments()


@router.get("/status")
@inject
def get_status():
    return {"status": "OK"}
