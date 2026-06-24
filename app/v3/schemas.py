from pydantic import BaseModel
from typing import Optional, List


class ArtistDetail(BaseModel):
    id: int
    name: str
    nationality: str


class GalleryLocation(BaseModel):
    city: str
    country: str
    address: str


class Artwork(BaseModel):
    id: int
    title: str
    artist: ArtistDetail              # BREAKING: was artist_name: str, now nested object
    created_at: str                   # BREAKING: renamed from year, ISO 8601 date string
    medium: str
    description: Optional[str] = None
    tags: Optional[List[str]] = None  # NON-BREAKING: new optional field


class ArtworkListResponse(BaseModel):  # BREAKING: list now wrapped in pagination envelope
    data: List[Artwork]
    total: int
    page: int
    page_size: int


class Gallery(BaseModel):
    id: int
    title: str                         # BREAKING: renamed from "name"
    location: GalleryLocation
    opening_hours: Optional[str] = None
    curator: Optional[str] = None      # NON-BREAKING: new optional field


class Exhibition(BaseModel):
    id: int
    name: str
    start_date: str
    end_date: str
    gallery_id: int
    artwork_ids: List[int]
