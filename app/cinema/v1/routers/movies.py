from fastapi import APIRouter, HTTPException
from typing import List
from app.cinema.v1.schemas import Movie
from app.cinema.v1.data import MOVIES

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
