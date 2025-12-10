

from cnnclassifier.components.model_train import Training
from cnnclassifier.config.configuration import ConfigurationManager


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