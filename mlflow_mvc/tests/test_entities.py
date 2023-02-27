import pytest

from mlflow_mvc.containers.controller_container import ControllersContainer
from mlflow_mvc.containers.repository_container import RepositoriesContainer
from mlflow_mvc.entities.run_data_entity import RunDataEntity
from mlflow_mvc.entities.run_info_entity import RunInfoEntity
from mlflow_mvc.entities.experiment_entity import ExperimentEntity
from mlflow_mvc.entities.model_version_entity import ModelVersionEntity
# from mlflow_mvc.entities.registered_model_entity import RegisteredModel


def test_latest_model_validation():
    container = ControllersContainer()
    check = container.model_version_controller().latest_model_validator(
        model_name="skbc",
        criteria="700",
        selected_metric="epoch"
    )
    assert check is True


def test_run_data_entity_properties():
    container = RepositoriesContainer()
    latest_model = container.model_version_repository().find_latest_model_version_by_model_name(model_name="skbc")
    run_id = latest_model.run_id
    run_entity = container.run_repository().find_run_by_run_id(run_id=run_id)
    run_data_model = RunDataEntity(run_entity, "fasttext_model_path")

    public_method_names = [method for method in dir(run_data_model) if callable(getattr(run_data_model, method)) if
                           not method.startswith('_')]  # 'private' methods start from _

    for method in public_method_names:
        getattr(run_data_model, method)()  # call


def test_run_info_entity_properties():
    container = RepositoriesContainer()
    latest_model = container.model_version_repository().find_latest_model_version_by_model_name(model_name="skbc")
    run_id = latest_model.run_id
    run_entity = container.run_repository().find_run_by_run_id(run_id=run_id)
    run_info_model = RunInfoEntity(run_entity)

    public_method_names = [method for method in dir(run_info_model) if callable(getattr(run_info_model, method)) if
                           not method.startswith('_')]  # 'private' methods start from _

    for method in public_method_names:
        getattr(run_info_model, method)()  # call


def test_experiment_entity_properties():
    container = RepositoriesContainer()
    experiments = container.experiment_repository().find_all_experiments_as_paged_list()
    experiment_sample = experiments[1]
    experiment_model = ExperimentEntity(experiment=experiment_sample)
    public_method_names = [method for method in dir(experiment_model) if callable(getattr(experiment_model, method)) if
                           not method.startswith('_')]  # 'private' methods start from _
    for method in public_method_names:
        getattr(experiment_model, method)()  # call


def test_model_version_entity_properties():
    container = RepositoriesContainer()
    model_version = container.model_version_repository().find_latest_model_version_by_model_name("skbc")
    model_version = ModelVersionEntity(model_version)
    public_method_names = [method for method in dir(model_version) if callable(getattr(model_version, method)) if
                           not method.startswith('_')]  # 'private' methods start from _
    for method in public_method_names:
        getattr(model_version, method)()  # call


"""
def test_registered_model_entity_properties():
    container = RepositoriesContainer()
    registered_model = container.registered_model_repository().find_all_registered_models()
"""
