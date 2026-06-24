from fastapi import FastAPI
from app.v2.routers import artworks, galleries

v2_app = FastAPI(
    title="Gallery Museum API",
    version="2.0.0",
    description=(
        "**v2 — Structural Changes**\n\n"
        "**Breaking changes (!):**\n"
        "- `artist` renamed to `artist_name`\n"
        "- `Gallery.location` changed from `str` to nested `{city, country, address}` object\n"
        "- `Gallery.capacity` field removed\n\n"
        "**Non-breaking additions (+):**\n"
        "- `GET /artworks/{id}/related` — new endpoint\n"
        "- `Artwork.description` — new optional field\n"
        "- `Gallery.opening_hours` — new optional field"
    ),
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

v2_app.include_router(artworks.router)
v2_app.include_router(galleries.router)
