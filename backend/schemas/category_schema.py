from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class CategoryBase(BaseModel):
    """Schema base con atributos comunes"""

    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Nombre de la categoría"
    )

    description: Optional[str] = Field(
        None,
        max_length=500,
        description="Descripción de la categoría"
    )


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):

    name: Optional[str] = None
    description: Optional[str] = None


class CategoryResponse(CategoryBase):

    id: int

    model_config = ConfigDict(from_attributes=True)