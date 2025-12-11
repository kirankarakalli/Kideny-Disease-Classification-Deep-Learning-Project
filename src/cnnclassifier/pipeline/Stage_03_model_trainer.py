
from cnnclassifier.components.model_train import Training
from cnnclassifier.config.configuration import ConfigurationManager
from cnnclassifier import logger

class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config=ConfigurationManager()
        traing_config=config.get_training_config()
        training=Training(config=traing_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

STAGE_NAME='MODEL TRAINING PIPELINE'

if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
        obj=ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e