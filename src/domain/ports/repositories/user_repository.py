from abc import ABC, abstractmethod
from domain.entities.user import User

class UserRepositoryPort(ABC):
    @abstractmethod
    async def get_by_email(self, email: str) -> User | None: ...
    
    @abstractmethod
    async def create_user(self, user: User) -> None: ...
