from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional


class UserBase(BaseModel):
    """Schema base con atributos comunes"""

    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Nombre del usuario"
    )

    email: EmailStr = Field(
        ...,
        description="Correo electrónico"
    )


class UserCreate(UserBase):

    password: str = Field(
        ...,
        min_length=6,
        max_length=100,
        description="Contraseña del usuario"
    )


class UserUpdate(BaseModel):

    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None


class UserResponse(UserBase):

    id: int
    is_admin: bool

    model_config = ConfigDict(from_attributes=True)