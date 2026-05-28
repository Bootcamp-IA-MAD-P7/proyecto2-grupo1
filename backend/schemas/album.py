from pydantic import BaseModel
from typing import Optional


class Base(BaseModel):
    titulo: str
    artista: str
    genero: str
    precio: float
    stock: int
    año: int
    descripcion: Optional[str] = None
    imagen_url: Optional[str] = None


class AlbumCreate(Base):
    categoria_id: int


class AlbumUpdate(BaseModel):
    titulo: Optional[str] = None
    artista: Optional[str] = None
    genero: Optional[str] = None
    precio: Optional[float] = None
    stock: Optional[int] = None
    año: Optional[int] = None
    descripcion: Optional[str] = None
    imagen_url: Optional[str] = None


class AlbumResponse(Base):
    id: int
    categoria_id: int

    class Config:
        from_attributes = True