from fastapi import Depends
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from src.application.services.authentication_service import AuthService
from src.application.use_cases.upload_chart import UploadChartUseCase
from src.domain.ports.repositories.user_repository import UserRepositoryPort
from src.domain.ports.repositories.charts_repository import ChartsRepositoryPort
from src.infrastructure.adapters.sqlserver.sql_user_repository import SqlUserRepository
from src.infrastructure.adapters.sqlserver.sql_charts_repository import SqlChartsRepository
from src.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


def get_user_repository(session: AsyncSession = Depends(get_db_session)) -> UserRepositoryPort:
    return SqlUserRepository(session)

def get_charts_repository(session: AsyncSession = Depends(get_db_session)) -> ChartsRepositoryPort:
    return SqlChartsRepository(session)

def get_auth_service(
    user_repo: UserRepositoryPort = Depends(get_user_repository),
) -> AuthService:
    return AuthService(
        user_repo=user_repo,
        secret_key=settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM,
        expires_minutes=settings.JWT_EXPIRE_MINUTES,
    )

def get_upload_use_case(charts_repo: ChartsRepositoryPort = Depends(get_charts_repository)) -> UploadChartUseCase:
    return UploadChartUseCase(charts_repo)