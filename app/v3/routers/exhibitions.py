from fastapi import APIRouter, HTTPException
from typing import List
from app.v3.schemas import Exhibition
from app.v3.data import EXHIBITIONS

router = APIRouter(prefix="/exhibitions", tags=["Exhibitions"])


@router.get("", response_model=List[Exhibition],
            summary="List exhibitions [NON-BREAKING: new in v3]")
def list_exhibitions():
    return EXHIBITIONS


@router.get("/{exhibition_id}", response_model=Exhibition)
def get_exhibition(exhibition_id: int):
    for exhibition in EXHIBITIONS:
        if exhibition.id == exhibition_id:
            return exhibition
    raise HTTPException(status_code=404, detail="Exhibition not found")
