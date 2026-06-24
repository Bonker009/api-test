from pydantic import BaseModel
from typing import Optional


class ShowtimeVenue(BaseModel):
    screen: str
    hall: str
    capacity: int


class Movie(BaseModel):
    id: int
    title: str
    director: str
    release_year: int             # BREAKING: renamed from "year"
    genre: str
    duration_min: int
    rating: Optional[float] = None  # NON-BREAKING: new optional field


class Showtime(BaseModel):
    id: int
    movie_id: int
    date: str
    time: str
    venue: ShowtimeVenue           # BREAKING: was screen: str, now nested object
    # available_seats removed      # BREAKING
