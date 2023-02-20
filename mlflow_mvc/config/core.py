"""Global Config Settings Module"""

from mlflow_mvc.util.const import Const

class Config:
  """Config for mlflow tracking server"""
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
  """End-points RestAPI Routing"""
  GET_ARTIFACT_PATH = "/get-artifact"