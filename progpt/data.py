# from datasets import load_dataset
from metaflow import FlowSpec, step

# from .utils import download_data_to_local

DATA_URL = ""


class DataFlow(FlowSpec):

    @step
    def start(self):
        # data_path = download_data_to_local(DATA_URL)
        pass

    def is_new_data(self):
        pass

    def preprocessing(self):
        pass

    def tokenization(self):
        pass

    def postprocessing(self):
        pass

    @step
    def end(self): pass
