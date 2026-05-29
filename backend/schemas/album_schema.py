# models/album_schema.py

from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class AlbumBase(BaseModel):
    """Schema base con atributos comunes"""
    title: str = Field(..., min_length=1, max_length=45, description="Título del álbum")
    price: float = Field(..., ge=0, description="Precio en euros")
    stock: int = Field(..., ge=0, description="Cantidad en inventario")
    year: Optional[int] = Field(None, ge=1900, le=2026, description="Año de lanzamiento")
    format_type: Optional[str] = Field(None, max_length=50, description="Tipo de formato del álbum")
    image_url: Optional[str] = Field(None, max_length=500, description="URL de la imagen")

class AlbumCreate(AlbumBase):
    """Schema para crear un nuevo álbum"""
    artist_id: int = Field(..., description="ID del artista (debe existir en la tabla artist)")
    genre_id: Optional[int] = Field(None, description="ID del género musical (opcional, debe existir en la tabla genre)")

class AlbumUpdate(BaseModel):
    """Schema para actualizar un álbum existente"""
    title: Optional[str] = Field(None, min_length=1, max_length=45)
    artist_id: Optional[int] = None
    genre_id: Optional[int] = None
    price: Optional[float] = Field(None, ge=0)
    stock: Optional[int] = Field(None, ge=0)
    year: Optional[int] = Field(None, ge=1900, le=2026)
    format_type: Optional[str] = Field(None, max_length=50)
    image_url: Optional[str] = Field(None, max_length=500)

class AlbumResponse(AlbumBase):
    """Schema para respuesta de álbum (con relaciones incluidas)"""
    id: int
    artist_id: int
    genre_id: Optional[int] = None
    
    # Opcional: Incluir datos relacionados para respuestas más completas
    artist_name: Optional[str] = None  # Para mostrar el nombre en la respuesta
    genre_name: Optional[str] = None   # Para mostrar el género en la respuesta

    model_config = ConfigDict(from_attributes=True)