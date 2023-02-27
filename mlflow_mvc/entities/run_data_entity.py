"Mlflow MVC Run-Data Entity Module"

from mlflow.entities import Run
import json

from ..util.type_safety import strict_prop_return, entity_type_check


class RunDataEntity(object):
    """Mlflow MVC Entity Class for Run.data"""

    def __init__(self, run: Run, strict_return: bool = True):
        entity_type_check(run, Run)
        self._run = dict(run.data)
        self._strict_return = strict_return
        
    def __str__(self):
        return json.dumps(dict(self._run))

    # Getters
    @property
    def get_run(self):
        """Dictionary. Processable run entity."""
        return self._run

    @property
    def get_metrics(self) -> dict:
        """Dictionary of string key -> metric value for the current run.
        For each metric key, the metric value with the latest timestamp is returned.
        In case there are multiple values with the same latest timestamp, the maximum of these values is returned."""
        prop = self._run.get("metrics")
        if self._strict_return:
            return strict_prop_return(prop, dict)
        return prop

    @property
    def get_params(self) -> dict:
        """Dictionary of param key (string) -> param value for the current run."""
        prop = self._run.get("params")
        if self._strict_return:
            return strict_prop_return(prop, dict)
        return prop

    @property
    def get_run_tags(self) -> dict:
        """Dictionary of tag key (string) -> tag value for the current run."""
        prop = self._run.get("tags")
        if self._strict_return:
            return strict_prop_return(prop, dict)
        return prop

    @property
    def get_source_name(self) -> str:
        """URI indicating the location of the model artifacts"""
        prop = self.get_run_tags.get("mlflow.source.name")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_source_type(self) -> str:
        """String. URI indicating the location of the model artifacts."""
        prop = self.get_run_tags.get("mlflow.source.type")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_git_commit(self) -> str:
        """String. Latest git commit of run."""
        prop = self.get_run_tags.get("mlflow.source.git.commit")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    # TODO for specific tags as a list, write queries
    # @property
    # def getModelSpecificTag(self):
    # return self.get_run_tags.get("runtag")

    @property
    def get_description(self) -> str:
        """String. Optional description for run."""
        prop = self.get_run_tags.get("mlflow.note.content")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_project_env(self) -> str:
        """String. Project environment of run."""
        prop = self.get_run_tags.get("mlflow.project.env")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_run_name(self) -> str:
        """String. Name of the run."""
        prop = self.get_run_tags.get("mlflow.runName")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_model_log_history(self) -> dict:
        """Dictionary. Model log history."""
        prop = json.loads(self.get_run_tags.get("mlflow.log-model.history"))[0]
        if self._strict_return:
            return strict_prop_return(prop, dict)
        return prop

    @property
    def get_run_id(self) -> str:
        """String. ID of the run to restore."""
        prop = self.get_model_log_history.get("run_id")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_artifact_path(self) -> str:
        """String. Artifact path of run."""
        prop = self.get_model_log_history.get("artifact_path")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_utc_time_created(self) -> str:
        """String. Creation time in UTC of run."""
        prop = self.get_model_log_history.get("utc_time_created")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_flavors(self) -> dict:
        """Dictionary. Model train meta data."""
        prop = self.get_model_log_history.get("flavors")
        if self._strict_return:
            return strict_prop_return(prop, dict)
        return dict

    @property
    def get_python_function(self) -> dict:
        """Dictionary. Python function which model trained."""
        prop = self.get_flavors.get("python_function")
        if self._strict_return:
            return strict_prop_return(prop, dict)
        return dict

    @property
    def get_artifacts(self) -> dict:
        """Dictionary. Saved Artifacts of run."""
        prop = self.get_python_function.get("artifacts")
        if self._strict_return:
            return strict_prop_return(prop, dict)
        return prop

    @property
    def get_loader_module(self):
        """String. Mlflow loader module of model."""
        prop = self.get_python_function.get("loader_module")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_python_version(self) -> str:
        """String. Python version of run."""
        prop = self.get_python_function.get("python_version")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_code(self) -> str:
        """String. Code of model."""
        prop = self.get_python_function.get("code")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_model_env(self) -> dict:
        """Dictionary. Model Enviroment yaml files."""
        prop = self.get_python_function.get("env")
        if self._strict_return:
            return strict_prop_return(prop, dict)
        return prop

    @property
    def get_conda_env(self) -> str:
        """String. Conda environment yaml file of run"""
        prop = self.get_model_env.get("conda")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_virtual_env(self) -> str:
        """String. Virtual environment yaml file of run"""
        prop = self.get_model_env.get("virtualenv")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_model_uuid(self) -> str:
        """String. Model uuid regarding to run."""
        prop = self.get_model_log_history.get("model_uuid")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop

    @property
    def get_mlflow_version(self) -> str:
        """String. Mlflow version of run."""
        prop = self.get_model_log_history.get("mlflow_version")
        if self._strict_return:
            return strict_prop_return(prop, str)
        return prop
