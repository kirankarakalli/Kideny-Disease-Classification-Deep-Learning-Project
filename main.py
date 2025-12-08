from cnnclassifier import logger
from cnnclassifier.pipeline.Stage_01_data_ingestion import DataIngestionPipeline



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

