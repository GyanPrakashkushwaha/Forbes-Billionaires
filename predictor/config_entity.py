from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir:Path
    STATUS_file :str
    data_dir:Path
    schema_check:dict





