from flask import current_app

from app.utils import err_resp, internal_err_resp, message
from app.models.users import User
from app.models.order import Order, OrderItem
from app.models.restaurant import Restaurant, Menu, Product
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.api.customer.utils import get_customer_id
from app import db


class RestaurantService:

    @staticmethod
    def get_restaurant_data(restaurant_name):
        """
        get restaurant data
        """

        if not (restaurant := Restaurant.query.filter_by(username=restaurant_name).first()):
            return err_resp("Restaurant Not Found", "user_404", 404)

        from .utils import load_data

        try:
            restaurant_data = load_data(restaurant)
            resp = message(True, "Restaurant data sent")
            resp["user"] = restaurant_data
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def update_restaurant_data(restaurant_name, data):
        """
        update restaurant data
        """

        if not (restaurant := Restaurant.query.filter_by(username=restaurant_name).first()):
            return err_resp("Restaurant Not Found", "user_404", 404)

        try:
            restaurant.name = data["name"]
            restaurant.email = data["email"]
            restaurant.username = data["username"]
            restaurant.restaurant_name = data["restaurant_name"]
            restaurant.menu_name = data["menu_name"]

            db.session.commit()
            resp = message(True, "Restaurant data updated")
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def delete_restaurant_data(restaurant_name):
        """
        delete restaurant data
        """

        if not (restaurant := Restaurant.query.filter_by(username=restaurant_name).first()):
            return err_resp("Restaurant Not Found", "user_404", 404)

        try:
            db.session.delete(restaurant)
            db.session.commit()
            resp = message(True, "Restaurant data deleted")
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def create_restaurant(data):
        """
        create restaurant
        """

        try:
            restaurant = Restaurant(
                name=data["name"],
                email=data["email"],
                username=data["username"],
                restaurant_name=data["restaurant_name"],
                menu_name=data["menu_name"]
            )
            db.session.add(restaurant)
            db.session.commit()
            resp = message(True, "Restaurant created")
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def get_all_restaurants():
        """
        get all restaurants
        """

        try:
            restaurants = Restaurant.query.all()
            resp = message(True, "Restaurants sent")
            resp["restaurants"] = restaurants
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def get_restaurant_menu(restaurant_name):
        """
        get restaurant menu
        """

        if not (restaurant := Restaurant.query.filter_by(username=restaurant_name).first()):
            return err_resp("Restaurant Not Found", "user_404", 404)

        try:
            menu = Menu.query.filter_by(restaurant_id=restaurant.id).all()
            resp = message(True, "Menu sent")
            resp["menu"] = menu
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def delete_restaurant_menu(restaurant_name, menu_name):
        """
        delete restaurant menu
        """

        if not (restaurant := Restaurant.query.filter_by(username=restaurant_name).first()):
            return err_resp("Restaurant Not Found", "user_404", 404)

        if not (menu := Menu.query.filter_by(restaurant_id=restaurant.id, name=menu_name).first()):
            return err_resp("Menu Not Found", "user_404", 404)

        try:
            db.session.delete(menu)
            db.session.commit()
            resp = message(True, "Menu deleted")
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def get_restaurant_products(restaurant_name):
        """
        get restaurant menu items
        """

        if not (restaurant := Restaurant.query.filter_by(username=restaurant_name).first()):
            return err_resp("Restaurant Not Found", "user_404", 404)

        try:
            products = Product.query.filter_by(restaurant_id=restaurant.id).all()
            resp = message(True, "Products sent")
            resp["products"] = products
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def get_restaurant_orders(restaurant_name):
        """
        get restaurant orders
        """

        if not (restaurant := Restaurant.query.filter_by(username=restaurant_name).first()):
            return err_resp("Restaurant Not Found", "user_404", 404)

        try:
            orders = Order.query.filter_by(restaurant_id=restaurant.id).all()
            resp = message(True, "Orders sent")
            resp["orders"] = orders
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def get_restaurant_order_items(restaurant_name, order_id):
        """
        get restaurant order items
        """

        if not (restaurant := Restaurant.query.filter_by(username=restaurant_name).first()):
            return err_resp("Restaurant Not Found", "user_404", 404)

        try:
            order_items = OrderItem.query.filter_by(order_id=order_id).all()
            resp = message(True, "Order Items sent")
            resp["order_items"] = order_items['product_id']
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def delete_restaurant_orders(restaurant_name):
        """
        delete all orders
        """

        if not (restaurant := Restaurant.query.filter_by(username=restaurant_name).first()):
            return err_resp("Restaurant Not Found", "user_404", 404)

        try:
            orders = Order.query.filter_by(restaurant_id=restaurant.id).all()
            for order in orders:
                db.session.delete(order)
            db.session.commit()
            resp = message(True, "Orders deleted")
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def delete_restaurant_order_items(restaurant_name, order_id):
        """
        delete individual orders
        """

        if not (restaurant := Restaurant.query.filter_by(username=restaurant_name).first()):
            return err_resp("Restaurant Not Found", "user_404", 404)

        try:
            order_items = OrderItem.query.filter_by(order_id=order_id).all()
            for order_item in order_items:
                db.session.delete(order_item)
            db.session.commit()
            resp = message(True, "Order Items deleted")
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def change_order_status(restaurant_name, order_id, status):
        """
        change order status
        """

        if not (restaurant := Restaurant.query.filter_by(username=restaurant_name).first()):
            return err_resp("Restaurant Not Found", "user_404", 404)

        try:
            order = Order.query.filter_by(id=order_id).first()
            order.status = status
            db.session.commit()
            resp = message(True, "Order status changed")
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def create_restaurant_menu(restaurant_name, menu):
        """
        create restaurant menu
        """

        if not (restaurant := Restaurant.query.filter_by(username=restaurant_name).first()):
            return err_resp("Restaurant Not Found", "user_404", 404)

        try:
            for item in menu:
                product = Product(item['name'], item['price'], item['description'], item['image'])
                product.restaurant_id = restaurant.id
                db.session.add(product)
            db.session.commit()
            resp = message(True, "Menu created")
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def update_restaurant_menu(restaurant_name, menu):
        """
        update restaurant menu
        """

        if not (restaurant := Restaurant.query.filter_by(username=restaurant_name).first()):
            return err_resp("Restaurant Not Found", "user_404", 404)

        try:
            restaurant.menu = menu
            db.session.commit()
            resp = message(True, "Menu updated")
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def add_item_to_restaurant_menu(restaurant_name, item):
        """
        add item to restaurant menu
        """

        if not (restaurant := Restaurant.query.filter_by(username=restaurant_name).first()):
            return err_resp("Restaurant Not Found", "user_404", 404)

        try:
            restaurant.menu.append(item)
            db.session.commit()
            resp = message(True, "Item added to menu")
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def update_item_in_restaurant_menu(restaurant_name, item_id, item):
        """
        update an item in restaurant menu
        """

        if not (restaurant := Restaurant.query.filter_by(username=restaurant_name).first()):
            return err_resp("Restaurant Not Found", "user_404", 404)

        try:
            restaurant.menu[item_id] = item
            db.session.commit()
            resp = message(True, "Item updated")
            return resp, 200

        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def delete_item_from_restaurant_menu(restaurant_name, item_id):
        """
        delete an item from restaurant menu
        """

        if not (restaurant := Restaurant.query.filter_by(username=restaurant_name).first()):
            return err_resp("Restaurant Not Found", "user_404", 404)

        try:
            del restaurant.menu[item_id]
            db.session.commit()
            resp = message(True, "Item deleted")
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def create_restaurant_product(restaurant_name, product):
        """
        create restaurant product
        """

        if not (restaurant := Restaurant.query.filter_by(username=restaurant_name).first()):
            return err_resp("Restaurant Not Found", "user_404", 404)

        try:
            product = Product(product['name'], product['price'], product['description'], product['image'])
            product.restaurant_id = restaurant.id
            product.menu_id = restaurant.menu_id
            db.session.add(product)
            db.session.commit()
            resp = message(True, "Product created")
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()



