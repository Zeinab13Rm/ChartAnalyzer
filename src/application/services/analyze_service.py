# application/services/analysis_service.py
from src.application.ports.analyze_service import AnalysisServicePort
from src.application.dtos.analysis import AnalysisRequestDTO, AnalysisResponseDTO
# from domain.ports.image_processor import IImageProcessor  # Domain interface
from src.application.ports.llm_service_port import LLMServicePort  # Domain interface
import uuid

class AnalyzeService(AnalysisServicePort):
    """Concrete implementation of the analysis service"""
    
    def __init__(self, 
                 llm_service: LLMServicePort
                 #image_processor: IImageProcessor
                    ):
        self.llm_service = llm_service
        # self.image_processor = image_processor
    
    async def analyze(self, request: AnalysisRequestDTO) -> AnalysisResponseDTO:
        """Process the analysis request"""
        
        # 1. Validate and preprocess image
        # processed_image = await self.image_processor.process(request.image_bytes)
        
        # 2. Prepare LLM prompt
        prompt = self._build_prompt(
            image_data=request.image_bytes,
            question=request.question
        )
        
        # 3. Call LLM service
        llm_response = await self.llm_service.analyze(prompt)
        
        # 4. Return formatted response
        return AnalysisResponseDTO(
            answer=llm_response.answer,
            analysis_id=str(uuid.uuid4())  # Generate unique ID
        )
    
    def _build_prompt(self, image_data: bytes, question: str) -> str:
        """Construct the prompt for the LLM"""
        return (
            f"You are a data analysis expert. Analyze this chart and "
            f"answer the following question: {question}\n"
            f"Chart data: {image_data}"
        )