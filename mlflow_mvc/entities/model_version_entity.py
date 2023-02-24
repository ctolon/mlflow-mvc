"Mlflow MVC Model Version Entity Module"

import json
from mlflow.entities.model_registry.model_version import ModelVersion

from ..util.type_safety import strict_prop_return, entity_type_check


class ModelVersionEntity(object):
    """Mlflow MVC Entity Class for Model Version"""

    def __init__(self, model_version: ModelVersion, strict_return: bool = True):
        entity_type_check(model_version, ModelVersion)
        self._model_version = model_version
        self._strict_return = strict_return

    # Getters
    @property
    def get_name(self) -> str:
        """String. Unique name within Model Registry."""
        prop = self._model_version.name
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_version(self) -> str:
        """String. Version"""
        prop = self._model_version.version
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_creation_timestamp(self) -> int:
        """Integer. Model version creation timestamp (milliseconds since the Unix epoch)."""
        prop = self._model_version.creation_timestamp
        if self._strict_return:
            return strict_prop_return(prop, int)
        return prop

    @property
    def get_last_updated_timestamp(self) -> int:
        """Integer. Timestamp of last update for this model version (milliseconds since the Unix
        epoch)."""
        prop = self._model_version.last_updated_timestamp
        if self._strict_return:
            return strict_prop_return(prop, int)
        return prop

    @property
    def get_current_stage(self) -> str:
        """String. Current stage of this model version."""
        prop = self._model_version.current_stage
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_description(self) -> str:
        """String. Description."""
        prop = self._model_version.description
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_source(self) -> str:
        """String. Source path of model."""
        prop = self._model_version.source
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_run_id(self) -> str:
        """String. MLflow run ID that generated this model."""
        prop = self._model_version.run_id
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_status(self) -> str:
        """String. MLflow run ID that generated this model."""
        prop = self._model_version.status
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_tags(self) -> dict:
        """Dictionary of tag key (string) -> tag value for the current model version."""
        prop = self._model_version.tags
        if self._strict_return:
            return strict_prop_return(prop, dict)
        return prop

    @property
    def get_run_link(self) -> str:
        """String. MLflow run link referring to the exact run that generated this model version."""
        prop = self._model_version.run_link
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    # Transformers
    def to_dictionary(self):
        return dict(self._model_version)

    def to_list(self):
        return list(self._model_version)

    def to_json(self):
        if not isinstance(dict, type(self._model_version)):
            return json.dumps(dict(self._model_version))
        return json.dumps(self._model_version)
