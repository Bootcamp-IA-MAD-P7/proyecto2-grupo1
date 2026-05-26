from pydantic import BaseModel


class CarritoItemBase(BaseModel):
    disco_id: int
    cantidad: int


class CarritoItemCreate(CarritoItemBase):
    pass


class CarritoItemResponse(CarritoItemBase):
    id: int
    usuario_id: int

    class Config:
        from_attributes = True