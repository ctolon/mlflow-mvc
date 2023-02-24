"""Endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from .fast_api_container import FastAPIContainer

router = APIRouter(prefix="/api/v1")


@router.get("/registered-models")
@inject
def get_list(
        registered_model_ctrl=Depends(
            Provide[FastAPIContainer.registered_models_controller]),
):
    # return experiment_service.__name__
    return registered_model_ctrl.list_all_registered_models()


@router.get("/status")
@inject
def get_status():
    return {"status": "OK"}
