from fastapi import FastAPI
from app.cinema.v2.routers import movies, showtimes

cinema_v2 = FastAPI(
    title="Cinema Booking API",
    version="2.0.0",
    description=(
        "**v2 — Structural Changes**\n\n"
        "**Breaking (!):** `year` → `release_year`; `Showtime.screen` → nested `venue` object; `available_seats` removed.\n\n"
        "**Non-breaking (+):** `GET /movies/{id}/showtimes`; optional `Movie.rating`."
    ),
    docs_url="/docs", redoc_url="/redoc", openapi_url="/openapi.json",
)

cinema_v2.include_router(movies.router)
cinema_v2.include_router(showtimes.router)
