from fastapi import APIRouter, HTTPException
from typing import List
from app.cinema.v3.schemas import Booking
from app.cinema.v3.data import BOOKINGS

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.get("", response_model=List[Booking],
            summary="List bookings [NON-BREAKING: new in v3]")
def list_bookings():
    return BOOKINGS


@router.get("/{booking_id}", response_model=Booking)
def get_booking(booking_id: int):
    for booking in BOOKINGS:
        if booking.id == booking_id:
            return booking
    raise HTTPException(status_code=404, detail="Booking not found")
