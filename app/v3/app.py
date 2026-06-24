from fastapi import FastAPI
from app.v3.routers import artworks, galleries, exhibitions

v3_app = FastAPI(
    title="Gallery Museum API",
    version="3.0.0",
    description=(
        "**v3 — Rich Objects and Pagination**\n\n"
        "**Breaking changes (!):**\n"
        "- `artist_name: str` replaced by `artist: {id, name, nationality}` nested object\n"
        "- `year: int` replaced by `created_at: str` (ISO 8601 date, e.g. `1889-06-01`)\n"
        "- `GET /artworks` response wrapped in pagination envelope `{data, total, page, page_size}`\n"
        "- `Gallery.name` renamed to `Gallery.title`\n\n"
        "**Non-breaking additions (+):**\n"
        "- `GET /exhibitions` — new endpoint with new Exhibition entity\n"
        "- `Artwork.tags` — new optional field\n"
        "- `Gallery.curator` — new optional field"
    ),
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

v3_app.include_router(artworks.router)
v3_app.include_router(galleries.router)
v3_app.include_router(exhibitions.router)
