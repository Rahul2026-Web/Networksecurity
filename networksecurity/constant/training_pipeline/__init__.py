import os
import sys
import numpy as np
import pandas as pd

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME

"""


TARGET_COLUMN ="Result"
# PIPELINE_NAMR:str="NetworkSecurity"
# ARTIFACT_DIT:str="Artifacts"
FILE_NAME:str="Phising_Detection_Dataset.csv"

TRAIN_FILE_NAME: str="train.csv"
TEST_FILE_NAME="test.csv"

PIPELINE_NAME = "NetworkSecurityPipeline"
ARTIFACT_DIR = "artifact"



DATA_INGESTION_COLLECTION_NAME:str="NetworkData"
DATA_INGESTION_DATABASE_NAME:str="rahul_yadav"
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR = "ingested_data"
# DATA_INGESTON_INGESTION_DIR:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float=0.2




# networksecurity/constant/training_pipeline.py

# Add this line to define the missing constant
#DATA_INGESTION_INGESTED_DIR = "ingested_data"
