from fastapi import APIRouter, Depends, HTTPException, status
from src.application.dtos.authentication import RegisterRequestDTO, LoginRequestDTO, TokenResponseDTO
from src.application.ports.authentication_service_port import AuthServicePort
from src.dependencies import get_auth_service

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