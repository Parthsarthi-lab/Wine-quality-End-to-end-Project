from mlProject import logger # Though logger is inside mlProject folder, we need not to write src.mlProject because we wrote the logging code inside the __init__.py
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainigPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<")
    obj = DataIngestionTrainigPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e