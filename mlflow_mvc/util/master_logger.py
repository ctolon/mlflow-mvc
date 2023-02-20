import logging
from logging import RootLogger
from mlflow_mvc.util.decorators import setterOnly

class MasterLogger(object):
    """Main class for logging"""

    def __init__(self):
        self._logger = logging.getLogger("crumbs")
        self._datefmt = "%d-%m-%y, %H:%M:%S"
        self._logfmt = "[%(asctime)s] {%(filename)s - L#%(lineno)d} [%(levelname)s] - %(message)s"

    @setterOnly
    def set_datemt(self, value):
        self._datefmt = value

    @setterOnly
    def set_logfmt(self, value):
        self._logfmt = value

    @property
    def get_logger(self) -> RootLogger:
        logging.basicConfig(format=self._logfmt, level="INFO", datefmt=self._datefmt)
        return self._logger

# usage ex for singleton logger:    
# logger = MasterLogger.get_logger