from typing import List

import pandas as pd
from evidently.metric_preset import DataDriftPreset
from evidently.report import Report
from pydantic import BaseModel
from pymongo import MongoClient
from schema import InferenceLog

MONGO_URL = "mongodb://localhost:27018"


def send_inference_log_to_mongo(log: InferenceLog):
    client = MongoClient(MONGO_URL)
    database = client.get_database('monitoring')
    collection = database.get_collection('inference_logs')
    collection.insert_one(log)


class TextData(BaseModel):
    input: str
    output: str


class DistributionDrift:
    def __init__(self, window_length: int):
        self.window_length = window_length

    def _extract_current_data(self) -> List[TextData]:
        EXCLUDE_COLUMNS = {"_id": 0, "model_id": 0, "user_id": 0}

        client = MongoClient(MONGO_URL)
        database = client.get_database('monitoring')
        collection = database.get_collection('inference_logs')
        results = collection.find({}, EXCLUDE_COLUMNS)\
                            .sort('timestamp', -1)\
                            .limit(self.window_length)
        return results

    def _extract_reference_data(self) -> List[TextData]:
        pass

    def _send_result_to_mongo(self, result: dict):
        client = MongoClient(MONGO_URL)
        database = client.get_database('monitoring')
        collection = database.get_collection('report')
        collection.insert_one(result)

    def compute(self):
        current_data = pd.DataFrame(data=self._extract_current_data())
        # reference_data = pd.DataFrame(data=self._extract_reference_data())
        reference_data = current_data

        report = Report(metrics=[
            DataDriftPreset()
        ])
        report.run(current_data=current_data, reference_data=reference_data)
        report = report.as_dict()

        self._send_result_to_mongo(report)


DistributionDrift(window_length=100).compute()
