# import sys
# from networksecurity.components.data_ingestion import DataIngestion
# from networksecurity.exception.exception import NetworkSecurityException
# from networksecurity.logging.logger import logging
# from networksecurity.entity.config_entity import DataIngestionConfig
# from networksecurity.entity.config_entity import TrainingPipelineConfig

# if __name__=='__main__':
#     try:
#         training_pipeline_config = TrainingPipelineConfig()
#         DataingestionConfig=DataIngestionConfig(training_pipeline_config)
#         data_ingestion=DataIngestion(DataingestionConfig)
#         logging.info("Initate the data ingestion")
#         dataingestionartifact=data_ingestion.initiate_data_ingestion()
#         print(dataingestionartifact)


#     except Exception as e:
#         raise NetworkSecurityException(e, sys)



import sys
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

if __name__ == '__main__':
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        
        logging.info("Initiating the data ingestion process.")
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        print(data_ingestion_artifact)

    except Exception as e:
        logging.error(f"Error occurred in python script name[{__file__}] line number[{sys.exc_info()[2].tb_lineno}] error message: {str(e)}")
        raise NetworkSecurityException(e, sys)













