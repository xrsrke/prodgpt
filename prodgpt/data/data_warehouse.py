import uuid as uid
from datetime import datetime
from typing import List

from google.cloud import bigquery
from pydantic import BaseModel, root_validator

# from sqlalchemy import Column, String, DateTime, Boolean
# from sqlalchemy.ext.declarative import declarative_base


# Base = declarative_base()


class TrainingText(BaseModel):
    uuid: str
    text: str
    created_at: str = datetime.now().isoformat()
    updated_at: str = None
    deleted_at: str = None
    is_deleted: bool = False

    @root_validator(pre=True)
    def generate_uuid(cls, values):
        values["uuid"] = str(uid.uuid4())
        return values


# class DataBatch(Base):
#     __tablename__ = "training_data_batch"
#     uuid = Column(String(36), primary_key=True)


# class TrainingText(Base):
#     __tablename__ = "training_text"
#     uuid = Column(String(36), primary_key=True)
#     # batch_id = Column(String(36), ForeignKey("training_data_batch.uid"))
#     text = Column(String(3000000), nullable=False)
#     created_at = Column(DateTime, default=datetime.now())
#     updated_at = Column(
#         DateTime,
#         default=datetime.now(),
#         onupdate=datetime.now()
#     )
#     deleted_at = Column(DateTime, nullable=True)
#     is_deleted = Column(Boolean, default=False)

#     def __repr__(self) -> str:
#         return f"Text(uuid={self.uuid})"


class DataWarehouse:
    def __init__(self, config) -> None:
        client = bigquery.Client()

        project_id = config["gcloud_data_warehouse"]["project_id"]
        dataset_id = config["gcloud_data_warehouse"]["dataset_id"]
        table_id = config["gcloud_data_warehouse"]["table_id"]
        table_name = f"{project_id}.{dataset_id}.{table_id}"

        self.client = client
        self.table = client.get_table(table_name)
        self.table_name = table_name
        self.config = config

    def insert(self, data: List[TrainingText]) -> bool:
        dict_data = [x.dict() for x in data]
        output = self.client.insert_rows_json(self.table, dict_data)

        if output == []:
            return True
        else:
            return False

    def extract_from_uuid(self, uuids: List[uid.UUID]):
        str_uuids = ', '.join(f"'{id_}'" for id_ in uuids)
        query = f"SELECT * FROM {self.table_name} WHERE uuid IN ({str_uuids})"
        return self.client.query(query)

    def delete(self, data_ids: List[uid.UUID]):
        query = f"UPDATE {self.table_name}\
            SET is_deleted = True WHERE uuid IN ({data_ids})"
        return self.client.query(query)
