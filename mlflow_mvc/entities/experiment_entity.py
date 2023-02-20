from mlflow.entities.experiment import Experiment
from typing import List

class ExperimentEntity(object):
    """MLflow Entity Class for Experiment"""
    
    def __init__(self, experiment: Experiment):
        self._experiment = experiment
        
    @property
    def getExperimentId(self) -> str:
        return self._experiment.get("experiment_id")
        
    @property
    def getName(self) -> str:
        return self._experiment.get("name")
    
    @property
    def getArtifactLocation(self) -> str:
        return self._experiment.get("artifact_location")
    
    @property
    def getLifecycleStage(self) -> str:
        return self._experiment.get("lifecycle_stage")
    
    @property
    def getLastUpdateTime(self) -> str:
        return self._experiment.get("last_update_time")
    
    @property
    def getCreationTime(self) -> str:
        return self._experiment.get("creation_time")
    
    @property
    def getTags(self) -> List[dict]:
        return self._experiment.get("tags")
    
