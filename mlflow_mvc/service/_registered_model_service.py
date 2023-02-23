"""Mlflow MVC Registered Models Service Module"""

from typing import List
from interface import implements

from .interface._i_registered_model_service import IRegisteredModelService
from ..repository import RegisteredModelRepository
from ..util.master_logger import MasterLogger

# Global logger settings
logger = MasterLogger().get_logger


class RegisteredModelService(implements(IRegisteredModelService)):
    """Mlflow MVC Registered Models Service Implementation"""

    def __init__(self, registered_models_repository :RegisteredModelRepository):

        self._registered_models_repository = registered_models_repository

    def list_all_registered_models(self) -> List[dict]:
        """Get All Registered Model Entities from Mlflow.

        Returns:
            List[dict]: All Registered Model entities as a dict in List.
        """
        return self._registered_models_repository.find_all_registered_models()
