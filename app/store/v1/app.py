from fastapi import FastAPI
from app.store.v1.routers import products, orders

store_v1 = FastAPI(
    title="Store API",
    version="1.0.0",
    description="**v1 — Baseline**\n\nProducts with flat `category` string and `price` float. Orders with flat `customer_name` and `total`.",
    docs_url="/docs", redoc_url="/redoc", openapi_url="/openapi.json",
)

store_v1.include_router(products.router)
store_v1.include_router(orders.router)
