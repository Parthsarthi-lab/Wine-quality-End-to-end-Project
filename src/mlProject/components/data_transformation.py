import os
from mlProject import logger
from sklearn.model_selection import train_test_split
from mlProject.entity.config_entity import DataTransformationConfig
import pandas as pd


# Data transformation will include all transformation techniques such as categorical encoding, scaling of features, gaussian transformation, pca & lda etc , i.e., all kinds of transformations
# We are only doing train_test_split as the data is already clean and the objective of the project is to showcase model deployment with mlflow

class DataTransformation:
    def __init__(self, config: DataTransformationConfig) -> None:
        self.config = config

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        train,test = train_test_split(data)

        # Train and test data will be saved in data transformation folder 
        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

        logger.info("Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
