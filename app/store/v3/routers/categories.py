from fastapi import APIRouter, HTTPException
from typing import List
from app.store.v3.schemas import Category
from app.store.v3.data import CATEGORIES

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("", response_model=List[Category],
            summary="List categories [NON-BREAKING: new in v3]")
def list_categories():
    return CATEGORIES


@router.get("/{category_id}", response_model=Category)
def get_category(category_id: int):
    for category in CATEGORIES:
        if category.id == category_id:
            return category
    raise HTTPException(status_code=404, detail="Category not found")
