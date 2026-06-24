from fastapi import APIRouter, HTTPException
from typing import List
from app.v2.schemas import Gallery
from app.v2.data import GALLERIES

router = APIRouter(prefix="/galleries", tags=["Galleries"])


@router.get("", response_model=List[Gallery])
def list_galleries():
    return GALLERIES


@router.get("/{gallery_id}", response_model=Gallery)
def get_gallery(gallery_id: int):
    for gallery in GALLERIES:
        if gallery.id == gallery_id:
            return gallery
    raise HTTPException(status_code=404, detail="Gallery not found")
