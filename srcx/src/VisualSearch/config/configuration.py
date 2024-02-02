from VisualSearch.constants import *
from VisualSearch.utils.common import read_yaml, create_directories
from VisualSearch.entity.config_entity import (DataIngestionConfig,PrepareBaseModelConfig,DataPreprocessingConfig)

class ConfigurationManager:
      def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH,
            schema_filepath = SCHEMA_FILE_PATH):
        
            self.config = read_yaml(config_filepath)
            self.params = read_yaml(params_filepath)
            self.schema = read_yaml(schema_filepath)

            create_directories([self.config.artifacts_root])

      def get_data_ingestion_config(self) -> DataIngestionConfig:
          config = self.config.data_ingestion 

          create_directories([config.root_dir])

          data_ingestion_config = DataIngestionConfig(
                root_dir=config.root_dir,
                source_URL=config.source_URL,
                local_data_file=config.local_data_file,
                unzip_dir=config.unzip_dir
          )       

          return data_ingestion_config
      
      def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
          config = self.config.prepare_base_model

          create_directories([config.root_dir])

          prepare_base_model_config = PrepareBaseModelConfig(
                root_dir = config.root_dir,
                data_path=config.data_path,
                params_weights=self.params.WEIGHTS,
                params_image_size=self.params.INPUT_SHAPE,
                params_include_top=self.params.INCLUDE_TOP,
                base_model = config.base_model
          )

          return prepare_base_model_config   
      
      def get_data_preprocessing_config(self) -> DataPreprocessingConfig:
        config = self.config.data_preprocessing 
        create_directories([config.root_dir])

        data_preprocessing_config = DataPreprocessingConfig(
             root_dir=config.root_dir,
             data_path=config.data_path,
             model_path=config.model_path,
             feature_list=config.feature_list,
             file_names=config.file_names,
             params_target_size=self.params.TARGET_SIZE
        )

        return data_preprocessing_config