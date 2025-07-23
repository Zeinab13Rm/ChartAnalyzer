# domain/ports/llm_service_port.py
from abc import ABC, abstractmethod
from dataclasses import dataclass
from dtos.LLM import LLMResponseDTO, LLMRequestDTO

class LLMServicePort(ABC):
    """Port/Interface for LLM services"""
    
    @abstractmethod
    async def analyze_chart(self, request: LLMRequestDTO) -> LLMResponseDTO:
        """
        Analyze a chart image with a given question
        
        Args:
            image_data: Binary image data
            question: Natural language question about the chart
            kwargs: Additional model-specific parameters
            
        Returns:
            LLMResponse: Structured response from the LLM
        """
        raise NotImplementedError