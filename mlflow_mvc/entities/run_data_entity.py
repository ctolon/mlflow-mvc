from mlflow.entities import Run
import json
from typing import Optional

from mlflow_mvc.util.generic_transformers import genericTransformer

class RunDataEntity(object):
    """MLflow Entity Class for Run.data"""
    
    def __init__(self, run: Run, path_name: Optional[str] = None):
        self._run = genericTransformer(run.data)
        self._path_name = path_name

    @property
    def getModel(self):
        return self._run
        
    @property
    def getModelMetrics(self) -> dict:
        return self._run.get("metrics")
    
    @property
    def getModelParams(self) -> dict:
        return self._run.get("params")
    
    @property
    def getModelTags(self) -> dict:
        return self._run.get("tags")
    
    @property
    def getModelSourceName(self) -> str:
        return self.getModelTags.get("mlflow.source.name")
    
    @property
    def getModelSourceType(self) -> str:
        return self.getModelTags.get("mlflow.source.type")
    
    @property
    def getModelGitCommit(self) -> str:
        return self.getModelTags.get("mlflow.source.git.commit")
    
    # TODO for specific tags as a list, write queries
    #@property
    #def getModelSpecificTag(self):
        #return self.getModelTags.get("runtag")
    
    @property
    def getModelDescription(self) -> str:
        return self.getModelTags.get("mlflow.note.content")
    
    @property
    def getModelProjectEnv(self) -> str:
        return self.getModelTags.get("mlflow.project.env")
    
    @property
    def getModelRunName(self) -> str:
        return self.getModelTags.get("mlflow.runName")

        
    @property
    def getModelMetaData(self) -> dict:
        return json.loads(self.getModelTags.get("mlflow.log-model.history"))[0]
    
    @property
    def getModelRunId(self) -> str:
        return self.getModelMetaData.get("run_id")

    @property
    def getModelArtifactPath(self) -> str:
        return self.getModelMetaData.get("artifact_path")
    
    @property
    def getModelCreationTimeUTC(self) -> str:
        return self.getModelMetaData.get("utc_time_created")
    
    @property
    def getFlavors(self) -> dict:
        return self.getModelMetaData.get("flavors")
        
    @property
    def getPythonFunction(self) -> dict:
        return self.getFlavors.get("python_function")
    
    @property
    def getArtifacts(self) -> dict:
        return self.getPythonFunction.get("artifacts")
    
    @property
    def getModelPathAndUri(self) -> str:
        if not isinstance(self._path_name, str):
            raise TypeError(
                f"For using {RunDataEntity.getModelPathAndUri.fget.__name__} function you have to define path_name type as str"
                )
        return self.getArtifacts.get(self._path_name)
            
    @property
    def getModelPath(self) -> str:
        if not isinstance(self._path_name, str):
            raise TypeError(
                f"For using {RunDataEntity.getModelPath.fget.__name__} function you have to define path_name type as str"
                )
        return self.getArtifacts.get(self._path_name).get("path")

    @property
    def getModelUri(self) -> str:
        if not isinstance(self._path_name, str):
            raise TypeError(
                f"For using {RunDataEntity.getModelUri.fget.__name__} function you have to define path_name type as str"
                )
        return self.getArtifacts.get(self._path_name).get("uri")
    
    # TODO fix it
    @property
    def getModelLoaderModule(self):
        return self.getModelMetaData.get("loader_module")
    
    # TODO fix it
    @property
    def getModelPythonVersion(self):
        return self.getPythonFunction.get("python_version")
    
    @property
    def getModelCode(self) -> str:
        return self.getModelMetaData.get("code")
    
    @property
    def getModelEnv(self) -> str:
        return self.getModelMetaData.get("env")
    
    @property
    def getModelCondaEnv(self) -> str:
        return self.getModelEnv.get("conda")
    
    @property
    def getModelVirtualEnv(self) -> str:
        return self.getModelEnv.get("virtualenv")
    
    @property
    def getModelUUID(self) -> str:
        return self.getModelMetaData.get("model_uuid")
    
    @property
    def getModelMLflowVersion(self) -> str:
        return self.getModelMetaData.get("mlflow_version")