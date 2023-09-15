from predictor.constatns import *
from utils import *
from predictor.config_entity import (DataTransformationConfig,
                                      DataValidationConfig)


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):


        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_dirs([self.config.artifacts_root])

    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.INDEPENDENT_FEATURES

        create_dirs([config.root_dir])
        

        data_validation_config =  DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_file=config.STATUS_FILE,
            data_dir=config.data_dir,
            schema_check=schema
        )

        return data_validation_config
    
    
    def get_data_transformation_config(self):
        config = self.config.data_transformation
        schema = self.schema.columns_renamer

        create_dirs([config.root_dir])

        return DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            Status_file=config.STATUS_FILE,
            transform_train_df_path=config.transformed_train_df_path,
            transform_test_df_path=config.transformed_test_df_path,
            feature_renamer_scehma=schema
        )
        
        
        
        