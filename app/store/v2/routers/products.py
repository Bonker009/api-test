from fastapi import APIRouter, HTTPException
from typing import List
from app.store.v2.schemas import Product
from app.store.v2.data import PRODUCTS

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


@router.get("/{product_id}/related", response_model=List[Product],
            summary="Get products in same category [NON-BREAKING: new in v2]")
def get_related_products(product_id: int):
    target = next((p for p in PRODUCTS if p.id == product_id), None)
    if not target:
        raise HTTPException(status_code=404, detail="Product not found")
    return [p for p in PRODUCTS
            if p.category.slug == target.category.slug and p.id != product_id]
