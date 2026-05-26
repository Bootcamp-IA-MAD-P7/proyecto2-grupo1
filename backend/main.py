from fastapi import FastAPI
from schemas.disco import DiscoCreate

app = FastAPI()


@app.get("/")
def root():
    return {"mensaje": "API tienda de musica"}

@app.post("/discos")
def crear_disco(disco: DiscoCreate):
    return disco
