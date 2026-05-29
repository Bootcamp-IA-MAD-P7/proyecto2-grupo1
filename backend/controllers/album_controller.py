from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.album_model import Album

class AlbumControllers:

    @staticmethod
    def get_all_albums(db: Session, skip: int = 0, limit: int = 100) -> List[Album]:
        """
        Obtener todos los álbumes con paginación
        
        Args:
            db: Sesión de base de datos
            skip: Número de registros a saltar
            limit: Número máximo de registros a retornar
        
        Returns:
            Lista de álbumes
        """
        try:
            return db.query(Album).offset(skip).limit(limit).all()
        except SQLAlchemyError as e:
            print(f"Error al obtener álbumes: {e}")
            return []

    @staticmethod
    def get_album_by_id(db: Session, album_id: int) -> Optional[Album]:
        """
        Obtener un álbum por su ID
        
        Args:
            db: Sesión de base de datos
            album_id: ID del álbum a buscar
        
        Returns:
            Álbum encontrado o None
        """
        try:
            return db.query(Album).filter(Album.id == album_id).first()
        except SQLAlchemyError as e:
            print(f"Error al obtener álbum con id {album_id}: {e}")
            return None