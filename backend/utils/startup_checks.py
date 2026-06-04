# utils/startup_checks.py

from database.database import LocalSession
from models.musintage_models import Artist, Genre, FormatType  # ← Ruta correcta
import logging

logger = logging.getLogger(__name__)

def is_database_empty():
    """Verifica si la base de datos está vacía"""
    db = LocalSession()
    try:
        has_artists = db.query(Artist).first() is not None
        has_genres = db.query(Genre).first() is not None
        has_formats = db.query(FormatType).first() is not None
        
        return not (has_artists or has_genres or has_formats)
    finally:
        db.close()

def initialize_database(force=False):
    """
    Inicializa la base de datos con datos semilla si está vacía
    Args:
        force: Si es True, fuerza el seeding aunque haya datos
    """
    from config.config_variables import settings  # ← Importación correcta
    
    skip_seed = settings.SKIP_SEED
    
    if skip_seed and not force:
        logger.info("⏭️ Seeding omitido por SKIP_SEED=true")
        return False
    
    if not force and not is_database_empty():
        logger.info("✅ Base de datos ya tiene datos - omitiendo seeding")
        return False
    
    logger.info("🔄 Base de datos vacía o force=True - ejecutando seeding...")
    from database.seed import run_seed
    return run_seed()

def verify_connection():
    """Verifica que la conexión a la BD funcione correctamente"""
    try:
        from database.database import test_connection
        if test_connection():
            logger.info("✅ Conexión a base de datos verificada")
            return True
        else:
            logger.error("❌ No se pudo conectar a la base de datos")
            return False
    except Exception as e:
        logger.error(f"❌ Error verificando conexión: {e}")
        return False