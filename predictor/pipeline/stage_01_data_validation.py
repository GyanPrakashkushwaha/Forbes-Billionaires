from components.data_validation import DataValidataion
from configuration import ConfigurationManager
from predictor import CustomException , logger


STAGE_NAME = "Data Validation stage"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_val_config = config.get_data_validation_config()
        data_validation = DataValidataion(config_in=data_val_config)
        data_validation.validate_features()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise CustomException(e)



