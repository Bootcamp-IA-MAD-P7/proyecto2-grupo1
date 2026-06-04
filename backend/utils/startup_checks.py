# utils/startup_checks.py

from database.database import LocalSession
from models.musintage_models import Artist, Genre, FormatType
from config.config_variables import settings
import logging
from sqlalchemy.exc import ProgrammingError

logger = logging.getLogger(__name__)

def is_database_empty():
    """Verifica si la base de datos está vacía (manejando tablas no existentes)"""
    db = LocalSession()
    try:
        # Intentar consultar las tablas
        has_artists = db.query(Artist).first() is not None
        has_genres = db.query(Genre).first() is not None
        has_formats = db.query(FormatType).first() is not None
        
        return not (has_artists or has_genres or has_formats)
    except ProgrammingError as e:
        # Si la tabla no existe, consideramos la BD como vacía
        if 'does not exist' in str(e):
            logger.info("📝 Las tablas aún no existen, se crearán con el seeding")
            return True
        # Otro error de programación
        logger.error(f"Error de programación SQL: {e}")
        raise
    except Exception as e:
        logger.error(f"Error inesperado en is_database_empty: {e}")
        return True
    finally:
        db.close()

def initialize_database(force=False):
    if settings.SKIP_SEED and not force:
        logger.info("⏭️ Seeding omitido por SKIP_SEED")
        return False

    if not force and not is_database_empty():
        logger.info("✅ BD ya tiene datos, omitiendo seeding")
        return False

    logger.info("🔄 Ejecutando seeding...")
    from database.seed import run_seed
    return run_seed()

def verify_connection():
    from database.database import test_connection
    ok = test_connection()
    if ok:
        logger.info("✅ Conexión a BD verificada")
    else:
        logger.error("❌ Error de conexión a BD")
    return ok