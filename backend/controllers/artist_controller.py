# controllers/artist_controller.py

from typing import List, Optional
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import SQLAlchemyError
from models.musintage_models import Artist

class ArtistControllers:

    # ========== READ (GET) ==========
    
    @staticmethod
    def get_all_artists(db: Session, skip: int = 0, limit: int = 100) -> List[Artist]:
        """Obtener todos los artistas con paginación"""
        try:
            return db.query(Artist).offset(skip).limit(limit).all()
        except SQLAlchemyError as e:
            print(f"Error al obtener artistas: {e}")
            return []

    @staticmethod
    def get_artist_by_id(db: Session, artist_id: int) -> Optional[Artist]:
        """Obtener un artista por su ID"""
        try:
            return db.query(Artist).filter(Artist.id == artist_id).first()
        except SQLAlchemyError as e:
            print(f"Error al obtener artista con id {artist_id}: {e}")
            return None

    @staticmethod
    def get_artist_with_albums(db: Session, artist_id: int) -> Optional[Artist]:
        """Obtener un artista con todos sus álbumes"""
        try:
            return db.query(Artist).options(
                joinedload(Artist.albums)
            ).filter(Artist.id == artist_id).first()
        except SQLAlchemyError as e:
            print(f"Error al obtener artista con álbumes: {e}")
            return None

    @staticmethod
    def search_artists(db: Session, search_term: str) -> List[Artist]:
        """Buscar artistas por nombre (búsqueda parcial)"""
        try:
            return db.query(Artist).filter(
                Artist.name.ilike(f"%{search_term}%")
            ).all()
        except SQLAlchemyError as e:
            print(f"Error en búsqueda de artistas: {e}")
            return []
    
    @staticmethod
    def get_artists_by_nationality(db: Session, nationality: str) -> List[Artist]:
        """Obtener artistas por nacionalidad"""
        try:
            return db.query(Artist).filter(
                Artist.nationality.ilike(f"%{nationality}%")
            ).all()
        except SQLAlchemyError as e:
            print(f"Error al obtener artistas por nacionalidad: {e}")
            return []