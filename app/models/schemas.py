from app import ma
from .users import User
from .dataset import Dataset


class CustomerSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "email", "name", "username", "password_hash", "order", "role")


class RestaurantSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "email", "name", "username", "restaurant_name", "password_hash", "menu", "orders", "role")


class MenuSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "restaurant_id", "menu_name", "products")


class ProductSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "restaurant_id", "menu_id", "product_name", "price", "description", "image")


class OrderSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "order_id", "customer_id", "restaurant_id", "order_date", "order_status")


class OrderItemSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "customer_id", "restaurant_id", "product_id", "products", "price", "quantity", "total_price", "date_added", "date_updated")
