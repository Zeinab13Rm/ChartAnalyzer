from fastapi import APIRouter, UploadFile, File, Depends
from src.application.use_cases.upload_chart import UploadChartUseCase
from src.dependencies import get_upload_use_case

router = APIRouter()

@router.post("/upload")
async def upload_chart(
    file: UploadFile = File(...),
    use_case: UploadChartUseCase = Depends(get_upload_use_case)
) -> dict:
    image_bytes = await file.read()
    image_id = use_case.execute(image_bytes, "user123")
    return {"image_id": image_id}