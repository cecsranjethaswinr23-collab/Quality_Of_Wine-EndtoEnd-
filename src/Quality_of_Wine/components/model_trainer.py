# required packages
import pandas as pd
import os
from Quality_of_Wine import logger
from Quality_of_Wine.entity.config_entity import ModelTrainerConfig
from sklearn.linear_model import ElasticNet
import joblib

# Model Trainer


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    """ 
    This is the primary method inside the ModelTrainer class.
        Action: It calls .fit() on the data.
        Output: Once training is finished, it uses joblib or your save_bin utility 
                to save the trained model as a .joblib or .pickle file in the artifacts/ folder.
       Logging: It usually logs that the model was saved successfully and at what path.
    """
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]


        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(train_x, train_y)

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))