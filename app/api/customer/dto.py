from flask_restx import Namespace, fields


class CustomerDto:
    api = Namespace("customer", description="Customer related operations")

    customer = api.model("Customer object", {
        "email": fields.String,
        "name": fields.String,
        "username": fields.String,
        "joined_date": fields.DateTime,
        "role": fields.String,
    })

    product = api.model("Product object", {
        "name": fields.String,
        "description": fields.String,
        "price": fields.Float,
        "image": fields.String,
    })

    orders = api.model("Order object", {
        "id": fields.Integer,
        "customer_id": fields.Integer,
        "restaurant_id": fields.Integer,
        "products": fields.List(fields.Nested(product)),
        "total_price": fields.Float,
        "order_date": fields.DateTime,
        "status": fields.String,
    })

    order_details = api.model("OrderDetails object", {
        "id": fields.Integer,
        "order_id": fields.Integer,
        "product_id": fields.Integer,
        "quantity": fields.Integer,
        "price": fields.Float,
    })

    customer_list = api.model("Customer list", {
        "customers": fields.List(fields.Nested(customer))
    })

    customer_update = api.model("Customer update", {
        "email": fields.String,
        "name": fields.String,
        "username": fields.String,
        "joined_date": fields.DateTime,
        "role": fields.String,
        "last_login": fields.DateTime,
        "orders": fields.List(fields.String),
    })

    customer_create = api.model("Customer create", {
        "email": fields.String,
        "name": fields.String,
        "username": fields.String,
        "joined_date": fields.DateTime,
        "role": fields.String,
        "last_login": fields.DateTime,
        "orders": fields.List(fields.String),
    })

    customer_delete = api.model("Customer delete", {
        "email": fields.String,
        "name": fields.String,
        "username": fields.String,
        "joined_date": fields.DateTime,
        "role": fields.String,
        "last_login": fields.DateTime,
        "orders": fields.List(fields.String),
    })

    customer_update_password = api.model("Customer update password", {
        "email": fields.String,
        "name": fields.String,
        "username": fields.String,
        "joined_date": fields.DateTime,
        "role": fields.String,
        "last_login": fields.DateTime,
        "orders": fields.List(fields.String),
        "password": fields.String,
    })

    customer_update_password_request = api.model("Customer update password request", {
        "email": fields.String,
        "name": fields.String,
        "username": fields.String,
        "joined_date": fields.DateTime,
        "role": fields.String,
        "last_login": fields.DateTime,
        "orders": fields.List(fields.String),
        "password": fields.String,
    })

    customer_update_password_response = api.model("Customer update password response", {
        "email": fields.String,
        "name": fields.String,
        "username": fields.String,
        "joined_date": fields.DateTime,
        "role": fields.String,
        "last_login": fields.DateTime,
        "orders": fields.List(fields.String),
        "password": fields.String,
    })

    customer_resp = api.model("Customer response", {
        "email": fields.String,
        "name": fields.String,
        "username": fields.String,
        "joined_date": fields.DateTime,
        "role": fields.String,
        "last_login": fields.DateTime,
        "orders": fields.List(fields.String),
    })

    customer_req = api.model("Customer request", {
        "email": fields.String,
        "name": fields.String,
        "username": fields.String,
        "joined_date": fields.DateTime,
        "role": fields.String,
        "last_login": fields.DateTime,
        "orders": fields.List(fields.String),
    })

    data_req = api.model("Data request", {
        "email": fields.String,
        "name": fields.String,
        "username": fields.String,
        "joined_date": fields.DateTime,
        "role": fields.String,
        "last_login": fields.DateTime,
        "orders": fields.List(fields.String),
        "password": fields.String,
    })

    data_resp = api.model("Customer data response", {
        "status": fields.Boolean,
        "message": fields.String,
        "user": fields.Nested(customer)
    })

    login_req = api.model("Login request", {
        "username": fields.String,
        "password": fields.String,
    })

    login_resp = api.model("Customer login response", {
        "status": fields.Boolean,
        "message": fields.String,
        "user": fields.Nested(customer)
    })

    register_req = api.model("Register request", {
        "email": fields.String,
        "name": fields.String,
        "username": fields.String,
        "joined_date": fields.DateTime,
        "role": fields.String,
        "last_login": fields.DateTime,
        "orders": fields.List(fields.String),
        "password": fields.String,
    })

    register_resp = api.model("Customer register response", {
        "status": fields.Boolean,
        "message": fields.String,
        "user": fields.Nested(customer)
    })

    update_resp = api.model("Customer update response", {
        "status": fields.Boolean,
        "message": fields.String,
        "user": fields.Nested(customer)
    })

    delete_req = api.model("Customer delete request", {
        "email": fields.String,
        "name": fields.String,
        "username": fields.String,
    })

    delete_resp = api.model("Customer delete response", {
        "status": fields.Boolean,
        "message": fields.String,
        "user": fields.Nested(customer)
    })

    order_req = api.model("Customer order request", {
        "email": fields.String,
        "name": fields.String,
        "username": fields.String,
        "product": fields.String,
        "quantity": fields.Integer,
        "price": fields.Integer,
        "total": fields.Integer,
        "date": fields.DateTime,
    })

    order_resp = api.model("Customer order response", {
        "status": fields.Boolean,
        "message": fields.String,
        "order": fields.Nested(order_req)
    })

    order_list_req = api.model("Customer order list request", {
        "email": fields.String,
        "name": fields.String,
        "username": fields.String,
    })

    order_list_resp = api.model("Customer order list response", {
        "status": fields.Boolean,
        "message": fields.String,
        "orders": fields.List(fields.Nested(customer))
    })
    order_list_delete_resp = api.model("Customer order list delete response", {
        "status": fields.Boolean,
        "message": fields.String,
        "orders": fields.List(fields.Nested(customer))
    })

    order_data_resp = api.model("Customer order data response", {
        "status": fields.Boolean,
        "message": fields.String,
        "order": fields.Nested(customer)
    })

    order_update_resp = api.model("Customer order update response", {
        "status": fields.Boolean,
        "message": fields.String,
        "order": fields.Nested(customer)
    })
    order_delete_req = api.model("Customer order delete request", {
        "order_id": fields.String,
    })

    order_delete_resp = api.model("Customer order delete response", {
        "status": fields.Boolean,
        "message": fields.String,
        "order": fields.Nested(customer)
    })

    order_item_resp_list = api.model("Customer order item list response", {
        "status": fields.Boolean,
        "message": fields.String,
        "order_items": fields.List(fields.Nested(customer))
    })

    order_item_data_resp = api.model("Customer order item data response", {
        "status": fields.Boolean,
        "message": fields.String,
        "order_item": fields.Nested(customer)
    })

    order_item_update_resp = api.model("Customer order item update response", {
        "status": fields.Boolean,
        "message": fields.String,
        "order_item": fields.Nested(customer)
    })

    order_item_delete_resp = api.model("Customer order item delete response", {
        "status": fields.Boolean,
        "message": fields.String,
        "order_item": fields.Nested(customer)
    })
