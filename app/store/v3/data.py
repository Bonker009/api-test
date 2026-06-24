from app.store.v3.schemas import Product, Order, ProductCategory, Price, CustomerDetail, Category

PRODUCTS = [
    Product(id=1, name="Wireless Headphones",
            price=Price(amount=89.99, currency="USD"),
            category=ProductCategory(id=10, name="Electronics", slug="electronics"),
            stock=42,
            description="Premium noise-cancelling wireless headphones with 30hr battery.",
            tags=["audio", "wireless", "noise-cancelling"]),
    Product(id=2, name="Running Shoes",
            price=Price(amount=129.99, currency="USD"),
            category=ProductCategory(id=11, name="Footwear", slug="footwear"),
            stock=15,
            tags=["sport", "running", "outdoor"]),
    Product(id=3, name="Coffee Maker",
            price=Price(amount=54.99, currency="USD"),
            category=ProductCategory(id=12, name="Kitchen", slug="kitchen"),
            stock=30,
            description="12-cup programmable coffee maker with thermal carafe.",
            tags=["kitchen", "coffee", "appliance"]),
    Product(id=4, name="Yoga Mat",
            price=Price(amount=34.99, currency="USD"),
            category=ProductCategory(id=13, name="Sports", slug="sports"),
            stock=80,
            tags=["fitness", "yoga", "sport"]),
]

ORDERS = [
    Order(id=1, customer=CustomerDetail(id=201, name="Alice Chen", email="alice@example.com"),
          product_ids=[1, 3], total_amount=144.98, status="delivered"),
    Order(id=2, customer=CustomerDetail(id=202, name="Bob Martinez", email="bob@example.com"),
          product_ids=[2], total_amount=129.99, status="shipped"),
    Order(id=3, customer=CustomerDetail(id=203, name="Carol Smith", email="carol@example.com"),
          product_ids=[4, 4], total_amount=69.98, status="processing"),
]

CATEGORIES = [
    Category(id=10, name="Electronics", slug="electronics", product_count=1),
    Category(id=11, name="Footwear",    slug="footwear",    product_count=1),
    Category(id=12, name="Kitchen",     slug="kitchen",     product_count=1),
    Category(id=13, name="Sports",      slug="sports",      product_count=1),
]
