# src/infrastructure/adapters/sql_user_repository.py
from sqlalchemy import select
from src.domain.ports import UserRepositoryPort
from src.domain.entities.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import EmailStr

class SqlUserRepository(UserRepositoryPort):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_email(self, email: EmailStr) -> User | None:
        result = await self._session.execute(
            select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def create_user(self, user: User) -> None:
        self._session.add(user)
        await self._session.commit()