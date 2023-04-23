"""Endpoints module."""

from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from pydantic import BaseModel
from typing import Optional

from .fast_api_container import FastAPIContainer

router = APIRouter()


class DownloadLatestModelBody(BaseModel):
    model_name: str
    model_path: str
    model_format: Optional[str]


@router.get("/model-versions")
@inject
def list_all_registered_models(
        model_version_controller=Depends(Provide[FastAPIContainer.model_version_controller]),
):
    return model_version_controller.list_all_model_versions()


@router.post("/model-versions/download-latest-model")
@inject
def download_latest_model(
        body: DownloadLatestModelBody,
        model_version_ctrl=Depends(Provide[FastAPIContainer.model_version_controller]),
):
    return model_version_ctrl.download_latest_model(
        model_name=body.model_name,
        model_path=body.model_path,
        model_format=body.model_format
    )
    
@router.post("/model-versions/download-by-run-uuid")
@inject
def download_latest_model(
        body: DownloadLatestModelBody,
        model_version_ctrl=Depends(Provide[FastAPIContainer.model_version_controller]),
):
    return model_version_ctrl.download_latest_model(
        model_name=body.model_name,
        model_path=body.model_path,
        model_format=body.model_format
    )


@router.get("/status")
@inject
def get_status():
    return {"status": "OK"}
