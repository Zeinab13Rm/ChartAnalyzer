# infrastructure/api/adapters/analysis_adapter.py
from fastapi import UploadFile
from application.services.analyze_service import AnalyzeService
from application.dtos.analysis import AnalysisRequestDTO, AnalysisResponseDTO

class FastAPIAnalysisAdapter:
    """Adapter to convert FastAPI-specific types to our DTOs"""
    
    @staticmethod
    async def to_request_dto(
        image: UploadFile, 
        question: str
    ) -> AnalysisRequestDTO:
        """Convert FastAPI UploadFile to our DTO"""
        return AnalysisRequestDTO(
            image_bytes=await image.read(),
            question=question
        )
    
    @staticmethod
    def to_api_response(response_dto: AnalysisResponseDTO) -> dict:
        """Convert our DTO to API response format"""
        return {
            "analysis_id": response_dto.analysis_id,
            "answer": response_dto.answer
        }