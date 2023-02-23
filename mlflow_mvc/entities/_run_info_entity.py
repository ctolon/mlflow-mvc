"Mlflow MVC Run-Info Entity Module"

from mlflow.entities import Run

from ..util.type_safety import strict_prop_return, entity_type_check
    
class RunInfoEntity(object):
    """Mlflow MVC Entity Class for Run.info"""
    
    def __init__(self, run: Run, strict_return: bool = True):
        entity_type_check(run, Run) 
        self._run = dict(run.info)
        self._strict_return = strict_return
        
    # Getters    
    @property
    def get_run_uuid(self) -> str:
        prop = self._run.get("run_uuid")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop
    
    @property
    def get_experiment_id(self) -> str:
        """String. The experiment ID."""
        prop = self._run.get("experiment_id")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop
    
    @property
    def get_run_name(self) -> str:
        """String. The name of the run."""
        prop = self._run.get("run_name")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop
    
    @property
    def get_user_id(self) -> str:
        """String. User that created this."""
        prop = self._run.get("user_id")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop
    
    @property
    def get_status(self) -> str:
        """String. Status of the run"""
        prop = self._run.get("status")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop
    
    @property
    def get_start_time(self) -> int:
        """Integer. Run creation timestamp (milliseconds since the Unix epoch)."""
        prop = self._run.get("start_time")
        if self._strict_return:
            return strict_prop_return(prop, int)
        return prop
    
    @property
    def get_end_time(self) -> int:
        """Integer. End of run timestamp (milliseconds since the Unix epoch)."""
        prop = self._run.get("end_time")
        if self._strict_return:
            return strict_prop_return(prop, int)
        return prop
    
    @property
    def get_artifact_uri(self) -> str:
        prop = self._run.get("artifact_uri")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop
    
    @property
    def get_lifecycle_stage(self) -> str:
        """Lifecycle stage of the run. Can either be 'active' or 'deleted'."""
        prop = self._run.get("lifecycle_stage")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop
    
    @property
    def get_run_id(self) -> str:
        """String ID of run."""
        prop = self._run.get("run_id")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop