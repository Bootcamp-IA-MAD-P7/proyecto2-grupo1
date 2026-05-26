from pydantic import BaseModel
from typing import List
from datetime import datetime


class PedidoItemBase(BaseModel):
    disco_id: int
    cantidad: int


class PedidoItemResponse(PedidoItemBase):
    id: int

    class Config:
        from_attributes = True


class PedidoBase(BaseModel):
    direccion_envio: str


class PedidoCreate(PedidoBase):
    items: List[PedidoItemBase]


class PedidoResponse(PedidoBase):
    id: int
    usuario_id: int
    fecha: datetime
    total: float
    items: List[PedidoItemResponse]

    class Config:
        from_attributes = True