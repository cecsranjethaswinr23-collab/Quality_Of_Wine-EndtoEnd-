from Quality_of_Wine.config.configuration import ConfigurationManager
from Quality_of_Wine.components.data_validation import DataValiadtion
from Quality_of_Wine import logger


STAGE_NAME = "Data Validation stage"         #***these are the
                                             #   code to be 
class DataValidationTrainingPipeline:        #   written before
    def __init__(self):                      #   pipeline
        pass                                 #   coding***

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()





if __name__ == '__main__':
    try:
        logger.info(f">>>>stage {STAGE_NAME} started<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>stage {STAGE_NAME} completed <<<<")
    except Exception as e:
        logger.exception(e)
        raise e