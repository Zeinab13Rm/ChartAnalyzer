from abc import ABC, abstractmethod
from src.domain.entities.chart_image import ChartImage

class ChartsRepositoryPort(ABC):
    @abstractmethod
    def save(self, analysis: ChartImage) -> None:
        pass