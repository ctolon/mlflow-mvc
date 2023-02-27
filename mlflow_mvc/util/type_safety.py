"""Python Type Safety Module"""

from typing import Type, Any
from mlflow_mvc.util.exceptions import PropertyNotFoundError


class _MetaConst(type):
    """Meta Const Class"""
    
    def __getattr__(cls, key):
        return cls[key]

    def __setattr__(cls, key, value):
        raise TypeError


class Const(object, metaclass=_MetaConst):
    """Python Constant Implementation as Base Class
    
    Usage Example:
    
    class People(Const):
      PI = 3.14
      RED = "red"
          
    >> People.PI   
    """
    
    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        raise TypeError


def strict_prop_return(prop: Any , expected_type: Type) -> Any:
    """This function allows to static type checking for Entity properties

    Args:
        prop (Any): Property of Entity Class
        expected_type (Type): Return Type as expected

    Raises:
        TypeError: When property return type false
        EntityNotFoundError: When property type is None

    Returns:
        Any: Property
    """
    
    if prop is None:
        raise PropertyNotFoundError("Property Not Found!")
    prop_type = type(prop)
    if not isinstance(prop, expected_type):
        print(prop)
        raise TypeError(f"Expected Type: {expected_type} === Return Type: {prop_type}")
    return prop


def entity_type_check(entity_type_actual: Any, entity_type_expected: Any) -> None:
    """Static entity type checker on instance

    Args:
        entity_type_actual (Any): Providede entity
        entity_type_expected (Any): Expected mlflow entity

    Raises:
        TypeError: If Entity type is wrong
    """
    
    if not isinstance(type(entity_type_actual), type(entity_type_expected)):
        raise TypeError(f"Wrong Type for Run Entity. Expected: {type(entity_type_expected)} == Provided: {type(entity_type_actual)}") 