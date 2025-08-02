from DiamondPricePrediction.components.data_ingestion import DataIngestion

import os
import sys
from DiamondPricePrediction.logger import logging
from DiamondPricePrediction.exception import CustomException
import pandas as pd

obj=DataIngestion()

obj.initiate_data_ingestion()