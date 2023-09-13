from predictor.constatns import *
from predictor.utils import *
from predictor.entity.config_entity import DataValidationConfig


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):


        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        creat_dirs([self.config.artifacts_root])

    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.INDEPENDENT_FEATURES

        creat_dirs([config.root_dir])
        

        data_validation_config =  DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_file=config.STATUS_FILE,
            data_dir=config.data_dir,
            schema_check=schema
        )

        return data_validation_config
        
        
        