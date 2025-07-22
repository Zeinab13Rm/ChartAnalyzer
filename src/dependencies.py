from fastapi import Depends
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from application.services import AuthService
from domain.ports import UserRepositoryPort
from infrastructure.adapters.sqlserver.sql_user_repository import SqlUserRepository
from config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


def get_user_repository(session: AsyncSession = Depends(get_db_session)) -> UserRepositoryPort:
    return SqlUserRepository(session)

def get_auth_service(
    user_repo: UserRepositoryPort = Depends(get_user_repository),
) -> AuthService:
    return AuthService(
        user_repo=user_repo,
        secret_key=settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM,
        expires_minutes=settings.JWT_EXPIRE_MINUTES,
    )