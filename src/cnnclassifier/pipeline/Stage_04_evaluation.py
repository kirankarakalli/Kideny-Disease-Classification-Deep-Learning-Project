
from cnnclassifier.components.evaluation import Evaluation
from cnnclassifier.config.configuration import ConfigurationManager
from cnnclassifier import logger

class EvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config=ConfigurationManager()
        eval_config=config.get_eval_config()
        eval=Evaluation(eval_config)
        eval.evaluation()
        #eval.log_into_mlflow()
        eval.save_score()

STAGE_NAME='MODEL EVAL PIPELINE'
if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
        obj=EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    