from app.store.v1.schemas import Product, Order

PRODUCTS = [
    Product(id=1, name="Wireless Headphones", price=89.99,
            category="Electronics", stock=42),
    Product(id=2, name="Running Shoes", price=129.99,
            category="Footwear", stock=15),
    Product(id=3, name="Coffee Maker", price=54.99,
            category="Kitchen", stock=30),
    Product(id=4, name="Yoga Mat", price=34.99,
            category="Sports", stock=80),
]

ORDERS = [
    Order(id=1, customer_name="Alice Chen",
          product_ids=[1, 3], total=144.98, status="delivered"),
    Order(id=2, customer_name="Bob Martinez",
          product_ids=[2], total=129.99, status="shipped"),
    Order(id=3, customer_name="Carol Smith",
          product_ids=[4, 4], total=69.98, status="processing"),
]
