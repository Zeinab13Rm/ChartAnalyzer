from fastapi import APIRouter, UploadFile, File, Depends
from src.application.services.analyze_service import AnalyzeService
from src.dependencies import get_upload_use_case

router = APIRouter()

@router.post("/analyze")
async def analyze_chart(
    file: UploadFile = File(...),
    service: AnalyzeService  = Depends(get_upload_use_case)
) -> dict:
    image_bytes = await file.read()
    image_id = service.execute(image_bytes, "user123")
    return {"image_id": image_id}