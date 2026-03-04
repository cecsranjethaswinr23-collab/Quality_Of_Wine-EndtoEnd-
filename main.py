# also can be written as from src.Quality of Wine import 
# logging(that is why -e. is used for not using the from src.Quality of Wine import logging)
from Quality_of_Wine import logger

#these imports is after the updation of the stage_01_data_ingestion.py with pipeline codes
from Quality_of_Wine.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Quality_of_Wine.config.configuration import ConfigurationManager
from Quality_of_Wine.components.data_ingestion import DataIngestion


"""     Actual Data Ingestion pipeline     """
# NOTES
"""     artifacts must be deleted before executing the main.py pipelines    """

STAGE_NAME="Data Ingestion Stage"

class DataIngestionTrainingPipeline: 
    def __init__(self):
        pass

    def main(self): #this function initializes the donload and extraction of zip file
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f">>>>stage {STAGE_NAME} started<<<<")
        obj=DataIngestionTrainingPipeline()  #the process gets initialized and a vaiable is created
        obj.main()
        logger.info((f">>>>stage {STAGE_NAME} completed<<<<"))
    except Exception as e:
        logger.excpetion(e)