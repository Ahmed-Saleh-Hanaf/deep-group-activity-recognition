

import os 
import yaml

def load_config(path: str):
    """
    This function is responsible for load config and return it
    Args:
        path (str): path of the config
    """
    # validation
    if not os.path.exists(path):
        raise FileNotFoundError("Config path not found {path}")
    
    with open(path, 'r') as file:
        config = yaml.safe_load(file)
    return config