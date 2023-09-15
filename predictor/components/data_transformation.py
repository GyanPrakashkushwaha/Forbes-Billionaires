from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler
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

        logger.info("Splited data into training and test sets")
        logger.info(train_df.shape)
        logger.info(test_df.shape)

        return (
            train_df,test_df
        )

    def scale_data(self):
        train_df , test_df = self.train_test_split_func()
        X_train = train_df.drop(columns=['net_worth','full_name'])
        X_test = test_df.drop(columns=['net_worth','full_name'])
        transformer = ColumnTransformer(transformers=[
                ('scale_values',MinMaxScaler(),['rank', 'age', 'country_of_citizenship', 'business_category', 'wealth_status'])

            ],remainder='passthrough')
        
        X_train_transformed = transformer.fit_transform(X_train)
        X_test_transformed = transformer.fit_transform(X_test)

        train_transformed = pd.DataFrame(data=X_train_transformed,columns=transformer.get_feature_names_out())
        test_transformed = pd.DataFrame(data=X_test_transformed,columns=transformer.get_feature_names_out())

        train_transformed.to_csv(self.trans_config.train_df_path,index=False)
        test_transformed.to_csv(self.trans_config.test_df_path,index=False)
        
        logger.info("transformed data")
        logger.info(train_transformed.shape)
        logger.info(test_transformed.shape)   

        