# schemas/genre_schema.py

from pydantic import BaseModel, ConfigDict
from typing import List
from schemas.album_schema import AlbumResponse

class GenreBase(BaseModel):
    """Schema base con atributos comunes de género"""
    name: str

class GenreResponse(GenreBase):
    """Schema para respuesta de género"""
    id: int
    model_config = ConfigDict(from_attributes=True)

class GenreWithAlbumsResponse(GenreBase):
    """Schema para respuesta de género con sus álbumes"""
    id: int
    albums: List[AlbumResponse] = []
    model_config = ConfigDict(from_attributes=True)