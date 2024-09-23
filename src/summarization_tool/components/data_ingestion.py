
import os 
import zipfile 
from urllib.request import urlretrieve
from summarization_tool.utils.common import get_size
from summarization_tool.logging import logger
from pathlib import Path
from summarization_tool.entity import DataIngestionConfig
from summarization_tool.constants import *

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  

           
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)