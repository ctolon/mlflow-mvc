"""Mlflow MVC Registered Models Service Interface"""

from interface import Interface
from typing import List

class IRegisteredModelService(Interface):
    """Mlflow MVC Registered Models Service Interface Class"""

    def list_all_registered_models(self) -> List[dict]:
        pass