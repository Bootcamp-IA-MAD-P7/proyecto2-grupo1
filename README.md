# 🎵 MUSINTAGE — Tienda de Música física & online

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)

**Musintage** es una plataforma de e-commerce especializada en la venta de música (álbumes, vinilos, merchandise). El proyecto está estructurado como un **monorepo** que contiene tanto el backend (API REST) como el frontend (aplicación web), permitiendo una gestión unificada del código y despliegues coordinados.

---

## 🧠 ¿Qué es Musintage?

Musintage nace como un proyecto integral para la venta de productos musicales, combinando un catálogo robusto de álbumes, artistas y géneros con un dashboard administrativo para su gestión. La plataforma está diseñada para ofrecer una experiencia de usuario fluida, moderna y responsive, respaldada por una API de alto rendimiento.

---

## 🏗️ Arquitectura del Proyecto

El sistema sigue una arquitectura **cliente-servidor** desacoplada, donde el frontend y el backend se comunican exclusivamente a través de una API REST documentada.

```text
📁 Musintage (Monorepo)
├── 📁 backend/                # API REST con FastAPI + Python
│   ├── routes/                # Endpoints organizados por dominio
│   ├── controllers/           # Lógica de negocio
│   ├── schemas/               # Modelos Pydantic (validación)
│   ├── database/              # Configuración SQLAlchemy
│   └── main.py                # Punto de entrada del servidor
│
├── 📁 frontend/               # Aplicación React + Vite
│   ├── src/
│   │   ├── components/        # Componentes reutilizables
│   │   ├── pages/             # Vistas principales
│   │   ├── services/          # Cliente HTTP (API calls)
│   │   └── hooks/             # Lógica compartida
│   └── package.json
│
└── 📄 README.md               # Este archivo

```

## 🔄 Flujo de Comunicación

- El frontend (React) realiza peticiones HTTP asíncronas hacia el backend.
- El backend (FastAPI) procesa la solicitud, aplica validaciones con Pydantic, y ejecuta la lógica de negocio en los controladores.
- El backend interactúa con la base de datos PostgreSQL a través de SQLAlchemy ORM.
- La respuesta (JSON) es enviada de vuelta al frontend para ser renderizada.

## 📚 Documentación de la API (FastAPI)

La API REST está completamente documentada de forma interactiva gracias a FastAPI. Una vez que el backend está desplegado o corriendo localmente, puedes explorar y probar todos los endpoints desde:

📍 Swagger UI: https://proyecto2-grupo1.onrender.com/docs (producción)

📍 ReDoc: https://proyecto2-grupo1.onrender.com/redoc

## 🔍 Características de la documentación

- Autogenerada a partir de los tipos de datos de Pydantic y las rutas definidas.
- Interactiva: permite ejecutar peticiones GET, POST, PUT, DELETE directamente desde el navegador.
- Esquemas visibles: cada endpoint muestra el modelo de solicitud (request body) y la estructura de respuesta esperada.
- Agrupación por etiquetas: artistas, álbumes, carrito, usuarios, pedidos, etc.

💡 La documentación está siempre sincronizada con el código real, evitando la obsolescencia.

## 🚀 Despliegue en Render

Todo el ecosistema de Musintage está desplegado en Render.com, una plataforma PaaS moderna que ofrece integración continua, certificados SSL automáticos y escalabilidad.

## 🗄️ Base de Datos (PostgreSQL)

Servicio: Render PostgreSQL (plan gratuito o según necesidades).
Características:

- Copias de seguridad automáticas.
- Conexión cifrada (SSL requerida por defecto).
- Variables de entorno expuestas automáticamente al backend.
- Configuración: La URL de conexión se inyecta vía DATABASE_URL en el servicio del backend.

## ⚙️ Backend (FastAPI)

- Servicio: Render Web Service.
- Build Command: pip install -r requirements.txt
- Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
- Variables de entorno clave:
- DATABASE_URL: conexión a PostgreSQL.
- ENVIRONMENT: production (activa pooling de conexiones optimizado).
- SECRET_KEY: clave para sesiones/firmas.
- CORS_ORIGINS: origen del frontend desplegado.

## 🎨 Frontend (React)

- Servicio: Render Static Site.
- Build Command: npm install && npm run build
- Publish Directory: dist (o build según configuración).
- Variables de entorno (frontend):

💡 VITE_API_BASE_URL: URL pública del backend (https://proyecto2-grupo1.onrender.com/api/v1).

✅ Cada servicio en Render se conecta automáticamente entre sí mediante las variables de entorno o URLs públicas. Render gestiona los certificados SSL y la red interna para comunicaciones seguras.

## 🧪 Entornos y Ciclo de Vida

| Entorno      | Backend URL                                   | Frontend URL                    | DB                |
| ------------ | --------------------------------------------- | --------------------------------| ----------------- |
| Producción   | https://proyecto2-grupo1.onrender.com/api/v1  | https://musintage.onrender.com  | PostgreSQL (SSL)  |
| Local        | http://localhost:8000                         | http://localhost:5173           | MySQL system Logs |


* Despliegue continuo: Cada push a las ramas main o develop activa un nuevo despliegue en Render.

* Rollbacks: Render permite revertir a despliegues anteriores con un clic.

## 📁 Estructura del Monorepo

```bash
musintage/
├── backend/
│   ├── config/
│   ├── database/
│   ├── routes/
│   ├── controllers/
│   ├── schemas/
│   ├── utils/
│   ├── requirements.txt
│   └── main.py
├── frontend/
│   ├── public/
│   ├── src/
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
└── README.md

```

## 🔧 Requisitos Locales

- Python 3.10+

- Node.js 18+

- PostgreSQL (local o Docker)

- pip y npm

## 🏁 Comandos Rápidos para Desarrollo

```bash
# Backend (desde la raíz del monorepo)
cd backend
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend (desde la raíz)
cd frontend
npm install
npm run dev

´´´
