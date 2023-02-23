"""mlflow-mvc Exceptions Module"""

class NotFoundError(Exception):
    """Base Class for Not Found"""
    
    entity_name: str

    def __init__(self, entity_id):
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")
   
class RecordNotFound(Exception):
    """Base Class for Not Found"""
    
    entity_name: str = "Experiment"
    
class EntityNotFoundError(Exception):
    """Base Class for Not Found"""
    
    entity_name: str = "Experiment"

class PropertyNotFoundError(Exception):
    """Base class for Property not found exception"""