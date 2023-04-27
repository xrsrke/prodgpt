from abc import abstractclassmethod

from .data_warehouse import DataWarehouse


class BaseExtractor:
    """Base class for all extractors."""
    def __init__(self):
        self.data_warehouse = DataWarehouse()

    @abstractclassmethod
    def extract(self):
        """Extract data from the data warehouse."""
        raise NotImplementedError


class RandomExtractor(BaseExtractor):
    """Randomly extract data from the data warehouse."""
    pass
