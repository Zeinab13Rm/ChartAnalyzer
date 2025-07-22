# src/application/services/auth.py
from datetime import datetime, timezone, timedelta
from jose import jwt
from passlib.context import CryptContext
from domain.ports import UserRepositoryPort 
from domain.entities.user import User
import uuid
from application.ports import AuthServicePort
from application.dtos.authentication import (
    RegisterRequest,
    LoginRequest,
    UserResponse,
    TokenResponse
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

    async def register(self, request: RegisterRequest) -> UserResponse:
        if await self._user_repo.get_by_email(request.email):
            raise ValueError("Email already registered")
        
        user = User(
            id=str(uuid.uuid4()),
            email=request.email,
            password_hash=self._hash_password(request.password)
        )
        await self._user_repo.create_user(user)
        return self._user_to_dto(user)

    async def login(self, request: LoginRequest) -> TokenResponse:
        user = await self._user_repo.get_by_email(request.email)
        if not user or not self._verify_password(request.password, user.password_hash):
            raise ValueError("Invalid credentials")
        
        return TokenResponse(
            access_token=self._create_access_token(user.email),
            token_type="bearer"
        )

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

    def _user_to_dto(self, user: User) -> UserResponse:
        return UserResponse(
            id=user.id,
            email=user.email,
            is_active=user.is_active
        )