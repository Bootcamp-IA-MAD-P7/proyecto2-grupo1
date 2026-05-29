from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
# from datetime import date

class AlbumBase(BaseModel):
    """Schema base con atributos comunes"""
    title: str = Field(..., min_length=1, max_length=200, description="Título del álbum")
    artist: str = Field(..., min_length=1, max_length=100, description="Nombre del artista")
    genre: Optional[str] = Field(None, max_length=50, description="Género musical")
    price: float = Field(..., ge=0, description="Precio en euros")
    stock: int = Field(..., ge=0, description="Cantidad en inventario")
    year: Optional[int] = Field(None, ge=1900, le=2026, description="Año de lanzamiento")
    format: Optional[str] = Field(None, max_length=50, description="Tipo de formato del álbum")
    image_url: Optional[str] = Field(None, max_length=500, description="URL de la imagen")


class AlbumCreate(AlbumBase):
    category_id: int


class AlbumUpdate(BaseModel):
    title: Optional[str] = None
    artist: Optional[str] = None
    genre: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    year: Optional[int] = None
    description: Optional[str] = None
    image_url: Optional[str] = None


class AlbumResponse(AlbumBase):
    id: int
    category_id: int

    class Config:
        from_attributes = True

        model_config = ConfigDict(from_attributes=True)  # ORM mode