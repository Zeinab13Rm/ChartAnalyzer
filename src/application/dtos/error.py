from pydantic import BaseModel
from typing import Optional

class LLMErrorDTO(BaseModel):
    """Standardized error response"""
    error_type: str
    message: str
    provider: str
    suggestion: Optional[str] = None

    @classmethod
    def from_exception(cls, exc: Exception):
        return cls(
            error_type=exc.__class__.__name__,
            message=str(exc),
            provider="chartgemma",
            suggestion="Try reducing image size or question length"
        )