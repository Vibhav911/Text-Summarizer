import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations # function might work even if datatype of arguments specified and used are different
from box import ConfigBox             # to ensure that this does not happen we use ensure_annotations as it will give an error
from pathlib import Path              # when the datatype specified and used are different
from typing import Type


# This program is used to read YAML files
@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:   # d = {'key':"value",'key1':"value1"} | d['key']: works, d.key: not work
    ''' 
    reads yaml files and returns            # d2= ConfigBox({'key':"value", "key1":"vlue1"}) | d.key:works, d2['key']:works
    
    args: path_to_yaml (str) : path like imput
    
    Raises :
          ValueError: if yaml file is empty
          e: empty file
          
    Returns:
        ConfigBox: ConfigBox type
    '''
    
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file : {path_to_yaml} is loaded successfully')
            return ConfigBox(content)
        
    except BoxValueError :
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e
    

# This program is used to create directories
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    ''' Creates list of directories
    
    args:
        path_to_directories (list) : list of directories to be created
        ignore_log (bool, optional): ignore if multiple directories is to be created. Defaults to false
    '''
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")
            
            
# This program is used to get the size of a file
@ensure_annotations
def get_size(path : Path) -> str:
    ''' get size in KB
    
    Args: path(Path) : path of the file
    Returns:
        str: size in KB
    '''
    
    size_in_kb = round(os.path.getsize(path)/1024)
    return f'~ {size_in_kb} KB'
            
            