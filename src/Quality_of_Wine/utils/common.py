import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

"""

In a professional End-to-End ML project, utils/common.py acts as the "Swiss Army Knife" of your codebase.
These functions are needed because ML pipelines are not just about math; they are about moving data safely
between different stages (Ingestion Transformation Training).

Here is why each specific function is essential for your project:

1. read_yaml
Why it's needed: Your project keeps paths in config.yaml and parameters in params.yaml.
The ML Role: Instead of "hardcoding" a path like C:/data/wine.csv inside your 
code (which would break on someone else's computer), you use read_yaml to pull that path
 from a central config file. It usually returns a ConfigBox, allowing you to access data 
 like config.artifacts_root instead of config['artifacts_root'].

2. create_directories
Why it's needed: ML pipelines generate many "artifacts" (folders for data, models, and plots).
If a folder doesn't exist when a script tries to save a file, the program will crash.
The ML Role: This function ensures that before any stage starts, the necessary "output" folders
are automatically created. It prevents the FileNotFoundError during long training runs.

3. save_json & load_json
Why it's needed: In ML, you often need to save Metadata or Metrics (like Accuracy, Precision, or Recall).
The ML Role: After training, you save the results in a .json file. This allows tools like MLflow or your
 app.py to read the model's performance without re-running the whole training process.

4. save_bin & load_bin (Binary Files)
Why it's needed: Python objects (like a trained Scikit-learn model or a Scaler) cannot be saved as plain text.
They must be converted to Binary format (usually using joblib or pickle).

The ML Role:
save_bin: Saves your trained "Wine Quality Model" to a file.
load_bin: Used in app.py to reload that exact model into memory to make real-time predictions for a user.

5. get_size
Why it's needed: ML datasets and models can become massive (Gigabytes).
The ML Role: This is a debugging and logging helper. It allows your logger to print something
like: INFO: Model saved successfully (Size: 250 KB). 
It helps you monitor if your data is growing unexpectedly or if a file saved is empty (0 KB).

Why use a "Common" file at all?

Without common.py, you would have to write the same 5 to 10 lines of "file-handling" code inside every
component (Data Ingestion, Model Trainer, etc.).
By putting them in utils:Cleaner Logic: Your ModelTrainer.py only contains training code, not "how to open a file" code.
Centralized Error Handling: If you want to change how your project handles errors (e.g., adding a specific log message
whenever a folder is created), you only have to change it in one place.
Standardization: Every developer on the team uses the exact same method to read files, ensuring the project is predictable.


"""


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")




@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
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




