# src/infrastructure/api/fastapi/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from application.dtos.authentication import RegisterRequest, LoginRequest, TokenResponse, UserResponse
from application.services import AuthService
from dependencies import get_auth_service

router = APIRouter(tags=["auth"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(
    request: RegisterRequest,
    auth_service: AuthService = Depends(get_auth_service),
):
    try:
        return await auth_service.register(request)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/login", response_model=TokenResponse)
async def login(
    request: LoginRequest,
    auth_service: AuthService = Depends(get_auth_service),
):
    try:
        return await auth_service.login(request)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )