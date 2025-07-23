from fastapi import APIRouter, Form, UploadFile, File, Depends
from src.application.services.analyze_service import AnalyzeService
from src.dependencies import get_upload_use_case
from src.application.dtos.LLM import LLMResponseDTO, LLMRequestDTO
from src.application.ports.llm_service_port import LLMServicePort
from src.dependencies import get_llm_service


router = APIRouter(tags=["charts"])


@router.post("/ask", response_model=LLMResponseDTO)
async def ask_about_chart(
    image: UploadFile = File(...),
    question: str = Form(...),
    llm_service: LLMServicePort = Depends(get_llm_service)
):
    request = LLMRequestDTO(
        image_bytes=await image.read(),
        question=question
    )
    return await llm_service.analyze(request)



@router.post("/analyze", response_model=LLMResponseDTO)
async def analyze_chart(
    image: UploadFile = File(...),
    # question: str = Form(...),
    llm_service: LLMServicePort = Depends(get_llm_service)
):
    request = LLMRequestDTO(
        image_bytes=await image.read(),
        question="analyze the trends showing in this chart"
    )
    return await llm_service.analyze(request)