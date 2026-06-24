from pydantic import BaseModel
from typing import Optional, List


class ProductCategory(BaseModel):
    id: int
    name: str
    slug: str


class Price(BaseModel):
    amount: float
    currency: str


class CustomerDetail(BaseModel):
    id: int
    name: str
    email: str


class Product(BaseModel):
    id: int
    name: str
    price: Price                      # BREAKING: was float, now nested object
    category: ProductCategory
    stock: int
    description: Optional[str] = None
    tags: Optional[List[str]] = None  # NON-BREAKING: new optional field


class ProductListResponse(BaseModel):  # BREAKING: list wrapped in pagination envelope
    data: List[Product]
    total: int
    page: int
    page_size: int


class Order(BaseModel):
    id: int
    customer: CustomerDetail          # BREAKING: was customer_name: str, now nested object
    product_ids: List[int]
    total_amount: float
    status: str


class Category(BaseModel):           # NON-BREAKING: new entity in v3
    id: int
    name: str
    slug: str
    product_count: int
