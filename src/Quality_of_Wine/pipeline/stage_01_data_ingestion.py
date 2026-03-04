from Quality_of_Wine.config.configuration import ConfigurationManager
from Quality_of_Wine.components.data_ingestion import DataIngestion
from Quality_of_Wine import logger


STAGE_NAME="Data Ingestion Stage"       # ***these are the 
                                        #    code that must
class DataIngestionTrainingPipeline:    #    be written
    def __init__(self):                 #    before giving
        pass                            #    pipeline codes***
    
    #pipeline code
    def main(self):                     #this function initializes the download and extraction of zip file
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

"""
this is the where code is actually(pipeline) is initaited

"""
if __name__ == '__main__':
    try:
        logger.info(f">>>>stage {STAGE_NAME} started<<<<")
        obj=DataIngestionTrainingPipeline()  #the process gets initialized and a vaiable is created
        obj.main()
        logger.info((f">>>>stage {STAGE_NAME} completed<<<<"))
    except Exception as e:
        logger.excpetion(e)

"""
To execute the function, it has to be mentioned in 
the main.py

"""