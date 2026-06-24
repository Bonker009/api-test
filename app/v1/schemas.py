from pydantic import BaseModel


class Artwork(BaseModel):
    id: int
    title: str
    artist: str
    year: int
    medium: str


class Gallery(BaseModel):
    id: int
    name: str
    location: str
    capacity: int
