# application/services/llm_service.py
from src.application.dtos.LLM import LLMRequestDTO, LLMResponseDTO
from src.application.dtos.error import LLMErrorDTO

class LLMService:
    async def analyze(self, request: LLMRequestDTO) -> LLMResponseDTO:
        try:
            # ... implementation ...
            return LLMResponseDTO(
                answer="The chart shows...",
                model_used="chartgemma",
                tokens_used=150,
                processing_time=2.3
            )
        except Exception as e:
            raise LLMErrorDTO.from_exception(e)