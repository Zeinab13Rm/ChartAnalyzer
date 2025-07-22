from abc import ABC, abstractmethod
from domain.entities import ChartImage

class ChartsRepositoryPort(ABC):
    @abstractmethod
    def save(self, analysis: ChartImage) -> None:
        pass