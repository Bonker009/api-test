from pydantic import BaseModel


class Movie(BaseModel):
    id: int
    title: str
    director: str
    year: int
    genre: str
    duration_min: int


class Showtime(BaseModel):
    id: int
    movie_id: int
    date: str
    time: str
    screen: str
    available_seats: int
