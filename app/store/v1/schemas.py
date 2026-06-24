from pydantic import BaseModel
from typing import List


class Product(BaseModel):
    id: int
    name: str
    price: float
    category: str
    stock: int


class Order(BaseModel):
    id: int
    customer_name: str
    product_ids: List[int]
    total: float
    status: str
