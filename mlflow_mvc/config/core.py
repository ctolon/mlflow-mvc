"""Global Config Settings Module"""

from ..util.type_safety import Const
import os


class Config:
    """Config Provider Alternative Class for Mlflow Tracking Server
    """

    BASE_CONFIG_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/application_properties.yml"

    # DEPRECATED: Use BASE_CONFIG_DIR Instead of this
    __conf = {
        "TRACKING_SERVER_URI": "http://0.0.0.0:5000",
    }
    __setters = ["TRACKING_SERVER_URI"]

    @staticmethod
    def get(name):
        return Config.__conf[name]

    @staticmethod
    def set(name, value):
        if name in Config.__setters:
            Config.__conf[name] = value
        else:
            raise NameError(f"{name} not accepted in set() method!")


class ApiPath(Const):
    """RestAPI End-points in Mlflow Core Framework"""

    GET_ARTIFACT_PATH = "/get-artifact"
