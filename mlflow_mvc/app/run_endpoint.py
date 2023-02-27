"""Endpoints module."""

from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from .fast_api_container import FastAPIContainer

router = APIRouter(prefix="/api/v1")


@router.get("/runs")
@inject
def get_list(
        run_ctrl=Depends(Provide[FastAPIContainer.run_controller]),
):
    return run_ctrl.list_all_runs()


@router.get("/status")
def get_status():
    return {"status": "OK"}
