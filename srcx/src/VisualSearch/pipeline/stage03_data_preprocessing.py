from VisualSearch.config.configuration import ConfigurationManager
from VisualSearch.components.data_preprocessing import DataPreprocessing
from VisualSearch import logger

STAGE_NAME = "Data Preprocessing Stage"

class DataPreprocessingPipeline:
    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManager()
        data_preprocessing_config = config.get_data_preprocessing_config()
        data_preprocessing = DataPreprocessing(config=data_preprocessing_config)
        data_preprocessing.preprocess_all_data()

if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started")
        obj = DataPreprocessingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===========x")
    except Exception as e:
        logger.exception(e)
        raise e