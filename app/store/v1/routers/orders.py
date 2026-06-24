from fastapi import APIRouter, HTTPException
from typing import List
from app.store.v1.schemas import Order
from app.store.v1.data import ORDERS

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.get("", response_model=List[Order])
def list_orders():
    return ORDERS


@router.get("/{order_id}", response_model=Order)
def get_order(order_id: int):
    for order in ORDERS:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")
