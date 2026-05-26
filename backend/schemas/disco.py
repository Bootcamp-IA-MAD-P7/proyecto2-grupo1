from pydantic import BaseModel
from typing import Optional


class DiscoBase(BaseModel):
    titulo: str
    artista: str
    genero: str
    precio: float
    stock: int
    año: int
    descripcion: Optional[str] = None
    imagen_url: Optional[str] = None


class DiscoCreate(DiscoBase):
    categoria_id: int


class DiscoUpdate(BaseModel):
    titulo: Optional[str] = None
    artista: Optional[str] = None
    genero: Optional[str] = None
    precio: Optional[float] = None
    stock: Optional[int] = None
    año: Optional[int] = None
    descripcion: Optional[str] = None
    imagen_url: Optional[str] = None


class DiscoResponse(DiscoBase):
    id: int
    categoria_id: int

    class Config:
        from_attributes = True