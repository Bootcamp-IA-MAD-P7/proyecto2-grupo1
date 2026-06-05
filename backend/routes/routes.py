# routes/routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from controllers.album_controller import AlbumControllers
from controllers.artist_controller import ArtistControllers
from controllers.genre_controller import GenreControllers
from controllers.format_type_controller import FormatTypeControllers
from schemas.album_schema import AlbumResponse, AlbumCreate, AlbumUpdate
from schemas.artist_schema import ArtistResponse
from schemas.genre_schema import GenreResponse
from schemas.format_type_schema import FormatTypeResponse
from database.database import get_db

router = APIRouter()

# ========== RUTAS DE ÁLBUMES (CRUD) ==========

@router.get(
    "/albums", 
    response_model=List[AlbumResponse], 
    tags=["Albums"], 
    summary="Obtener todos los álbumes",
    description="Retorna una lista paginada de todos los álbumes musicales. Permite usar skip y limit para paginación."
)
def get_albums(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return AlbumControllers.get_all_albums(db, skip=skip, limit=limit)

@router.get(
    "/albums/{album_id}", 
    response_model=AlbumResponse, 
    tags=["Albums"],
    summary="Obtener un álbum por ID",
    description="Retorna los detalles completos de un álbum específico utilizando su ID único."
)
def get_album(album_id: int, db: Session = Depends(get_db)):
    album = AlbumControllers.get_album_by_id(db, album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Álbum no encontrado")
    return album

@router.post(
    "/albums", 
    response_model=AlbumResponse, 
    status_code=201, 
    tags=["Albums"],
    summary="Crear un nuevo álbum",
    description="Crea un nuevo álbum musical con toda su información (título, artista, género, formato, año, etc.)."
)
def create_album(album: AlbumCreate, db: Session = Depends(get_db)):
    try:
        return AlbumControllers.create_album(db, album)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put(
    "/albums/{album_id}", 
    response_model=AlbumResponse, 
    tags=["Albums"],
    summary="Actualizar un álbum existente",
    description="Actualiza los datos de un álbum específico. Solo se deben enviar los campos a modificar."
)
def update_album(album_id: int, album: AlbumUpdate, db: Session = Depends(get_db)):
    updated = AlbumControllers.update_album(db, album_id, album)
    if not updated:
        raise HTTPException(status_code=404, detail="Álbum no encontrado")
    return updated

@router.delete(
    "/albums/{album_id}", 
    status_code=204, 
    tags=["Albums"],
    summary="Eliminar un álbum",
    description="Elimina permanentemente un álbum de la base de datos utilizando su ID."
)
def delete_album(album_id: int, db: Session = Depends(get_db)):
    deleted = AlbumControllers.delete_album(db, album_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Álbum no encontrado")
    return None

# ========== RUTAS DE ARTISTAS (SOLO LECTURA) ==========

@router.get(
    "/artists", 
    response_model=List[ArtistResponse], 
    tags=["Artists"],
    summary="Obtener todos los artistas",
    description="Retorna una lista paginada de todos los artistas musicales disponibles en la base de datos."
)
def get_artists(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtener todos los artistas"""
    return ArtistControllers.get_all_artists(db, skip=skip, limit=limit)

# ========== RUTAS DE GÉNEROS (SOLO LECTURA) ==========

@router.get(
    "/genres", 
    response_model=List[GenreResponse], 
    tags=["Genres"],
    summary="Obtener todos los géneros musicales",
    description="Retorna una lista paginada de todos los géneros musicales (Rock, Pop, Jazz, etc.) disponibles."
)
def get_genres(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtener todos los géneros musicales"""
    return GenreControllers.get_all_genres(db, skip=skip, limit=limit)

# ========== RUTAS DE FORMATOS (SOLO LECTURA) ==========

@router.get(
    "/formats", 
    response_model=List[FormatTypeResponse], 
    tags=["Formats"],
    summary="Obtener todos los formatos",
    description="Retorna una lista paginada de todos los formatos disponibles (CD, Vinilo, Cassette, Digital, etc.)."
)
def get_formats(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtener todos los formatos disponibles"""
    return FormatTypeControllers.get_all_formats(db, skip=skip, limit=limit)