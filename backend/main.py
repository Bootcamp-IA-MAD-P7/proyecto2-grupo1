from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.routes import router
from database.database import engine, Base
from typing import Any, Dict

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Inicializar la aplicación FastAPI
app = FastAPI(
    title="API de Álbumes Musicales",
    description="API para gestionar información de álbumes musicales",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(router)

@app.get("/", tags=["root"])
def root() -> Dict[str, Any]:
    """Endpoint raíz con información básica"""
    return {
        "message": "API de Álbumes Musicales",
        "version": "1.0.0",
        "endpoints": {
            "albums": "/api/v1/albums/",
            "album_by_id": "/api/v1/albums/{id}",
            "documentation": "/docs"
        }
    }

@app.get("/health", tags=["health"])
def health_check():
    """Endpoint para verificar el estado de la API"""
    return {"status": "healthy", "service": "album-api"}