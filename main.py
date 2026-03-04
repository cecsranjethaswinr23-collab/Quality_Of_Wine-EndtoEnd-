# also can be written as from src.Quality of Wine import 
# logging(that is why -e. is used for not using the from src.Quality of Wine import logging)
from Quality_of_Wine import logger

#these imports is after the updation of the stage_01_data_ingestion.py with pipeline codes
from Quality_of_Wine.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Quality_of_Wine.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

from Quality_of_Wine.config.configuration import ConfigurationManager
from Quality_of_Wine.components.data_ingestion import DataIngestion


"""     Actual Data Ingestion pipeline     """
# NOTES
"""     artifacts must be deleted before executing the main.py pipelines    """

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>> stage {STAGE_NAME} started <<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>> stage {STAGE_NAME} completed <<<<")
except Exception as e:
        logger.exception(e)
        raise e



"""     Actual Data Validation pipeline     """

# NOTES
"""     artifacts must be deleted before executing the main.py pipelines    """

STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>> stage {STAGE_NAME} started <<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>> stage {STAGE_NAME} completed <<<<")
except Exception as e:
        logger.exception(e)
        raise e