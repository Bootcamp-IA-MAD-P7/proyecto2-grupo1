from pydantic import BaseModel, EmailStr, Field


class LoginSchema(BaseModel):
    """Schema para login de usuario"""

    email: EmailStr = Field(
        ...,
        description="Correo electrónico del usuario"
    )

    password: str = Field(
        ...,
        min_length=6,
        description="Contraseña del usuario"
    )


class TokenSchema(BaseModel):
    """Schema para token JWT"""

    access_token: str = Field(
        ...,
        description="JWT access token"
    )

    token_type: str = Field(
        ...,
        description="Tipo de token"
    )