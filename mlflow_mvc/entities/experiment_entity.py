"Mlflow MVC Experiment Entity Module"

import json
from mlflow.entities.experiment import Experiment

from ..util.type_safety import strict_prop_return, entity_type_check


class ExperimentEntity(object):
    """Mlflow MVC Entity Class for Experiment"""

    def __init__(self, experiment: Experiment, strict_return: bool = True):
        entity_type_check(experiment, Experiment)
        self._experiment = experiment
        self._strict_return = strict_return

    # Getters
    @property
    def get_experiment_id(self) -> str:
        """String ID of experiment."""
        prop = self._experiment.experiment_id
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_name(self) -> str:
        """String name of experiment."""
        prop = self._experiment.name
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_artifact_location(self) -> str:
        """Dictionary of tag key (string) -> tag value for the current model version."""
        prop = self._experiment.artifact_location
        return strict_prop_return(prop, str)

    @property
    def get_lifecycle_stage(self) -> str:
        """Lifecycle stage of the experiment. Can either be 'active' or 'deleted'."""
        prop = self._experiment.lifecycle_stage
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_last_updated_timestamp(self) -> int:
        """Integer. Timestamp of last update for this experiment (milliseconds since the Unix
        epoch)."""
        prop = self._experiment.last_update_time
        if self._strict_return:
            return strict_prop_return(prop, int)
        return prop

    @property
    def get_creation_time(self) -> int:
        """Integer. Experiment creation timestamp (milliseconds since the Unix epoch)."""
        prop = self._experiment.creation_time
        if self._strict_return:
            return strict_prop_return(prop, int)
        return prop

    @property
    def get_tags(self) -> dict:
        """Tags that have been set on the experiment."""
        prop = self._experiment.tags
        if self._strict_return:
            return strict_prop_return(prop, dict)
        return prop

    # Transformers
    def to_dictionary(self):
        return dict(self._experiment)

    def to_list(self):
        return list(self._experiment)

    def to_json(self):
        if not isinstance(dict, type(self._experiment)):
            return json.dumps(dict(self._experiment))
        return json.dumps(self._experiment)
