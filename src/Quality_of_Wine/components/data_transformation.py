import os
from Quality_of_Wine import logger
from Quality_of_Wine.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
import pandas as pd

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config


    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape," is the shape of the training data")
        print(test.shape," is the shape of the testing data")