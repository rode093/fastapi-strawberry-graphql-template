import yaml
import os
from singleton_decorator import singleton
@singleton
class Config:    
    def __init__(self, path="config.yml") -> None:
        # Load config file
        self.config = yaml.load(open(os.getcwd()+ '/'+path), Loader=yaml.SafeLoader)
        Config.__instance=self
    
    def get(self, key): 
        return self.config[key] or None
        