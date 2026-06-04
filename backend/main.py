# main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routes.routes import router
from database.database import engine, Base
from utils.startup_checks import initialize_database, verify_connection
from config.config_variables import settings
from typing import Any, Dict
import os
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ✅ IMPORTANTE: Crear tablas ANTES de cualquier otra operación
try:
    logger.info("📝 Creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    logger.info("✅ Tablas creadas/verificadas correctamente")
except Exception as e:
    logger.error(f"❌ Error al crear tablas: {e}")

# Inicializar la aplicación FastAPI
app = FastAPI(
    title="API de Álbumes Musicales",
    description="API para gestionar información de álbumes musicales",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS if ALLOWED_ORIGINS != ["*"] else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(router, prefix="/api/v1")

@app.on_event("startup")
async def startup_event():
    """Evento que se ejecuta al iniciar la aplicación"""
    logger.info("🚀 Iniciando aplicación...")
    
    # Verificar conexión a base de datos
    if not verify_connection():
        logger.warning("⚠️ No se pudo conectar a la base de datos")
        return
    
    # Inicializar datos semilla automáticamente
    if settings.AUTO_SEED:
        logger.info("🌱 Verificando y cargando datos iniciales...")
        success = initialize_database()
        if success:
            logger.info("✅ Datos iniciales cargados exitosamente")
        else:
            logger.info("ℹ️ Datos iniciales ya existían o se omitió el seeding")
    else:
        logger.info("ℹ️ Auto-seeding desactivado por configuración")
    
    logger.info("✨ Aplicación lista para recibir peticiones")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("🛑 Apagando aplicación...")

@app.get("/", tags=["root"])
def root() -> Dict[str, Any]:
    return {
        "message": "API de Álbumes Musicales",
        "version": "1.0.0",
        "environment": settings.ENVIRONMENT,
        "database_type": "PostgreSQL",
        "endpoints": {
            "albums": "/api/v1/albums/",
            "artists": "/api/v1/artists/",
            "genres": "/api/v1/genres/",
            "formats": "/api/v1/formats/",
            "health": "/health",
            "docs": "/docs"
        }
    }

@app.get("/health", tags=["health"])
def health_check():
    from database.database import test_connection
    
    db_status = test_connection()
    return {
        "status": "healthy" if db_status else "unhealthy",
        "service": "album-api",
        "environment": settings.ENVIRONMENT,
        "database": "connected" if db_status else "disconnected"
    }

@app.post("/seed-database", tags=["admin"])
def manual_seed(force: bool = False) -> Dict[str, Any]:
    """Endpoint manual para ejecutar seeding (solo para administración)"""
    logger.info(f"🔄 Ejecutando seeding manual (force={force})")
    from utils.startup_checks import initialize_database
    
    success = initialize_database(force=force)
    if success:
        return {"message": "Seeding completado exitosamente", "force": force}
    else:
        raise HTTPException(status_code=500, detail="Error durante el seeding")