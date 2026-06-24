from pydantic import BaseModel
from typing import Optional


class GalleryLocation(BaseModel):
    city: str
    country: str
    address: str


class Artwork(BaseModel):
    id: int
    title: str
    artist_name: str          # BREAKING: renamed from "artist"
    year: int
    medium: str
    description: Optional[str] = None   # NON-BREAKING: new optional field


class Gallery(BaseModel):
    id: int
    name: str
    location: GalleryLocation           # BREAKING: was str, now nested object
    opening_hours: Optional[str] = None  # NON-BREAKING: new optional field
    # capacity removed — BREAKING
