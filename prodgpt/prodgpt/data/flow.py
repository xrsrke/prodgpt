# from datasets import load_dataset
from metaflow import FlowSpec, step

from .utils import download_data_to_local

DATA_URL = ""


class DataFlow(FlowSpec):
    @step
    def start(self):
        self.next(self.download_new_data)

    @step
    def download_new_data(self):
        self.data_path = download_data_to_local(DATA_URL)
        self.next(self.preprocessing)

    @step
    def preprocessing(self):
        pass

    @step
    def tokenization(self):
        pass

    @step
    def postprocessing(self):
        pass

    @step
    def end(self): pass
