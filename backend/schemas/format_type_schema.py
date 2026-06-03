# schemas/format_type_schema.py

from pydantic import BaseModel, ConfigDict
from typing import List
from schemas.album_schema import AlbumResponse

class FormatTypeBase(BaseModel):
    """Schema base con atributos comunes de formato"""
    name: str

class FormatTypeResponse(FormatTypeBase):
    """Schema para respuesta de formato"""
    id: int
    model_config = ConfigDict(from_attributes=True)

class FormatTypeWithAlbumsResponse(FormatTypeBase):
    """Schema para respuesta de formato con sus álbumes"""
    id: int
    albums: List[AlbumResponse] = []
    model_config = ConfigDict(from_attributes=True)