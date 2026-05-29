# controllers/album_controllers.py

from typing import List, Optional
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from models.musintage_models import Album, Artist, Genre
from schemas.album_schema import AlbumCreate, AlbumUpdate

class AlbumControllers:

    # ========== READ (GET) ==========
    
    @staticmethod
    def get_all_albums(db: Session, skip: int = 0, limit: int = 100) -> List[Album]:
        """Obtener todos los álbumes con paginación"""
        try:
            return db.query(Album).options(
                joinedload(Album.artist),
                joinedload(Album.genre)
            ).offset(skip).limit(limit).all()
        except SQLAlchemyError as e:
            print(f"Error al obtener álbumes: {e}")
            return []

    @staticmethod
    def get_album_by_id(db: Session, album_id: int) -> Optional[Album]:
        """Obtener un álbum por su ID"""
        try:
            return db.query(Album).options(
                joinedload(Album.artist),
                joinedload(Album.genre)
            ).filter(Album.id == album_id).first()
        except SQLAlchemyError as e:
            print(f"Error al obtener álbum con id {album_id}: {e}")
            return None

    # ========== CREATE (POST) ==========
    
    @staticmethod
    def create_album(db: Session, album_data: AlbumCreate) -> Album:
        """Crear un nuevo álbum"""
        try:
            # Verificar si el artista existe
            artist = db.query(Artist).filter(Artist.id == album_data.artist_id).first()
            if not artist:
                raise ValueError(f"Artista con ID {album_data.artist_id} no existe")
            
            # Verificar si el género existe (si se proporcionó)
            if album_data.genre_id:
                genre = db.query(Genre).filter(Genre.id == album_data.genre_id).first()
                if not genre:
                    raise ValueError(f"Género con ID {album_data.genre_id} no existe")
            
            # Crear el álbum
            db_album = Album(
                title=album_data.title,
                artist_id=album_data.artist_id,
                genre_id=album_data.genre_id,
                price=album_data.price,
                stock=album_data.stock,
                year=album_data.year,
                format_type=album_data.format_type,
                image_url=album_data.image_url
            )
            
            db.add(db_album)
            db.commit()
            db.refresh(db_album)
            
            # Cargar relaciones para la respuesta
            return db.query(Album).options(
                joinedload(Album.artist),
                joinedload(Album.genre)
            ).filter(Album.id == db_album.id).first()
            
        except IntegrityError as e:
            db.rollback()
            raise ValueError(f"Error de integridad: {str(e)}")
        except SQLAlchemyError as e:
            db.rollback()
            raise ValueError(f"Error al crear álbum: {str(e)}")

    # ========== UPDATE (PUT/PATCH) ==========
    
    @staticmethod
    def update_album(db: Session, album_id: int, album_data: AlbumUpdate) -> Optional[Album]:
        """Actualizar un álbum existente"""
        try:
            db_album = db.query(Album).filter(Album.id == album_id).first()
            
            if not db_album:
                return None
            
            # Obtener solo los campos que se enviaron
            update_data = album_data.model_dump(exclude_unset=True)
            
            # Verificar si el nuevo artist_id existe
            if 'artist_id' in update_data and update_data['artist_id']:
                artist = db.query(Artist).filter(Artist.id == update_data['artist_id']).first()
                if not artist:
                    raise ValueError(f"Artista con ID {update_data['artist_id']} no existe")
            
            # Verificar si el nuevo genre_id existe
            if 'genre_id' in update_data and update_data['genre_id']:
                genre = db.query(Genre).filter(Genre.id == update_data['genre_id']).first()
                if not genre:
                    raise ValueError(f"Género con ID {update_data['genre_id']} no existe")
            
            # Actualizar campos
            for field, value in update_data.items():
                if hasattr(db_album, field):
                    setattr(db_album, field, value)
            
            db.commit()
            db.refresh(db_album)
            
            # Retornar con relaciones cargadas
            return db.query(Album).options(
                joinedload(Album.artist),
                joinedload(Album.genre)
            ).filter(Album.id == album_id).first()
            
        except IntegrityError as e:
            db.rollback()
            raise ValueError(f"Error de integridad: {str(e)}")
        except SQLAlchemyError as e:
            db.rollback()
            raise ValueError(f"Error al actualizar álbum: {str(e)}")

    # ========== DELETE (DELETE) ==========
    
    @staticmethod
    def delete_album(db: Session, album_id: int) -> bool:
        """Eliminar un álbum por su ID"""
        try:
            db_album = db.query(Album).filter(Album.id == album_id).first()
            
            if not db_album:
                return False
            
            db.delete(db_album)
            db.commit()
            return True
            
        except SQLAlchemyError as e:
            db.rollback()
            raise ValueError(f"Error al eliminar álbum: {str(e)}")

    # ========== MÉTODOS ADICIONALES ==========
    
    @staticmethod
    def get_albums_by_artist(db: Session, artist_id: int) -> List[Album]:
        """Obtener todos los álbumes de un artista específico por ID"""
        try:
            return db.query(Album).filter(Album.artist_id == artist_id).options(
                joinedload(Album.artist),
                joinedload(Album.genre)
            ).all()
        except SQLAlchemyError as e:
            print(f"Error al obtener álbumes por artista: {e}")
            return []
    
    @staticmethod
    def get_albums_by_genre(db: Session, genre_id: int) -> List[Album]:
        """Obtener todos los álbumes de un género específico por ID"""
        try:
            return db.query(Album).filter(Album.genre_id == genre_id).options(
                joinedload(Album.artist),
                joinedload(Album.genre)
            ).all()
        except SQLAlchemyError as e:
            print(f"Error al obtener álbumes por género: {e}")
            return []