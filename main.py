from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys

if __name__ == '__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionaritfact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation completed")
        print(dataingestionaritfact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionaritfact,data_validation_config)
        logging.info("Initate the data Validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data validation completed")
        print(data_validation_artifact)


    except Exception as e:
        raise NetworkSecurityException(f"Error occurred in python script name[{__file__}] line number[{sys._getframe().f_lineno}] error message[{str(e)}]", sys.exc_info())

    #     # Initialize configs and components
    #     training_pipeline_config = TrainingPipelineConfig()
    #     data_ingestion_config = DataIngestionConfig(training_pipeline_config)
    #     data_ingestion = DataIngestion(data_ingestion_config)
    #     logging.info("Initiating data ingestion...")
    #     data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
    #     logging.info("Data ingestion completed.")

    #     data_validation_config = DataValidationConfig(training_pipeline_config)
    #     data_validation = DataValidation(data_ingestion_artifact, data_validation_config)
    #     logging.info("Initiating data validation...")
    #     data_validation_artifact = data_validation.initiate_data_validation()
    #     logging.info("Data validation completed.")
        
    #     print(data_validation_artifact)

    # except Exception as e:
    #     raise NetworkSecurityException(e, sys)










