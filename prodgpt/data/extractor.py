from abc import abstractclassmethod

from .data_warehouse import DataWarehouse, DataWarehouseBase


class BaseExtractor:
    """Base class for all extractors."""
    def __init__(self, data_warehouse: DataWarehouseBase):
        self.data_warehouse = DataWarehouse()

    @abstractclassmethod
    def extract(self):
        """Extract data from the data warehouse."""
        raise NotImplementedError


class RandomExtractor(BaseExtractor):
    """Randomly extract data from the data warehouse."""
    pass
