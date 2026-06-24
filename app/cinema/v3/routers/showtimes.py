from fastapi import APIRouter, HTTPException, Query
from app.cinema.v3.schemas import Showtime, ShowtimeListResponse
from app.cinema.v3.data import SHOWTIMES

router = APIRouter(prefix="/showtimes", tags=["Showtimes"])


@router.get("", response_model=ShowtimeListResponse,
            summary="List showtimes [BREAKING: paginated envelope in v3]")
def list_showtimes(page: int = Query(1, ge=1), page_size: int = Query(10, ge=1, le=100)):
    start = (page - 1) * page_size
    end = start + page_size
    return ShowtimeListResponse(
        data=SHOWTIMES[start:end],
        total=len(SHOWTIMES),
        page=page,
        page_size=page_size,
    )


@router.get("/{showtime_id}", response_model=Showtime)
def get_showtime(showtime_id: int):
    for showtime in SHOWTIMES:
        if showtime.id == showtime_id:
            return showtime
    raise HTTPException(status_code=404, detail="Showtime not found")
