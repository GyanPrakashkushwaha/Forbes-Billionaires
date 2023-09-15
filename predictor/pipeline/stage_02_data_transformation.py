from components.data_transformation import TransformData
from configuration import ConfigurationManager
from predictor import logger , CustomException


STAGE_NAME = 'Data Transformation stage'

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = TransformData(config_transform_data=data_transformation_config)
        data_transformation.train_test_split_func()
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise CustomException(e)
