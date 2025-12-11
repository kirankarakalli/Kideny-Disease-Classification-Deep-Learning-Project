
from cnnclassifier.components.evaluation import Evaluation
from cnnclassifier.config.configuration import ConfigurationManager


class EvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config=ConfigurationManager()
        eval_config=config.get_eval_config()
        eval=Evaluation(eval_config)
        eval.evaluation()
        eval.log_into_mlflow()
        eval.save_score()