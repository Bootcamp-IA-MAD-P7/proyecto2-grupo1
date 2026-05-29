from fastapi import FastAPI
from schemas.album import AlbumCreate
from backend.routes.routes import router

app = FastAPI()


@app.get("/")
def root():
    return {"mensaje": "Welcome to Musintage"}

@app.post("/discos")
def crear_disco(disco: DiscoCreate):
    return disco


app.include_router(router)
