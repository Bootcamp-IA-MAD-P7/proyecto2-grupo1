from pydantic import BaseModel
from typing import List
from datetime import datetime


class OrderItemBase(BaseModel):
    album_id: int
    quantity: int


class OrderItemResponse(OrderItemBase):
    id: int

    class Config:
        from_attributes = True


class OrderBase(BaseModel):
    shipping_address: str


class OrderCreate(OrderBase):
    items: List[OrderItemBase]


class OrderResponse(OrderBase):
    id: int
    user_id: int
    date: datetime
    total: float
    items: List[OrderItemResponse]

    class Config:
        from_attributes = True