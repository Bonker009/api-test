from pydantic import BaseModel
from typing import Optional, List


class DirectorDetail(BaseModel):
    name: str
    nationality: str


class ShowtimeVenue(BaseModel):
    screen: str
    hall: str
    capacity: int


class Movie(BaseModel):
    id: int
    title: str
    director: DirectorDetail       # BREAKING: was str, now nested object
    release_year: int
    genres: List[str]              # BREAKING: renamed from genre: str, now a list
    duration_min: int
    rating: Optional[float] = None
    cast: Optional[List[str]] = None  # NON-BREAKING: new optional field


class ShowtimeListResponse(BaseModel):  # BREAKING: list wrapped in pagination envelope
    data: List["Showtime"]
    total: int
    page: int
    page_size: int


class Showtime(BaseModel):
    id: int
    movie_id: int
    date: str
    time: str
    venue: ShowtimeVenue


class Booking(BaseModel):           # NON-BREAKING: new entity in v3
    id: int
    showtime_id: int
    customer_name: str
    seats: int
    confirmed: bool


ShowtimeListResponse.model_rebuild()
