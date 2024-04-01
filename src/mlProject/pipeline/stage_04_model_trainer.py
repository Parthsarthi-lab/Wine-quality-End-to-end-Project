from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer
from mlProject import logger

STAGE_NAME = "Model training stage"

class ModelTrainerPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        """Initialize the pipeline stepwise"""

        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()

if __name__ == "__main__":
    try:
          logger.info(f">>>>> stage {STAGE_NAME} started <<<<")
          obj = ModelTrainerPipeline()
          obj.main()
          logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<")
    except Exception as e:
          logger.exception(e)
          raise e