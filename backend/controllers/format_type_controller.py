# controllers/format_type_controller.py

from typing import List, Optional
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import SQLAlchemyError
from models.musintage_models import FormatType

class FormatTypeControllers:

    # ========== READ (GET) ==========
    
    @staticmethod
    def get_all_formats(db: Session, skip: int = 0, limit: int = 100) -> List[FormatType]:
        """Obtener todos los formatos con paginación"""
        try:
            return db.query(FormatType).offset(skip).limit(limit).all()
        except SQLAlchemyError as e:
            print(f"Error al obtener formatos: {e}")
            return []

    @staticmethod
    def get_format_by_id(db: Session, format_id: int) -> Optional[FormatType]:
        """Obtener un formato por su ID"""
        try:
            return db.query(FormatType).filter(FormatType.id == format_id).first()
        except SQLAlchemyError as e:
            print(f"Error al obtener formato con id {format_id}: {e}")
            return None

    @staticmethod
    def get_format_by_name(db: Session, name: str) -> Optional[FormatType]:
        """Obtener un formato por su nombre"""
        try:
            return db.query(FormatType).filter(FormatType.name == name).first()
        except SQLAlchemyError as e:
            print(f"Error al obtener formato por nombre: {e}")
            return None

    @staticmethod
    def get_format_with_albums(db: Session, format_id: int) -> Optional[FormatType]:
        """Obtener un formato con todos sus álbumes"""
        try:
            return db.query(FormatType).options(
                joinedload(FormatType.albums)
            ).filter(FormatType.id == format_id).first()
        except SQLAlchemyError as e:
            print(f"Error al obtener formato con álbumes: {e}")
            return None

    @staticmethod
    def search_formats(db: Session, search_term: str) -> List[FormatType]:
        """Buscar formatos por nombre (búsqueda parcial)"""
        try:
            return db.query(FormatType).filter(
                FormatType.name.ilike(f"%{search_term}%")
            ).all()
        except SQLAlchemyError as e:
            print(f"Error en búsqueda de formatos: {e}")
            return []