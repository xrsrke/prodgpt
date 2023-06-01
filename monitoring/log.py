from pymongo import MongoClient
from schema import InferenceLog


def send_inference_log_to_mongo(log: InferenceLog):
    client = MongoClient("mongodb://localhost:27018")
    database = client.get_database('monitoring')
    collection = database.get_collection('inference_logs')
    collection.insert_one(log)
