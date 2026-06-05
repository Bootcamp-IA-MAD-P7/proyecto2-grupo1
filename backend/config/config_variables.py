# config/config_variables.py

import os
from dotenv import load_dotenv
import urllib.parse

# Cargar variables del .env SOLO si existe (desarrollo local)
if os.path.exists(".env"):
    load_dotenv()

class Settings:
    DB_USER: str = os.getenv("DB_USER", "")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_HOST: str = os.getenv("DB_HOST", "")
    DB_NAME: str = os.getenv("DB_NAME", "")

    # Para Railway/Render (inyectado automáticamente)
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")

    # Control del seeding automático
    AUTO_SEED: bool = os.getenv("AUTO_SEED", "true").lower() == "true"
    SKIP_SEED: bool = os.getenv("SKIP_SEED", "false").lower() == "true"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    @property
    def get_database_url(self) -> str:
        """Retorna la URL de BD para SQLAlchemy"""
        if self.DATABASE_URL:
            if self.DATABASE_URL.startswith("mysql://"):
                return self.DATABASE_URL.replace("mysql://", "mysql+pymysql://", 1)
            return self.DATABASE_URL
        else:
            # Construcción manual para desarrollo local
            encoded_password = urllib.parse.quote_plus(self.DB_PASSWORD)
            return f"mysql+pymysql://{self.DB_USER}:{encoded_password}@{self.DB_HOST}/{self.DB_NAME}"

settings = Settings()

# Solo para depuración en desarrollo
if settings.ENVIRONMENT == "development":
    print(f"🔧 Modo desarrollo - Conectando a DB en: {settings.DB_HOST}")
    print(f"📊 Base de datos: {settings.DB_NAME}")