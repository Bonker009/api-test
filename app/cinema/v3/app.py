from fastapi import FastAPI
from app.cinema.v3.routers import movies, showtimes, bookings

cinema_v3 = FastAPI(
    title="Cinema Booking API",
    version="3.0.0",
    description=(
        "**v3 — Rich Objects and Pagination**\n\n"
        "**Breaking (!):** `director: str` → nested `{name, nationality}`; `genre: str` → `genres: List[str]`; showtime list paginated.\n\n"
        "**Non-breaking (+):** `GET /bookings`; optional `Movie.cast`."
    ),
    docs_url="/docs", redoc_url="/redoc", openapi_url="/openapi.json",
)

cinema_v3.include_router(movies.router)
cinema_v3.include_router(showtimes.router)
cinema_v3.include_router(bookings.router)
