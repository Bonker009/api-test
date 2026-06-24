from fastapi import APIRouter, HTTPException
from typing import List
from app.store.v1.schemas import Product
from app.store.v1.data import PRODUCTS

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("", response_model=List[Product])
def list_products():
    return PRODUCTS


@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in PRODUCTS:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")
