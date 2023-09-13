from components.data_validation import DataValidataion
from configuration import ConfigurationManager
from predictor import CustomException


try:
    config = ConfigurationManager()
    data_val_config = config.get_data_validation_config()
    data_validation = DataValidataion(config_in=data_val_config)
    data_validation.validate_features()
except Exception as e:
    raise CustomException(e)


