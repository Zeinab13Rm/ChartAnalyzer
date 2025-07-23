from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class LLMProvider(str, Enum):
    HUGGINGFACE = "huggingface"
    OPENAI = "openai"
    LOCAL = "local"

class LLMRequestDTO(BaseModel):
    """Input for LLM analysis requests"""
    image_bytes: bytes = Field(..., description="Binary image data (PNG/JPEG)")
    question: str = Field(..., max_length=500, description="Question about the chart")
    provider: LLMProvider = Field(LLMProvider.HUGGINGFACE, description="LLM service provider")
    max_tokens: int = Field(300, gt=0, le=2000, description="Max response length")
    # temperature: float = Field(0.3, ge=0.1, le=1.0, description="Creativity control")

    class Config:
        json_encoders = {
            bytes: lambda v: v.decode('latin1')  # For base64 conversion
        }

class LLMResponseDTO(BaseModel):
    """Structured LLM output"""
    answer: str = Field(..., description="Generated analysis")
    model_used: str = Field(..., description="Model identifier")
    tokens_used: Optional[int] = Field(None, description="Token count")
    processing_time: Optional[float] = Field(None, description="Inference time in seconds")
    confidence: Optional[float] = Field(None, ge=0, le=1, description="Confidence score")
    raw_response: Optional[dict] = Field(None, description="Full API response")

    def to_api_response(self):
        return {
            "analysis": self.answer,
            "metadata": {
                "model": self.model_used,
                "tokens": self.tokens_used,
                "processing_time": self.processing_time
            }
        }