from DiamondPricePrediction.components.data_ingestion import DataIngestion
from DiamondPricePrediction.components.data_transformation import DataTransformation
from DiamondPricePrediction.components.model_trainer import ModelTrainer

import os
import sys
from DiamondPricePrediction.logger import logging
from DiamondPricePrediction.exception import CustomException
import pandas as pd

obj=DataIngestion()

train_data_path,test_data_path,raw_data_path=obj.initiate_data_ingestion()

data_transformation=DataTransformation()

train_arr,test_arr=data_transformation.initialize_data_transformation(train_data_path,test_data_path) 

model_trainer_obj = ModelTrainer()
model_trainer_obj.initiate_model_training(train_arr, test_arr)
