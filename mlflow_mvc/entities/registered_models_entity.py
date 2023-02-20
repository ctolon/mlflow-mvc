from mlflow.entities.model_registry.model_version import ModelVersion

# TODO complete it
class RegisteredModelEntity(object):
    """MLflow Entity Class for Registered Models"""
    
    def __init__(self, model_version: ModelVersion):
        self._model_version = model_version
                
    @property
    def getName(self) -> str:
        return self._model_version.get("name")
    
    @property
    def getCreationTimestamp(self) -> str:
        return self._model_version.get("creation_timestamp")
    
    @property
    def getLastUpdateTime(self) -> str:
        return self._model_version.get("last_update_time")
    
    @property
    def getDescription(self) -> str:
        return self._model_version.get("last_updated_timestamp")
    
    # TODO extend it
