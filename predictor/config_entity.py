from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir:Path
    STATUS_file :str
    data_dir:Path
    schema_check:dict


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir : Path
    data_path : Path
    Status_file : str
    transform_train_df_path : Path
    transform_test_df_path : Path
    feature_renamer_scehma:dict


