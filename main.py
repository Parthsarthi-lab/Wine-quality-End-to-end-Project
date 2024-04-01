from mlProject import logger # Though logger is inside mlProject folder, we need not to write src.mlProject because we wrote the logging code inside the __init__.py
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainigPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<")
    data_ingestion = DataIngestionTrainigPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)


STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)

STAGE_NAME = "Model Training stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)