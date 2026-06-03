# schemas/artist_schema.py

from pydantic import BaseModel, ConfigDict
from typing import List
from schemas.album_schema import AlbumResponse

class ArtistBase(BaseModel):
    """Schema base con atributos comunes de artista"""
    name: str
    nationality: str

class ArtistResponse(ArtistBase):
    """Schema para respuesta de artista"""
    id: int
    model_config = ConfigDict(from_attributes=True)

class ArtistWithAlbumsResponse(ArtistBase):
    """Schema para respuesta de artista con sus álbumes"""
    id: int
    albums: List[AlbumResponse] = []
    model_config = ConfigDict(from_attributes=True)