from fastapi import APIRouter, Query
from typing import Optional

router = APIRouter()

@router.get("/ping", tags=["health"])
def ping():
    return {"status": "ok"}

@router.get("/discos")
def get_discos(
    genero: Optional[str] = Query(default=None),
    artista: Optional[str] = Query(default=None),
):
    return []
