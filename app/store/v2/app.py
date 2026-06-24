from fastapi import FastAPI
from app.store.v2.routers import products, orders

store_v2 = FastAPI(
    title="Store API",
    version="2.0.0",
    description=(
        "**v2 — Structural Changes**\n\n"
        "**Breaking (!):** `category: str` → nested `{id, name, slug}`; `total` → `total_amount`.\n\n"
        "**Non-breaking (+):** `GET /products/{id}/related`; optional `Product.description`."
    ),
    docs_url="/docs", redoc_url="/redoc", openapi_url="/openapi.json",
)

store_v2.include_router(products.router)
store_v2.include_router(orders.router)
