from cnnclassifier import logger
from cnnclassifier.pipeline.Stage_01_data_ingestion import DataIngestionPipeline
from cnnclassifier.pipeline.Stage_02_prepare_base_model import PrepareBaseModelPipeline
from cnnclassifier.pipeline.Stage_03_model_trainer import ModelTrainingPipeline



STAGE_NAME='DATA INGESTION PIPELINE'

if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME='PREPARE BASE MODEL PIPELINE'

if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
        obj=PrepareBaseModelPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
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