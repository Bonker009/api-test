from fastapi import APIRouter, HTTPException
from typing import List
from app.v1.schemas import Artwork
from app.v1.data import ARTWORKS

router = APIRouter(prefix="/artworks", tags=["Artworks"])


@router.get("", response_model=List[Artwork])
def list_artworks():
    return ARTWORKS


@router.get("/{artwork_id}", response_model=Artwork)
def get_artwork(artwork_id: int):
    for artwork in ARTWORKS:
        if artwork.id == artwork_id:
            return artwork
    raise HTTPException(status_code=404, detail="Artwork not found")
