from fastapi import APIRouter, HTTPException
from typing import List
from app.cinema.v2.schemas import Movie, Showtime
from app.cinema.v2.data import MOVIES, SHOWTIMES

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.get("", response_model=List[Movie])
def list_movies():
    return MOVIES


@router.get("/{movie_id}", response_model=Movie)
def get_movie(movie_id: int):
    for movie in MOVIES:
        if movie.id == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")


@router.get("/{movie_id}/showtimes", response_model=List[Showtime],
            summary="Get showtimes for a movie [NON-BREAKING: new in v2]")
def get_movie_showtimes(movie_id: int):
    if not any(m.id == movie_id for m in MOVIES):
        raise HTTPException(status_code=404, detail="Movie not found")
    return [s for s in SHOWTIMES if s.movie_id == movie_id]
