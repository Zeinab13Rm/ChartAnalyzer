# src/application/dtos/auth.py
from pydantic import BaseModel, EmailStr

class RegisterRequestDTO(BaseModel):
    email: EmailStr
    password: str

class LoginRequestDTO(BaseModel):
    email: EmailStr
    password: str

class UserResponseDTO(BaseModel):
    id: str
    email: str
    is_active: bool

class TokenResponseDTO(BaseModel):
    access_token: str
    token_type: str = "bearer"