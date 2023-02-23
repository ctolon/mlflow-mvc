"""mlflow-mvc Standard Logging Module For Mostly Service Layer"""

import logging
from logging import RootLogger
from mlflow_mvc.util.decorators import setter_onlyf

class MasterLogger(object):
    """Main class for logging mlflow-mvc as standard"""

    def __init__(self):
        self._logger = logging.getLogger("crumbs")
        self._datefmt = "%d-%m-%y, %H:%M:%S"
        self._logfmt = "[%(asctime)s] {%(filename)s - L#%(lineno)d} [%(levelname)s] - %(message)s"

    @setter_onlyf
    def set_datemt(self, value):
        self._datefmt = value

    @setter_onlyf
    def set_logfmt(self, value):
        self._logfmt = value

    @property
    def get_logger(self) -> RootLogger:
        logging.basicConfig(format=self._logfmt, level="INFO", datefmt=self._datefmt)
        return self._logger