# 🚀 Musintage Backend — FastAPI

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F27?style=for-the-badge&logo=python&logoColor=white)](https://www.sqlalchemy.org/)
[![Database](https://img.shields.io/badge/MySQL%20%2F%20PostgreSQL-4479A1?style=for-the-badge&logo=database)](https://github.com/)

Este directorio contiene el núcleo de la API para el proyecto **Musintage**, desarrollado utilizando **FastAPI** y **Python**. El sistema gestiona de forma centralizada la lógica de e-commerce de música (usuarios, álbumes, carritos, categorías y pedidos). Usa **SQLAlchemy** como ORM y soporta la conexión nativa a MySQL o PostgreSQL según la configuración de la variable `DATABASE_URL`.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** 🐍 Python 3.10+
* **Bases de Datos:** 🐬 MySQL / PostgreSQL (Dinámico mediante `DATABASE_URL`)
* **Gestor de paquetes:** 📦 pip
* **Framework principal:** ⚡ FastAPI, Uvicorn, Pydantic
* **ORM:** 🗄️ SQLAlchemy
* **Testing:** 🧪 Pytest

---

## 📁 Documentación Interactiva (Swagger UI)

FastAPI genera automáticamente una interfaz gráfica interactiva para testear y revisar todos los endpoints en tiempo real una vez que el servidor está corriendo:

* 📍 **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* 📍 **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📐 Arquitectura y Estructura del Código

El backend sigue un diseño modular y desacoplado por responsabilidades:

```text
├── ⚙️ config/
│   └── config_variables.py   # Inicializa la clase Settings (procesa el entorno vía python-dotenv).
├── 🗄️ database/
│   └── database.py           # Conexión SQLAlchemy (create_engine), get_db() y pooling de producción.
├── 📂 routes/
│   └── routes.py             # Define las rutas principales bajo el prefijo /api/v1.
├── 📐 schemas/
│   └── ...                   # Validaciones Pydantic (AlbumResponse, AlbumCreate, ArtistResponse, etc.).
├── 🎮 controllers/
│   └── ...                   # Lógica de negocio (AlbumControllers, ArtistControllers, etc.).
├── 🧰 utils/
│   └── startup_checks.py     # verify_connection() e initialize_database() (seeding automático).
└── 🚀 main.py                # Punto de entrada. Inicializa FastAPI, CORS y middlewares.

🛠️ Especificaciones Tecnológicas y Capacidades
El stack tecnológico ha sido seleccionado estratégicamente para ofrecer un balance ideal entre velocidad de desarrollo y rendimiento en producción:

Core Engine: FastAPI ⚡ sobre Python 3.10+, aprovechando la validación asíncrona nativa y el tipado estricto para reducir errores en tiempo de ejecución.

Capa de Persistencia: SQLAlchemy ORM 🗄️ integrado con el driver mysql+pymysql. Actúa como una capa de abstracción agnóstica que permite la conmutación nativa entre MySQL y PostgreSQL según las necesidades de infraestructura a través de variables de entorno.

Validación y DTOs: Pydantic 📐, garantizando que cualquier entrada o salida de datos cumpla rigurosamente con los esquemas definidos, incluyendo validaciones complejas de tipos y correos electrónicos (EmailStr).

Calidad de Software: Suite de pruebas automatizadas integrada con Pytest 🧪 para la verificación de endpoints y lógica de negocio.

🌐 Ecosistema de Servicios y Endpoints
La API expone una interfaz REST estructurada y predecible para interactuar con el dominio de Musintage.

📋 Gestión del Sistema y Control de Estado
Ciclo de Vida e Inicialización: El archivo principal main.py incluye una rutina automatizada que genera las tablas en la base de datos local al inicializar la aplicación mediante la instrucción database.Base.metadata.create_all.

Monitoreo de Infraestructura: Endpoint de salud (GET /health) que ejecuta consultas de control de conexión directa (SELECT 1) contra la base de datos para asegurar la disponibilidad del servicio.

Sincronización de Datos Iniciales: Mecanismo de inicialización automatizada (AUTO_SEED) o manual (POST /seed-database) para el aprovisionamiento controlado de datos de prueba en entornos de desarrollo.

📁 Documentación Interactiva (Swagger UI)
El framework genera automáticamente una interfaz gráfica interactiva para testear y revisar todos los endpoints en tiempo real.

🗺️ Swagger UI: http://127.0.0.1:8000/docs

📍 ReDoc: http://127.0.0.1:8000/redoc

🔒 Robustez y Operaciones en Producción
El backend está diseñado bajo estándares modernos de resiliencia y seguridad:

Pooling de Conexiones Dinámico: El sistema detecta el entorno operativo de forma autónoma. En producción (ENVIRONMENT=production), conmuta automáticamente hacia un esquema de QueuePool ajustando los parámetros de tamaño de pool (pool_size) y desbordamiento máximo (max_overflow) para soportar alta concurrencia. En desarrollo, prioriza el modo depuración (echo=True).

Seguridad Perimetral: Aislamiento de secretos de infraestructura (claves criptográficas, credenciales de BD) mediante inyección de entorno externa, soporte nativo para políticas de origen cruzado (CORS) restringidas y diseño preparado para la inyección de middleware de autenticación (JWT/OAuth2) mediante el módulo auth.py.

Ciclo de Vida Automatizado: Gestión nativa de eventos de inicio y parada (startup/shutdown), garantizando una inicialización controlada de esquemas y un cierre limpio e inyectable de las sesiones de base de datos a través de get_db().