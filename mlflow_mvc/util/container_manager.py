from dependency_injector import containers
from ..config.core import Config
from typing import Optional, Any


class ContainerManager(object):
    """Class For Create instance of container."""
    
    def __init__(self, container: containers.DeclarativeContainer, config_file: Optional[str] = Config.BASE_CONFIG_DIR):
        self._container = container
        self._config_file = config_file
        self._container.init_resources()
        self._container.config.from_yaml(config_file)
        self._container.wire(modules=[__name__])
        
    @property
    def get_container(self) -> Any:
        return self._container
    
    @property
    def get_config_file(self):
        return self._config_file
