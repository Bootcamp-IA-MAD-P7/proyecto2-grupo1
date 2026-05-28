# 🚀 Musintage Backend — FastAPI

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F1F?style=for-the-badge&logo=SQLAlchemy&logoColor=white" alt="SQLAlchemy">
</p>

Este directorio contiene el núcleo de la API para el proyecto **Musintage**, desarrollado utilizando **FastAPI** y **Python**. El sistema gestiona de forma centralizada la lógica de e-commerce de música (usuarios, álbumes, carritos, categorías y pedidos) utilizando **MySQL** como motor de persistencia y **SQLAlchemy** como ORM.

---

## 🛠️ Requisitos Previos

Antes de desplegar el backend en tu entorno local, asegúrate de contar con:
* 🐍 **Python 3.10+**
* 🐬 Servidor local **MySQL** *(activo mediante XAMPP, Workbench o Docker)*
* 📦 Gestor de paquetes `pip`

---

## 📦 Instalación y Configuración

Sigue estos pasos ordenados en tu terminal para inicializar el entorno de desarrollo de forma limpia:

### 1️⃣ Entrar a la carpeta del backend
```bash
cd backend

2️⃣ Crear y activar el entorno virtual (.venv)
En entornos Windows (usando Git Bash / Terminal de VS Code):

python -m venv .venv
source .venv/Scripts/activate

3️⃣ Instalar las dependencias del proyecto
Instala todos los paquetes requeridos mapeados en el archivo requirements.txt:

pip install -r requirements.txt

4️⃣ Configurar las Variables de Enorno
Crea un archivo llamado .env en la raíz de la carpeta backend/ para mapear las credenciales locales.

⚠️ IMPORTANTE: El archivo .env real contiene credenciales privadas. Está configurado de forma estricta en el .gitignore y nunca debe ser subido al repositorio público de GitHub.

Utiliza la siguiente estructura limpia como plantilla:

DB_USER=tu_usuario_mysql
DB_PASSWORD=tu_contraseña_mysql
DB_HOST=127.0.0.1
DB_NAME=musintage

⚡ Ejecución del Servidor y Base de Datos
El archivo principal main.py incluye una rutina automatizada que genera de forma automática las tablas en tu base de datos local al inicializar la aplicación por primera vez mediante la instrucción database.Base.metadata.create_all.

Para encender el servidor de desarrollo en tiempo real con recarga automática (live-reload), ejecuta:

uvicorn main:app --reload

El servicio se desplegará de forma local en:
 🔗 http://127.0.0.1:8000

📂 Documentación Interactiva (Swagger UI)
FastAPI genera automáticamente una interfaz gráfica interactiva para testear y revisar todos los endpoints en tiempo real. Puedes acceder desde el navegador en:

🗺️ Swagger UI: http://127.0.0.1:8000/docs

Método,Endpoint,Descripción,Payload (Ejemplo de Entrada)
GET,/,Mensaje de bienvenida oficial,Ninguno
POST,/album,Registro y validación de un nuevo álbum,Ver JSON abajo

Ejemplo de estructura para POST /album

JSON 

{
  "title": "Abbey Road",
  "artist": "The Beatles",
  "genre": "Rock",
  "price": 29.99,
  "stock": 15,
  "year": 1969,
  "format": "Vinyl",
  "image_url": "[http://example.com/abbeyroad.jpg](http://example.com/abbeyroad.jpg)",
  "category_id": 1
}

📁 Arquitectura y Estructura del Código
El backend sigue un diseño arquitectónico modular estructurado por responsabilidades lógicas:

⚙️ config/

config_variables.py: Inicializa la clase Settings encargada de procesar el entorno mediante python-dotenv.

🗄️ database/

database.py: Implementa la conexión mediante el driver mysql+pymysql, levanta el motor de SQLAlchemy (create_engine) y expone la función inyectable get_db() para el manejo limpio del ciclo de vida de las sesiones.

📐 schemas/ (Modelos de validación estructural basados en Pydantic)

album_schema.py / album.py: Validaciones completas para creación, edición y respuestas de álbumes (títulos, artistas, precios y stock).

auth.py: Modelos para el inicio de sesión y gestión de tokens de seguridad.

cart.py: Estructura para el flujo de ítems dentro de los carritos de compra.

category.py: Modelos base y respuestas para la catalogación estricta de productos.

order.py: Esquemas para el procesamiento de pedidos de clientes.

user.py: Validaciones de perfiles de usuario (UserCreate, UserUpdate) utilizando EmailStr.

🚀 main.py

Punto de entrada de la aplicación. Inicializa la app de FastAPI, levanta los metadatos de las tablas en MySQL y expone las rutas principales.
