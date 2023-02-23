"""Generic Transformations Functions Module"""

from typing import List, Any
from mlflow.store.entities.paged_list import PagedList
from mlflow.entities.experiment import Experiment
from mlflow.entities.run import Run
from mlflow.entities.model_registry.model_version import ModelVersion
from mlflow.entities.model_registry import RegisteredModel

mlflow_entity_list = [Experiment, Run, ModelVersion, RegisteredModel]
mlflow_entity_types = [type(entity) for entity in mlflow_entity_list]
mlflow_entity_names = [entity.__name__ for entity in mlflow_entity_list]

                 
def generic_multi_transformer(value: PagedList[Any]) -> List[dict]:
    """Generic Multi Transformer Class For Handle Mlflow Generic Type Entities

    Args:
        value (PagedList[Any]): Mlflow one of to Entity Type in PagedList >> Run, Experiment, ModelVersion or RegisteredModel

    Returns:
        List[dict]: Processable Entity
    """
    
    global mlflow_entity_list
    global mlflow_entity_types
    global mlflow_entity_names
    
    enities_in_paged_list = [PagedList[entity] for entity in mlflow_entity_list]
    entity_types_in_pages_list = []
    
    #if type(value) not in enities_in_paged_list:
        #raise TypeError("Invalid type of Mlflow Entity. You should provide type in one of these types: ", mlflow_entity_names)
    
    # TODO apply functional programming
    merge_list = []
    for i in range(len(value)):
        merge_list.append(dict((x, y) for x, y in tuple(value[i])))
    return merge_list
    