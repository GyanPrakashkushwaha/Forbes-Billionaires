from pipeline.stage_02_data_transformation import DataTransformationTrainingPipeline
from predictor import logger , CustomException
from predictor.pipeline.stage_01_data_validation import DataValidationTrainingPipeline



# STAGE_NAME = "Data Validation stage"
# try:
#    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
#    data_ingestion = DataValidationTrainingPipeline()
#    data_ingestion.main()
#    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         logger.exception(e)
#         raise CustomException(e)


STAGE_NAME = 'Data Transformation stage'
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   obj = DataTransformationTrainingPipeline()
   obj.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
   logger.exception(e)
   raise CustomException(e)
