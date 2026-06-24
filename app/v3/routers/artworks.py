from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.v3.schemas import Artwork, ArtworkListResponse
from app.v3.data import ARTWORKS

router = APIRouter(prefix="/artworks", tags=["Artworks"])


@router.get("", response_model=ArtworkListResponse,
            summary="List artworks [BREAKING: paginated envelope in v3]")
def list_artworks(page: int = Query(1, ge=1), page_size: int = Query(10, ge=1, le=100)):
    start = (page - 1) * page_size
    end = start + page_size
    return ArtworkListResponse(
        data=ARTWORKS[start:end],
        total=len(ARTWORKS),
        page=page,
        page_size=page_size,
    )


@router.get("/{artwork_id}", response_model=Artwork)
def get_artwork(artwork_id: int):
    for artwork in ARTWORKS:
        if artwork.id == artwork_id:
            return artwork
    raise HTTPException(status_code=404, detail="Artwork not found")


@router.get("/{artwork_id}/related", response_model=List[Artwork])
def get_related_artworks(artwork_id: int):
    target = next((a for a in ARTWORKS if a.id == artwork_id), None)
    if not target:
        raise HTTPException(status_code=404, detail="Artwork not found")
    return [a for a in ARTWORKS if a.medium == target.medium and a.id != artwork_id]
