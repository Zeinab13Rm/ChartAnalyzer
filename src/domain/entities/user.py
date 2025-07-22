# src/domain/entities/user.py
from datetime import datetime, timezone, timedelta
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class User(BaseModel):
        
    id: str  # UUID
    email: EmailStr
    password_hash: str  # Always hashed, never plaintext
    is_active: bool = True
    created_at: datetime = datetime.now(timezone.utc)
    last_login: Optional[datetime] = None

