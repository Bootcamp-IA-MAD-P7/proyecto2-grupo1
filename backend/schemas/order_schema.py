from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from datetime import datetime


class OrderItemBase(BaseModel):
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


class OrderItemResponse(OrderItemBase):

    id: int

    model_config = ConfigDict(from_attributes=True)


class OrdersBase(BaseModel):
    """Schema base con atributos comunes"""

    shipping_address: str = Field(
        ...,
        min_length=5,
        max_length=300,
        description="Dirección de envío"
    )


class OrderCreate(OrdersBase):

    items: List[OrderItemBase]


class OrderUpdate(BaseModel):

    shipping_address: Optional[str] = None


class OrderResponse(OrdersBase):

    id: int
    user_id: int
    total: float
    created_at: datetime
    items: List[OrderItemResponse]

    model_config = ConfigDict(from_attributes=True)