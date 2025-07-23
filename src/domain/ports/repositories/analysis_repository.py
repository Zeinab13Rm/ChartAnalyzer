from abc import ABC, abstractmethod
from src.domain.entities import ChartAnalysis

class AnalysisRepositoryPort(ABC):
    @abstractmethod
    def save(self, analysis: ChartAnalysis) -> None:
        pass