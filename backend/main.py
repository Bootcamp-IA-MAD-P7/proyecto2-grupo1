from fastapi import FastAPI
from schemas.album_schema import AlbumCreate

app = FastAPI()


@app.get("/")
def root():
    return {"mensaje": "Welcome to Musintage"}

@app.post("/albums")
def create_album(album: AlbumCreate):
    return album
