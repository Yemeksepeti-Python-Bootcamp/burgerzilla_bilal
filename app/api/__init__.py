from flask_restx import Api
from flask import Blueprint

from .customer.controller import api as customer_ns
from .restaurant.controller import api as restaurant_ns
# from .restaurant.controller import menu_model as menu_ns
# from .restaurant.controller import order_model as order_ns


api_bp = Blueprint("api", __name__)
api = Api(api_bp, version="1.", title="API", description="API")


api.add_namespace(customer_ns)
api.add_namespace(restaurant_ns)
# api.add_namespace(menu_ns)
# api.add_namespace(order_ns)

