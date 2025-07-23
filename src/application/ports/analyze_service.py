# application/ports/analysis_service_port.py
from abc import ABC, abstractmethod
from src.application.dtos.analysis import AnalysisRequestDTO, AnalysisResponseDTO

class AnalysisServicePort(ABC):
    """Port/Interface for the analysis service"""
    
    @abstractmethod
    async def analyze(self, request: AnalysisRequestDTO) -> AnalysisResponseDTO:
        """Analyze a chart image with a given question"""
        raise NotImplementedError