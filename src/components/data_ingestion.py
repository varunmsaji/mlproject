import os 
import sys 
from src.exception import CustomException
from src.logger import logging
import pandas as pd 

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainer
from src.components.model_trainer import ModelTrainerConfig


@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','trian.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()


    def initiate_data_ingestion(self):
        logging.info("enter teh data ingestion method")
        try :
            df = pd.read_csv('notebook/stud.csv')    
            logging.info("read the data set")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info("trian test split initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            train_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("ingestion of the date is complere")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
             
        except Exception as e:
            raise CustomException(e,sys)
            pass

if __name__=='__main__':
    obj = DataIngestion()
    train ,test =obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train ,test,_= data_transformation.initiate_data_transformation(train,test)
    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train,test))
