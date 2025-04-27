import os
import sys
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from networksecurity.constant.training_pipeline import TARGET_COLUMN, DATA_TRANSFORMATION_IMPUTER_PARAMS
from networksecurity.entity.artifact_entity import DataValidationArtifact, DataTransformationAritfact
from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.utils.main_utils.utils import save_numpy_array_data, save_object

class DataTransformation:
    def __init__(self, data_validation_artifact: DataValidationArtifact,
                 data_transformation_config: DataTransformationConfig):
        try:
            self.data_validation_artifact = data_validation_artifact
            self.data_transformation_config = data_transformation_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    @staticmethod
    def read_data(file_path):
        try:
            df = pd.read_csv(file_path)
            df.columns = df.columns.str.strip()  # Strip spaces from column names
            return df
        except Exception as e:
            raise Exception(f"Error reading file {file_path}: {str(e)}")

    def get_datatransformer_object(self) -> Pipeline:
        logging.info("Entering get_datatransformer_object method")
        try:
            imputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            processor = Pipeline([("imputer", imputer)])
            logging.info(f"KNNImputer initialized with params: {DATA_TRANSFORMATION_IMPUTER_PARAMS}")
            return processor
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_transformation(self) -> DataTransformationAritfact:
        logging.info("Entering initiate_data_transformation method")
        try:
            # Read the validated training and test data
            train_df = self.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df = self.read_data(self.data_validation_artifact.valid_test_file_path)

            # Print columns to verify the presence of 'Result'
            logging.info(f"Train Data Columns: {train_df.columns}")
            logging.info(f"Test Data Columns: {test_df.columns}")

            # Check if the target column exists in the training data
            if TARGET_COLUMN not in train_df.columns:
                raise Exception(f"Target column '{TARGET_COLUMN}' not found in training data!")

            # Split input and target features
            input_feature_train_df = train_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_feature_train_df = train_df[TARGET_COLUMN].replace(-1, 0)

            input_feature_test_df = test_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_feature_test_df = test_df[TARGET_COLUMN].replace(-1, 0)

            # Data transformation
            preprocessor = self.get_datatransformer_object()
            preprocessor_object = preprocessor.fit(input_feature_train_df)
            transformed_input_train_features = preprocessor_object.transform(input_feature_train_df)
            transformed_input_test_features = preprocessor_object.transform(input_feature_test_df)

            # Merge features and targets
            train_arr = np.c_[transformed_input_train_features, np.array(target_feature_train_df)]
            test_arr = np.c_[transformed_input_test_features, np.array(target_feature_test_df)]

            # Save transformed data
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path, array=train_arr)
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path, array=test_arr)
            save_object(self.data_transformation_config.transformed_object_file_path, preprocessor_object)

            # Prepare and return artifact
            data_transformation_artifact = DataTransformationAritfact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path,
            )

            logging.info("Data transformation completed successfully")
            return data_transformation_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)

