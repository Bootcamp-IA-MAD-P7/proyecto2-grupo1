from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from models.album_model import Album
from schemas.album_schema import AlbumCreate, AlbumUpdate

class AlbumControllers:

    # ========== READ (GET) - Obtener datos ==========
    
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

    # ========== CREATE (POST) - Crear nuevo álbum ==========
    
    @staticmethod
    def create_album(db: Session, album_data: AlbumCreate) -> Album:
        """
        Crear un nuevo álbum
        
        Args:
            db: Sesión de base de datos
            album_data: Datos del álbum a crear (validados por Pydantic)
        
        Returns:
            Álbum creado
        
        Raises:
            ValueError: Si hay error de validación o integridad
        """
        try:
            # Verificar si ya existe un álbum con el mismo título y artista (opcional)
            existing_album = db.query(Album).filter(
                Album.title == album_data.title,
                Album.artist == album_data.artist
            ).first()
            
            if existing_album:
                raise ValueError(f"Ya existe un álbum con título '{album_data.title}' del artista '{album_data.artist}'")
            
            # Crear nuevo álbum
            db_album = Album(**album_data.model_dump())
            db.add(db_album)
            db.commit()
            db.refresh(db_album)
            return db_album
            
        except IntegrityError as e:
            db.rollback()
            raise ValueError(f"Error de integridad de datos: {str(e)}")
        except SQLAlchemyError as e:
            db.rollback()
            raise ValueError(f"Error al crear álbum: {str(e)}")

    # ========== UPDATE (PUT/PATCH) - Actualizar álbum ==========
    
    @staticmethod
    def update_album(
        db: Session, 
        album_id: int, 
        album_data: AlbumUpdate
    ) -> Optional[Album]:
        """
        Actualizar un álbum existente
        
        Args:
            db: Sesión de base de datos
            album_id: ID del álbum a actualizar
            album_data: Datos a actualizar (solo los campos proporcionados)
        
        Returns:
            Álbum actualizado o None si no existe
        
        Raises:
            ValueError: Si hay error de validación
        """
        try:
            # Buscar el álbum
            db_album = db.query(Album).filter(Album.id == album_id).first()
            
            if not db_album:
                return None
            
            # Actualizar solo los campos que vienen en el request
            update_data = album_data.model_dump(exclude_unset=True)
            
            for field, value in update_data.items():
                setattr(db_album, field, value)
            
            db.commit()
            db.refresh(db_album)
            return db_album
            
        except IntegrityError as e:
            db.rollback()
            raise ValueError(f"Error de integridad al actualizar: {str(e)}")
        except SQLAlchemyError as e:
            db.rollback()
            raise ValueError(f"Error al actualizar álbum: {str(e)}")

    # ========== DELETE (DELETE) - Eliminar álbum ==========
    
    @staticmethod
    def delete_album(db: Session, album_id: int) -> bool:
        """
        Eliminar un álbum por su ID
        
        Args:
            db: Sesión de base de datos
            album_id: ID del álbum a eliminar
        
        Returns:
            True si se eliminó correctamente, False si no existía
        
        Raises:
            ValueError: Si hay error al eliminar
        """
        try:
            # Buscar el álbum
            db_album = db.query(Album).filter(Album.id == album_id).first()
            
            if not db_album:
                return False
            
            # Eliminar el álbum
            db.delete(db_album)
            db.commit()
            return True
            
        except SQLAlchemyError as e:
            db.rollback()
            raise ValueError(f"Error al eliminar álbum: {str(e)}")

    # ========== MÉTODOS ADICIONALES ÚTILES ==========
    
    @staticmethod
    def search_albums(
        db: Session, 
        search_term: str, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Album]:
        """
        Buscar álbumes por título, artista o género
        
        Args:
            db: Sesión de base de datos
            search_term: Término de búsqueda
            skip: Número de registros a saltar
            limit: Número máximo de registros a retornar
        
        Returns:
            Lista de álbumes que coinciden con la búsqueda
        """
        try:
            return db.query(Album).filter(
                (Album.title.ilike(f"%{search_term}%")) |
                (Album.artist.ilike(f"%{search_term}%")) |
                (Album.genre.ilike(f"%{search_term}%"))
            ).offset(skip).limit(limit).all()
        except SQLAlchemyError as e:
            print(f"Error en búsqueda: {e}")
            return []
    
    @staticmethod
    def get_albums_by_artist(db: Session, artist: str) -> List[Album]:
        """
        Obtener todos los álbumes de un artista específico
        
        Args:
            db: Sesión de base de datos
            artist: Nombre del artista
        
        Returns:
            Lista de álbumes del artista
        """
        try:
            return db.query(Album).filter(Album.artist.ilike(f"%{artist}%")).all()
        except SQLAlchemyError as e:
            print(f"Error al obtener álbumes por artista: {e}")
            return []
    
    @staticmethod
    def update_stock(db: Session, album_id: int, quantity_change: int) -> Optional[Album]:
        """
        Actualizar el stock de un álbum (incrementar o decrementar)
        
        Args:
            db: Sesión de base de datos
            album_id: ID del álbum
            quantity_change: Cambio en cantidad (positivo o negativo)
        
        Returns:
            Álbum actualizado o None si no existe
        
        Raises:
            ValueError: Si el stock resultante sería negativo
        """
        try:
            db_album = db.query(Album).filter(Album.id == album_id).first()
            
            if not db_album:
                return None
            
            new_stock = db_album.stock + quantity_change
            
            if new_stock < 0:
                raise ValueError(f"No hay suficiente stock. Stock actual: {db_album.stock}")
            
            db_album.stock = new_stock
            db.commit()
            db.refresh(db_album)
            return db_album
            
        except SQLAlchemyError as e:
            db.rollback()
            raise ValueError(f"Error al actualizar stock: {str(e)}")