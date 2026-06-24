from fastapi import APIRouter, HTTPException
from typing import List
from app.cinema.v2.schemas import Showtime
from app.cinema.v2.data import SHOWTIMES

router = APIRouter(prefix="/showtimes", tags=["Showtimes"])


@router.get("", response_model=List[Showtime])
def list_showtimes():
    return SHOWTIMES


@router.get("/{showtime_id}", response_model=Showtime)
def get_showtime(showtime_id: int):
    for showtime in SHOWTIMES:
        if showtime.id == showtime_id:
            return showtime
    raise HTTPException(status_code=404, detail="Showtime not found")
