
import os

from yaml import load, CLoader as Loader

'''how in general can you make this shit so that it works fine and does not require a config???'''

def configLoad(): #fucking name, config
    try:
        with open('config.yml') as file:
            data = load(file, Loader = Loader)

            if not(os.path.exists((path := data \
                ['log']['path'])) and os.path.isdir(
                    path)): os.mkdir(path)

            return data
    except FileNotFoundError: return \
        {'log': {'enable': False}}
