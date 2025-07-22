from pydantic import BaseModel

class AnalysisRequestDTO(BaseModel):
    image_bytes: bytes  # Or UploadFile for FastAPI
    question: str

class AnalysisResponseDTO(BaseModel):
    answer: str
    analysis_id: str