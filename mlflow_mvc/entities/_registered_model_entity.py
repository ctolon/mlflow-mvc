"Mlflow MVC Registered Model Entity Module"

from mlflow.entities.model_registry import RegisteredModel
from mlflow.entities.model_registry.model_version import ModelVersion
from typing import List
import json


from ..util.type_safety import strict_prop_return, entity_type_check


class RegisteredModelEntity(object):
    """Mlflow MVC Entity Class for Registered Models"""

    def __init__(self, registered_model: RegisteredModel, strict_return: bool = True):
        entity_type_check(registered_model, RegisteredModel)
        self._registered_model = registered_model
        self._strict_return = strict_return

    @property
    def get_name(self) -> str:
        """String. Registered model name."""
        prop = self._registered_model.name
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_creation_timestamp(self) -> int:
        """Integer. Model version creation timestamp (milliseconds since the Unix epoch)."""
        prop = self._registered_model.creation_timestamp
        if self._strict_return:
            return strict_prop_return(prop, int)
        return prop

    @property
    def get_last_updated_timestamp(self) -> int:
        """Integer. Timestamp of last update for this model version (milliseconds since the Unix
        epoch)."""
        prop = self._registered_model.last_updated_timestamp
        if self._strict_return:
            return strict_prop_return(prop, int)
        return prop

    @property
    def get_description(self) -> str:
        """String. Description"""
        prop = self._registered_model.description
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop
    
    @property
    def get_latest_versions(self) -> List[ModelVersion]: # Can be None?
        """List of the latest mlflow.entities.model_registry.ModelVersion instances for each stage"""
        prop = self._registered_model.latest_versions
        if self._strict_return:
            return strict_prop_return(prop, list)
        return prop
    
    # Transformers
    def to_dictionary(self):
        return dict(self._registered_model)

    def to_list(self):
        return list(self._registered_model)

    def to_json(self):
        if not isinstance(dict, type(self._registered_model)):
            return json.dumps(dict(self._registered_model))
        return json.dumps(self._registered_model)
