
from abc import ABC, abstractmethod
from src.domain.entities.user import User
from src.application.dtos.authentication import (
    RegisterRequestDTO,
    LoginRequestDTO,
    UserResponseDTO,
    TokenResponseDTO
)

class AuthServicePort(ABC):
    @abstractmethod
    async def register(self, email, password) -> User: ...
    
    @abstractmethod
    async def login(self, email, password) -> str: ...