# Here we will load the data
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from DiamondPricePrediction.logger import logging
from DiamondPricePrediction.exception import CustomException
 
from sklearn.model_selection import train_test_split 

from dataclasses import dataclass

from pathlib import Path
 


# Creating our own class

class DataIngestionConfig:
      raw_data_path:str=os.path.join("artifacts","raw_data.csv")
      train_data_path:str=os.path.join("artifacts","train_data.csv")
      test_data_path:str=os.path.join("artifacts","test_data.csv")
      






class DataIngestion:
      def __init__(self):
            self.ingestion_config=DataIngestionConfig()
           

      def initiate_data_ingestion(self):
            logging.info('Data Ingestion Started')
            
            try:
                  data=pd.read_csv(Path(os.path.join("/home/ankit/INEURON/ML_Project/notebooks/data/cubic_zirconia.csv")))
                  logging.info('Data Loaded Successfully')
                  
                  os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
                  data.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
                  logging.info("Saved the raw data in artifacts folder")
                  
                  
                  
                  logging.info('Splitting Data into Train and Test Split')
                  
                  train_data,test_data=train_test_split(data,test_size=0.25)
                  logging.info('Data Split Successfully')
                  
                  train_data.to_csv(self.ingestion_config.train_data_path,index=False)
                  test_data.to_csv(self.ingestion_config.test_data_path,index=False)
                  
                  logging.info('Data ingestion part completed')
                  
            
            
            
            except Exception as e:
                  logging.info('Exception Occurred in Data Ingestion')
                  raise(CustomException(e,sys))
      
      
           
            