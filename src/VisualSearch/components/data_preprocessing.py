import tensorflow 
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50,preprocess_input	
import numpy as np
from numpy.linalg import norm
import os 
from tqdm import tqdm
import joblib
from VisualSearch.entity.config_entity import DataPreprocessingConfig


class DataPreprocessing:
    def __init__(self, config: DataPreprocessingConfig):
        self.config = config
        self.model = joblib.load(self.config.model_path)
        self.file_names = []
        self.feature_list = []

    def get_data_preprocess(self,path):

        img = image.load_img(path,target_size=self.config.params_target_size, color_mode="rgb")
        img_array = image.img_to_array(img)
        expanded_img_array = np.expand_dims(img_array, axis=0)
        preprocessed_img = preprocess_input(expanded_img_array)
        result = self.model.predict(preprocessed_img).flatten()
        normalized_result = result / norm(result)

        return normalized_result

    def preprocess_all_data(self):
        for file in os.listdir(self.config.data_path):
            self.file_names.append(os.path.join(self.config.data_path, file))

        for file in tqdm(self.file_names):
            self.feature_list.append(self.get_data_preprocess(file))

        joblib.dump(self.file_names,os.path.join(self.config.root_dir,self.config.file_names))
        joblib.dump(self.feature_list,os.path.join(self.config.root_dir,self.config.feature_list))


