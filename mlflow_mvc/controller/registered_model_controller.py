"""Mlflow MVC Registered Models Controller Module"""

from typing import List
from dependency_injector.wiring import inject

from ..service.registered_model_service import RegisteredModelService


class RegisteredModelController(object):
    """Mlflow MVC Registered Models Controller Implementation"""

    @inject
    def __init__(self, registered_model_service: RegisteredModelService):
        self._registered_model_service = registered_model_service

    def list_all_registered_models(self) -> List[dict]:
        return self._registered_model_service.list_all_registered_models()
