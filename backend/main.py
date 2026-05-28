from fastapi import FastAPI
from schemas.album import AlbumCreate
from database import database



app = FastAPI()


@app.get("/")
def root():
    return {"mensaje": "API tienda de musica"}

@app.post("/album")
def crear_album(album: AlbumCreate):
    return album 



#IMPORTANTE: Aquí referenciamos el archivo "database" no la variable "db"


def run():
    pass
if __name__ == '__main__':
    database.Base.metadata.create_all(database.engine)
    run()

