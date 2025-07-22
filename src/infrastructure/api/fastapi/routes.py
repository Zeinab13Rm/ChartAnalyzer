from fastapi import APIRouter, UploadFile, File, Depends
from application.use_cases.upload_chart import UploadChartUseCase

from fastapi import APIRouter, Depends, HTTPException, status
from application.dtos import RegisterRequestDTO, LoginRequestDTO, TokenResponseDTO
from application.ports import AuthServicePort
from dependencies import get_auth_service, get_upload_use_case
router = APIRouter(tags=["auth"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    request: RegisterRequestDTO,
    auth_service: AuthServicePort = Depends(get_auth_service)
):
    try:
        user = await auth_service.register(request.email, request.password)
        return {"id": user.id, "email": user.email}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=TokenResponseDTO)
async def login(
    request: LoginRequestDTO,
    auth_service: AuthServicePort = Depends(get_auth_service)
):
    try:
        token = await auth_service.login(request.email, request.password)
        return {"access_token": token, "token_type": "bearer"}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.post("/upload")
async def upload_chart(
    file: UploadFile = File(...),
    use_case: UploadChartUseCase = Depends(get_upload_use_case)
) -> dict:
    image_bytes = await file.read()
    image_id = use_case.execute(image_bytes, "user123")  # Replace with real user ID
    return {"image_id": image_id}