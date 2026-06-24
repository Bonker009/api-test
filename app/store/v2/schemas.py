from pydantic import BaseModel
from typing import Optional, List


class ProductCategory(BaseModel):
    id: int
    name: str
    slug: str


class Product(BaseModel):
    id: int
    name: str
    price: float
    category: ProductCategory         # BREAKING: was str, now nested object
    stock: int
    description: Optional[str] = None  # NON-BREAKING: new optional field


class Order(BaseModel):
    id: int
    customer_name: str
    product_ids: List[int]
    total_amount: float               # BREAKING: renamed from "total"
    status: str
