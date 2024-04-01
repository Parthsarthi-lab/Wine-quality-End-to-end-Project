from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidation
from mlProject import logger

STAGE_NAME = "Data Validation stage"

class DataValidationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        """Initializes the pipeline stepwise"""
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__ =="__main__":
    try:
          logger.info(f">>>>> stage {STAGE_NAME} started <<<<")
          obj = DataValidationPipeline()
          obj.main()
          logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<")
    except Exception as e:
          logger.exception(e)
          raise e