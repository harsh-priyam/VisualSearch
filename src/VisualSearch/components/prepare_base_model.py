import os
from VisualSearch import logger 
import joblib
import tensorflow as tf
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.applications.resnet50 import ResNet50
from VisualSearch.entity.config_entity import PrepareBaseModelConfig

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config
        
    
    def get_base_model(self):
        self.model = ResNet50(weights=self.config.params_weights,include_top=self.config.params_include_top,input_shape=self.config.params_image_size)

        self.model.trainable = False

        self.model = tf.keras.Sequential([
            self.model,
            GlobalMaxPooling2D()
        ])
    
        joblib.dump(self.model, os.path.join(self.config.root_dir, self.config.base_model))
