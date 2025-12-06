import json 
import yaml

path="test.json"

def fun(obj):
    if isinstance(obj,path):
        with open(path) as f:
            json.load(path)
    else:
        with open(path) as f:
            yaml.safe_load(path)
    return fun()
