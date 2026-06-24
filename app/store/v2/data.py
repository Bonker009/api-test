from app.store.v2.schemas import Product, Order, ProductCategory

PRODUCTS = [
    Product(id=1, name="Wireless Headphones", price=89.99,
            category=ProductCategory(id=10, name="Electronics", slug="electronics"),
            stock=42,
            description="Premium noise-cancelling wireless headphones with 30hr battery."),
    Product(id=2, name="Running Shoes", price=129.99,
            category=ProductCategory(id=11, name="Footwear", slug="footwear"),
            stock=15),
    Product(id=3, name="Coffee Maker", price=54.99,
            category=ProductCategory(id=12, name="Kitchen", slug="kitchen"),
            stock=30,
            description="12-cup programmable coffee maker with thermal carafe."),
    Product(id=4, name="Yoga Mat", price=34.99,
            category=ProductCategory(id=13, name="Sports", slug="sports"),
            stock=80),
]

ORDERS = [
    Order(id=1, customer_name="Alice Chen",
          product_ids=[1, 3], total_amount=144.98, status="delivered"),
    Order(id=2, customer_name="Bob Martinez",
          product_ids=[2], total_amount=129.99, status="shipped"),
    Order(id=3, customer_name="Carol Smith",
          product_ids=[4, 4], total_amount=69.98, status="processing"),
]
