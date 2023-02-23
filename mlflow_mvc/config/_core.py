"""Global Config Settings Module"""

from ..util.type_safety import Const

class Config:
  """Config Provider Alternative Class for Mlflow Tracking Server

  DEPRECATED: Use config.yml configuration instead of this  
  """
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