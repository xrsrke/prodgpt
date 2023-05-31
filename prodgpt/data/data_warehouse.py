import uuid as uid
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional

from sqlalchemy import Boolean, Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class DataBatch(Base):
    __tablename__ = "training_data_batch"

    uuid = Column(String(36), primary_key=True)
    name = Column(String(200), nullable=False)
    desc = Column(String(1000), nullable=True)
    created_at = Column(String, default=datetime.now().isoformat())
    updated_at = Column(String, default=datetime.now().isoformat())
    deleted_at = Column(String, nullable=True)
    is_deleted = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"DataBatch(uuid={self.uuid}, name={self.name}"


class TrainingText(Base):
    __tablename__ = "training_text"

    uuid = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uid.uuid4())
    )
    # batch_id = Column(String(36), ForeignKey("training_data_batch.uid"))
    text = Column(String(3000000), nullable=False)
    created_at = Column(String, default=datetime.now().isoformat())
    updated_at = Column(
        String,
        default=datetime.now().isoformat(),
        onupdate=datetime.now().isoformat()
    )
    deleted_at = Column(String, nullable=True)
    is_deleted = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"Text(uuid={self.uuid})"


class BaseDataWarehouse(ABC):
    @abstractmethod
    def insert(self):
        raise NotImplementedError

    @abstractmethod
    def extract_from_uuid(self):
        raise NotImplementedError

    @abstractmethod
    def delete_from_uuid(self):
        raise NotImplementedError


class DataWarehouse(BaseDataWarehouse):
    def __init__(self, config) -> None:
        project_id = config["gcloud_data_warehouse"]["project_id"]
        dataset_id = config["gcloud_data_warehouse"]["dataset_id"]
        engine = create_engine(f"bigquery://{project_id}/{dataset_id}")

        self.Session = sessionmaker(bind=engine)

    @property
    def session(self) -> sessionmaker:
        return self.Session()

    def insert(self, data: List[TrainingText]) -> Optional[bool]:
        session = self.Session()
        try:
            session.add_all(data)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            raise e

    def extract_from_uuid(self, uuids: List[uid.UUID]) -> List[TrainingText]:
        session = self.Session()
        try:
            data = session.query(TrainingText).filter(
                TrainingText.uuid.in_(uuids)
            ).all()
            return data
        except Exception as e:
            session.rollback()
            raise e

    def delete_from_uuid(self, data_ids: List[uid.UUID]) -> Optional[bool]:
        session = self.Session()
        try:
            session.query(TrainingText).filter(
                TrainingText.uuid.in_(data_ids)
            ).delete(synchronize_session=False)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            raise e
