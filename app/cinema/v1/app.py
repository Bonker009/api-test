from fastapi import FastAPI
from app.cinema.v1.routers import movies, showtimes

cinema_v1 = FastAPI(
    title="Cinema Booking API",
    version="1.0.0",
    description="**v1 — Baseline**\n\nMovies with flat `director` string, `genre` string, and integer `year`. Showtimes with flat `screen` string and `available_seats`.",
    docs_url="/docs", redoc_url="/redoc", openapi_url="/openapi.json",
)

cinema_v1.include_router(movies.router)
cinema_v1.include_router(showtimes.router)
