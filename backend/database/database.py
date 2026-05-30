# database/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.config_variables import settings

 # Variables de entorno para no exponer información sensible
DB_USER = settings.DB_USER
DB_PASSWORD = settings.DB_PASSWORD
DB_HOST = settings.DB_HOST
DB_NAME = settings.DB_NAME

# Conexión con la base de datos
DATABASE_URL = "mysql+pymysql://"+DB_USER+":"+DB_PASSWORD+"@"+DB_HOST+"/"+DB_NAME+""  # MySQL
# DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Crea un engine
engine = create_engine(DATABASE_URL)

# Crea una clase para configurar la sesión
LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crea una clase base para los modelos
Base = declarative_base()

# función para obtener la sesión de la base de datos
def get_db():
    db = LocalSession()  # Crea una nueva sesión
    try:
        yield db  # Usa la sesión
    finally:
        db.close()  # Cierra la sesión al terminar

# Esta función crea una sesión para trabajar con la base de datos, la devuelve mientras haces algo (yield db) y la cierra automáticamente al terminar.