from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    data_path: Path
    params_weights: str
    params_include_top: bool 
    params_image_size: list 
    base_model: Path

@dataclass(frozen=True)
class DataPreprocessingConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    feature_list: Path 
    file_names: Path 
    params_target_size: list    