from fastapi import FastAPI
from app.v1.routers import artworks, galleries

v1_app = FastAPI(
    title="Gallery Museum API",
    version="1.0.0",
    description=(
        "**v1 — Baseline**\n\n"
        "Artworks with flat `artist` string and integer `year`. "
        "Galleries with flat `location` string and `capacity` field."
    ),
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

v1_app.include_router(artworks.router)
v1_app.include_router(galleries.router)
