# controllers/genre_controller.py

from typing import List, Optional
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import SQLAlchemyError
from models.musintage_models import Genre

class GenreControllers:

    # ========== READ (GET) ==========
    
    @staticmethod
    def get_all_genres(db: Session, skip: int = 0, limit: int = 100) -> List[Genre]:
        """Obtener todos los géneros con paginación"""
        try:
            return db.query(Genre).offset(skip).limit(limit).all()
        except SQLAlchemyError as e:
            print(f"Error al obtener géneros: {e}")
            return []

    @staticmethod
    def get_genre_by_id(db: Session, genre_id: int) -> Optional[Genre]:
        """Obtener un género por su ID"""
        try:
            return db.query(Genre).filter(Genre.id == genre_id).first()
        except SQLAlchemyError as e:
            print(f"Error al obtener género con id {genre_id}: {e}")
            return None

    @staticmethod
    def get_genre_by_name(db: Session, name: str) -> Optional[Genre]:
        """Obtener un género por su nombre"""
        try:
            return db.query(Genre).filter(Genre.name == name).first()
        except SQLAlchemyError as e:
            print(f"Error al obtener género por nombre: {e}")
            return None

    @staticmethod
    def get_genre_with_albums(db: Session, genre_id: int) -> Optional[Genre]:
        """Obtener un género con todos sus álbumes"""
        try:
            return db.query(Genre).options(
                joinedload(Genre.albums)
            ).filter(Genre.id == genre_id).first()
        except SQLAlchemyError as e:
            print(f"Error al obtener género con álbumes: {e}")
            return None

    @staticmethod
    def search_genres(db: Session, search_term: str) -> List[Genre]:
        """Buscar géneros por nombre (búsqueda parcial)"""
        try:
            return db.query(Genre).filter(
                Genre.name.ilike(f"%{search_term}%")
            ).all()
        except SQLAlchemyError as e:
            print(f"Error en búsqueda de géneros: {e}")
            return []