from summarization_tool.config.configuration import ConfigurationManager
from summarization_tool.components.data_validation import DataValidation
from summarization_tool.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()
