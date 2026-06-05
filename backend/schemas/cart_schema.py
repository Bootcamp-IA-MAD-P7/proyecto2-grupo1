from pydantic import BaseModel, Field, ConfigDict


class CartItemBase(BaseModel):
    """Schema base con atributos comunes"""

    album_id: int = Field(
        ...,
        ge=1,
        description="ID del álbum"
    )

    quantity: int = Field(
        ...,
        ge=1,
        description="Cantidad de álbumes"
    )


class CartItemCreate(CartItemBase):
    pass


class CartItemUpdate(BaseModel):

    quantity: int = Field(
        ...,
        ge=1,
        description="Cantidad actualizada"
    )


class CartItemResponse(CartItemBase):

    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)