from Quality_of_Wine.config.configuration import ConfigurationManager
from Quality_of_Wine.components.model_evaluation import ModelEvaluation
from Quality_of_Wine import logger

STAGE_NAME = "Model evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    # only the contents inside are the pipeline
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<")
    except Exception as e:
        logger.exception(e)
        raise e

