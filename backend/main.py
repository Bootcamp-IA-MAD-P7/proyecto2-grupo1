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

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Crear tablas
try:
    Base.metadata.create_all(bind=engine)
    logger.info("✅ Tablas creadas/verificadas")
except Exception as e:
    logger.error(f"❌ Error creando tablas: {e}")

app = FastAPI(
    title="API de Álbumes Musicales",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS
origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins if origins != ["*"] else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")

@app.on_event("startup")
async def startup_event():
    logger.info("🚀 Iniciando app...")
    if not verify_connection():
        logger.warning("⚠️ Sin conexión a BD")
        return
    if settings.AUTO_SEED:
        logger.info("🌱 Verificando datos iniciales...")
        initialize_database()
    logger.info("✨ App lista")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("🛑 Apagando app...")

@app.get("/")
def root() -> Dict[str, Any]:
    return {
        "message": "API de Álbumes Musicales",
        "environment": settings.ENVIRONMENT,
        "endpoints": {
            "albums": "/api/v1/albums/",
            "docs": "/docs"
        }
    }

@app.get("/health")
def health():
    from database.database import test_connection
    return {
        "status": "healthy" if test_connection() else "unhealthy",
        "environment": settings.ENVIRONMENT
    }

@app.post("/seed-database")
def manual_seed(force: bool = False) -> Dict[str, Any]:
    success = initialize_database(force=force)
    if success:
        return {"message": "Seeding exitoso", "force": force}
    raise HTTPException(status_code=500, detail="Error en seeding")