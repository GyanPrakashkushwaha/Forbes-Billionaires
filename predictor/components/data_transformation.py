from predictor.utils import logger 
from config_entity import DataTransformationConfig
import pandas as pd
from sklearn.model_selection import train_test_split


class TransformData:
    def __init__(self,config_transform_data:DataTransformationConfig) -> None:
        self.trans_config = config_transform_data

    def train_test_split_func(self):
        df = pd.read_csv(self.trans_config.data_path)
        train_df , test_df = train_test_split(df,test_size=0.23)

        train_df.to_csv(self.trans_config.train_df_path,index=False)
        test_df.to_csv(self.trans_config.test_df_path,index=False)

        logger.info("Splited data into training and test sets")
        logger.info(train_df.shape)
        logger.info(test_df.shape)
