import os
import json
import joblib
import yaml
from pathlib import Path
from box.exceptions import BoxValueError
from cnnclassifier import logger
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
import base64


@ensure_annotations
def read_yaml(yaml_path:Path)->ConfigBox:
     
    """reads yaml file and returns

    Args:
       yaml_path (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(yaml_path,'r') as f:
            data=yaml.safe_load(f)
            logger.info(f"yaml file {yaml_path} loaded sucessfully")
            return ConfigBox(data)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(list_of_dir:list,verbose=True):
    """create list of directories

    Args:
        list_of_dir (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in list_of_dir:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created a directory {path}")


@ensure_annotations
def save_json(path:Path,data:dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path,'w') as f:
        json.dump(data,f,indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path:Path)->ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path,'r') as f:
        data=json.load(f)
    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(data)
    

@ensure_annotations
def save_bin(data:Any,path:Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path:Path)->Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data=joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())





