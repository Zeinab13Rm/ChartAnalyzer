
from abc import ABC, abstractmethod
from domain.entities.user import User
from application.dtos.authentication import (
    RegisterRequest,
    LoginRequest,
    UserResponse,
    TokenResponse
)


# src/domain/ports/auth_service.py
class AuthServicePort(ABC):
    @abstractmethod
    async def register(self, request: RegisterRequest) -> UserResponse: ...
    
    @abstractmethod
    async def login(self, request: LoginRequest) -> TokenResponse:  # Returns JWT
        ...