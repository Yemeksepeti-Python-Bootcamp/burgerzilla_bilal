from flask import current_app

from app.utils import err_resp, internal_err_resp, message
from app.models.users import User
from app.models.order import Order, OrderItem
from app.models.restaurant import Restaurant, Menu, Product
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.api.customer.utils import get_customer_id
from app import db


class CustomerService:

    @staticmethod
    def get_customer_data(username):
        """
        get user data"""
        if not (user := User.query.filter_by(username=username).first()):
            return err_resp("User Not Found", "user_404", 404)

        from .utils import load_data

        try:
            user_data = load_data(user)
            resp = message(True, "User data sent")
            resp["user"] = user_data
            return resp, 200
        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def get_restaurant_menu(username, restaurant_id):
        """
        get restaurant menu
        """
        if not (user := User.query.filter_by(username=username).first()):
            return err_resp("User Not Found", "user_404", 404)

        from app.api.restaurant.utils import get_restaurant_menu

        try:
            current_user = get_jwt_identity()
            restaurant_menu = get_restaurant_menu(restaurant_id)
            resp = message(True, "Restaurant menu sent")
            resp["menu"] = restaurant_menu
            return resp, 200

        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def create_order(username, order):
        """
        create order
        """
        if not (user := User.query.filter_by(username=username).first()):
            return err_resp("User Not Found", "user_404", 404)

        try:
            current_user = get_jwt_identity()
            order = OrderItem(customer_id=current_user, restaurant_id=order["restaurant_id"],
                              product_id=order["product_id"], quantity=order["quantity"],
                              total_price=(order["quantity"] * order["price"]))
            db.session.add(order)
            db.session.commit()
            return message(True, "Order created successfully")

        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def create_order_by_user_id(user_id, order):
        """
        create order
        """
        try:
            order = OrderItem(customer_id=user_id, restaurant_id=order["restaurant_id"],
                              product_id=order["product_id"], quantity=order["quantity"],
                              total_price=(order["quantity"] * order["price"]))
            db.session.add(order)
            db.session.commit()
            return message(True, "Order created successfully")

        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def get_order_details(username, order_id):
        """
        order details
        """
        if not (user := User.query.filter_by(username=username).first()):
            return err_resp("User Not Found", "user_404", 404)

        from .utils import get_customer_order

        try:
            current_user = get_jwt_identity()
            user_order = get_customer_order(current_user, order_id)
            resp = message(True, "User order details sent")
            resp["order"] = user_order
            return resp, 200

        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def get_order_details_by_user_id(user_id, order_id):
        """
        order details
        """
        from .utils import get_customer_order

        try:
            user_order = get_customer_order(user_id, order_id)
            resp = message(True, "User order details sent")
            resp["order"] = user_order
            return resp, 200

        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def update_order(username, order_id, new_order):
        """
        order update
        """
        if not (user := User.query.filter_by(username=username).first()):
            return err_resp("User Not Found", "user_404", 404)

        from .utils import load_data

        try:
            current_user = get_jwt_identity()
            order = OrderItem.query.filter_by(id=order_id, customer_id=current_user).first()
            if not order:
                return err_resp("Order Not Found", "order_404", 404)

            order.product_id = new_order["product_id"]
            order.quantity = new_order["quantity"]
            order.total_price = (new_order["quantity"] * new_order["price"])
            db.session.add(order)
            db.session.commit()
            return message(True, "Order updated successfully")

        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def update_order_by_user_id(user_id, order_id, new_order):
        """
        order update by user id
        """
        from .utils import load_data

        try:
            order = OrderItem.query.filter_by(id=order_id, customer_id=user_id).first()
            if not order:
                return err_resp("Order Not Found", "order_404", 404)

            order.product_id = new_order["product_id"]
            order.quantity = new_order["quantity"]
            order.total_price = (new_order["quantity"] * new_order["price"])
            db.session.add(order)
            db.session.commit()
            return message(True, "Order updated successfully")

        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def delete_order(username, order_id):
        """
        deleting an order
        """
        if not (user := User.query.filter_by(username=username).first()):
            return err_resp("User Not Found", "user_404", 404)

        from .utils import get_customer_order

        try:
            current_user = get_jwt_identity()
            order = get_customer_order(current_user, order_id)
            if not order:
                return err_resp("Order Not Found", "order_404", 404)

            db.session.delete(order)
            db.session.commit()
            return message(True, "Order deleted successfully")

        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def delete_order_by_user_id(user_id, order_id):
        """
        deleting an order by user id
        """
        from .utils import get_customer_order

        try:
            order = get_customer_order(user_id, order_id)
            if not order:
                return err_resp("Order Not Found", "order_404", 404)

            db.session.delete(order)
            db.session.commit()
            return message(True, "Order deleted successfully")

        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def delete_all_orders_by_user_id(user_id):
        """
        deleting an order by user id
        """
        try:
            orders = OrderItem.query.filter_by(customer_id=user_id).first()
            if not orders:
                return err_resp("Order Not Found", "order_404", 404)

            db.session.delete(orders)
            db.session.commit()
            return message(True, "Order deleted successfully")

        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def get_orders(username):
        """
        get all orders
        """
        if not (user := User.query.filter_by(username=username).first()):
            return err_resp("User Not Found", "user_404", 404)

        from .utils import get_customer_orders

        try:
            current_user = get_jwt_identity()
            orders = get_customer_orders(current_user)
            resp = message(True, "User orders sent")
            resp["orders"] = orders
            return resp, 200

        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def get_orders_by_user_id(user_id):
        """
        get order by id
        """
        if not (user := User.query.filter_by(username=user_id).first()):
            return err_resp("User Not Found", "user_404", 404)

        from .utils import get_customer_orders

        try:
            current_user = get_jwt_identity()
            order = get_customer_orders(user_id)
            resp = message(True, "User order sent")
            resp["order"] = order
            return resp, 200

        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def delete_customer_data(username):
        """
        deleting a user
        """
        if not (user := User.query.filter_by(username=username).first()):
            return err_resp("User Not Found", "user_404", 404)

        try:
            db.session.delete(user)
            db.session.commit()
            return message(True, "User deleted successfully")

        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def update_customer_data(username, new_user):
        """
        updating a user
        """
        if not (user := User.query.filter_by(username=username).first()):
            return err_resp("User Not Found", "user_404", 404)

        try:
            first_name = new_user["first_name"]
            last_name = new_user["last_name"]
            user.name = f"{first_name} {last_name}"
            user.email = new_user["email"]
            db.session.add(user)
            db.session.commit()
            return message(True, "User updated successfully")

        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def change_password(username, old_password, new_password):
        """
        changing a user password
        """
        if not (user := User.query.filter_by(username=username).first()):
            return err_resp("User Not Found", "user_404", 404)

        if not (user.check_password(old_password)):
            return err_resp("Old password is incorrect", "old_password_incorrect", 400)

        try:
            user.password = new_password
            db.session.add(user)
            db.session.commit()
            return message(True, "User password updated successfully")

        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def get_all_customer_data():
        """
        get all users
        """
        try:
            users = User.query.all()
            resp = message(True, "All users sent")
            resp["users"] = users
            return resp, 200

        except Exception as e:
            print("Error User:", e)
            current_app.logger.error(e)
            return internal_err_resp()
