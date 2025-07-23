# src/application/services/auth.py
from datetime import datetime, timezone, timedelta
from jose import jwt
from passlib.context import CryptContext
from src.domain.ports.repositories.user_repository import UserRepositoryPort
from src.domain.entities.user import User
import uuid
from src.application.ports.authentication_service_port import AuthServicePort
from src.application.dtos.authentication import (
    RegisterRequestDTO,
    LoginRequestDTO,
    UserResponseDTO,
    TokenResponseDTO
)

class AuthService(AuthServicePort):
    def __init__(
        self,
        user_repo: UserRepositoryPort,
        secret_key: str,
        algorithm: str = "HS256",
        expires_minutes: int = 30
    ):
        self._user_repo = user_repo
        self._secret_key = secret_key
        self._algorithm = algorithm
        self._expires_minutes = expires_minutes
        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def register(self, email, password) -> User:
        if await self._user_repo.get_by_email(email):
            raise ValueError("Email already registered")
        
        user = User(
            id=str(uuid.uuid4()),
            email=email,
            password_hash=self._hash_password(password)
        )
        await self._user_repo.create_user(user)
        return user

    async def login(self, email, password) -> str:
        user = await self._user_repo.get_by_email(email)
        if not user or not self._verify_password(password, user.password_hash):
            raise ValueError("Invalid credentials")
        
        return self._create_access_token(user.email)

    def _hash_password(self, password: str) -> str:
        return self._pwd_context.hash(password)

    def _verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self._pwd_context.verify(plain_password, hashed_password)

    def _create_access_token(self, email: str) -> str:
        expires = datetime.now(timezone.utc) + timedelta(minutes=self._expires_minutes)
        return jwt.encode(
            {"sub": email, "exp": expires},
            self._secret_key,
            algorithm=self._algorithm
        )

    def _user_to_dto(self, user: User) -> UserResponseDTO:
        return UserResponseDTO(
            id=user.id,
            email=user.email,
            is_active=user.is_active
        )