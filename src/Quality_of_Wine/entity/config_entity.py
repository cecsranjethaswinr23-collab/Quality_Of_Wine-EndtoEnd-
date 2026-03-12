# packages for the entity functions
from dataclasses import dataclass
from pathlib import Path


# Entity of the Data Ingestion part
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


# Entity of the Data Validation part
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict


# Entity of the Data Transformation part
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path


# Entity of the Model Trainer part
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path  
    model_name: str           # takes the model name from the config.yaml 
    alpha: float              # hyperparams
    l1_ratio: float           # hyperparams
    target_column: str


# Entity of the Model Evaluation part
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
    mlflow_uri: str