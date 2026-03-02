from Quality_of_Wine.config.configuration import ConfigurationManager
from Quality_of_Wine.components.data_ingestion import DataIngestion
from Quality_of_Wine import logger


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

"""

next from here to test the pipeline , it has to be mentioned in 
the main.py

"""