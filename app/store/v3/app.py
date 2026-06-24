from fastapi import FastAPI
from app.store.v3.routers import products, orders, categories

store_v3 = FastAPI(
    title="Store API",
    version="3.0.0",
    description=(
        "**v3 — Rich Objects and Pagination**\n\n"
        "**Breaking (!):** `price: float` → nested `{amount, currency}`; `customer_name: str` → nested `customer` object; product list paginated.\n\n"
        "**Non-breaking (+):** `GET /categories`; optional `Product.tags`."
    ),
    docs_url="/docs", redoc_url="/redoc", openapi_url="/openapi.json",
)

store_v3.include_router(products.router)
store_v3.include_router(orders.router)
store_v3.include_router(categories.router)
