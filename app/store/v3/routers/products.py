from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.store.v3.schemas import Product, ProductListResponse
from app.store.v3.data import PRODUCTS

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("", response_model=ProductListResponse,
            summary="List products [BREAKING: paginated envelope in v3]")
def list_products(page: int = Query(1, ge=1), page_size: int = Query(10, ge=1, le=100)):
    start = (page - 1) * page_size
    end = start + page_size
    return ProductListResponse(
        data=PRODUCTS[start:end],
        total=len(PRODUCTS),
        page=page,
        page_size=page_size,
    )


@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in PRODUCTS:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@router.get("/{product_id}/related", response_model=List[Product])
def get_related_products(product_id: int):
    target = next((p for p in PRODUCTS if p.id == product_id), None)
    if not target:
        raise HTTPException(status_code=404, detail="Product not found")
    return [p for p in PRODUCTS
            if p.category.slug == target.category.slug and p.id != product_id]
