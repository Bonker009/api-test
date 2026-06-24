from fastapi import APIRouter, HTTPException
from typing import List
from app.v2.schemas import Artwork
from app.v2.data import ARTWORKS

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


@router.get("/{artwork_id}/related", response_model=List[Artwork],
            summary="Get related artworks [NON-BREAKING: new in v2]")
def get_related_artworks(artwork_id: int):
    target = next((a for a in ARTWORKS if a.id == artwork_id), None)
    if not target:
        raise HTTPException(status_code=404, detail="Artwork not found")
    return [a for a in ARTWORKS if a.medium == target.medium and a.id != artwork_id]
