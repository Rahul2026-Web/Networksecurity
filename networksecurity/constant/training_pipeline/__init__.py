# import os
import sys
import numpy as np
import pandas as pd

import os

SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")


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


"""
Data Vaalidation related constant start with DATA_VALIDATION VAR NAME

"""
DATA_VALIDATION_DIR_NAME: str="data_validation"
DATA_VALIDATION_VALID_DIR: str= "validated"
DATA_VALIDATION_INVALID_DIR:str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str="dritf_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str ="report.yaml"
PREPROCESSING_OBJECT_NAME="preprocessing.pkl"


"""
Data Transformation related constand start with DATA_TRANSFORMATION VAR NAME

"""
# Constants related to data transformation

TARGET_COLUMN: str = 'Result'  # Ensure this is the exact column name

DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DIR_NAME: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_NAME: str = "preprocessing.pkl"

# KNN imputer parameters
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}




