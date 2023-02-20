from mlflow.entities import Run

from mlflow_mvc.util.generic_transformers import genericTransformer
    
class RunInfoEntity(object):
    """MLflow Entity Class for Run.info"""
    
    def __init__(self, run: Run):
        self._run = genericTransformer(run.info)
        
    @property
    def getModelRunUUID(self) -> str:
        return self._run.get("run_uuid")
    
    @property
    def getModelExperimentId(self) -> str:
        return self._run.get("experiment_id")
    
    @property
    def getModelRunName(self) -> str:
        return self._run.get("run_name")
    
    @property
    def getUserId(self) -> str:
        return self._run.get("user_id")
    
    @property
    def getModelStatus(self) -> str:
        return self._run.get("status")
    
    @property
    def getModelStartTime(self) -> int:
        return self._run.get("start_time")
    
    @property
    def getModelEndTime(self) -> int:
        return self._run.get("end_time")
    
    @property
    def getModelArtifactUri(self) -> str:
        return self._run.get("artifact_uri")
    
    @property
    def getModelLifecycleStage(self) -> str:
        return self._run.get("lifecyle_stage")
    
    @property
    def getModelRunId(self) -> str:
        return self._run.get("run_id")