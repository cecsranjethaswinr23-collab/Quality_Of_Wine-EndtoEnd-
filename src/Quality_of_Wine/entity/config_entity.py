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