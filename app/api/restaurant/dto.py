from flask_restx import Namespace, fields


class RestaurantDto:
    api = Namespace("restaurant", description="Restaurant related operations")

    restaurant = api.model(
        "restaurant object",
        {
            "name": fields.String(required=True, description="The name of a restaurant"),
            "email": fields.String(required=True, description="The email of a restaurant"),
            "restaurant_name": fields.String(required=True, description="The restaurant name of a restaurant"),
            "username": fields.String(required=True, description="The username of a restaurant"),
            "joined_date": fields.DateTime,
            "role": fields.String,
            "last_login": fields.DateTime,
            "orders": fields.List(fields.String)
        })

    product = api.model(
        "product object",
        {
            "restaurant_id": fields.Integer(required=True, description="The id of a restaurant"),
            "menu_id": fields.Integer(required=True, description="The id of a menu"),
            "product_name": fields.String(required=True, description="The name of a product"),
            "price": fields.Float(required=True, description="The price of a product"),
            "description": fields.String(required=True, description="The description of a product"),
            "image": fields.String(required=True, description="The image of a product"),
        })

    menu = api.model(
        "menu object",
        {
            "restaurant_id": fields.Integer(required=True, description="The id of a restaurant"),
            "menu_name": fields.String(required=True, description="The name of a menu"),
            "products": fields.List(fields.Nested(product))
        })

    order = api.model(
        "order object",
        {
            "restaurant_id": fields.Integer(required=True, description="The id of a restaurant"),
            "order_id": fields.Integer(required=True, description="The id of an order"),
            "order_date": fields.DateTime(required=True, description="The date of an order"),
            "order_status": fields.String(required=True, description="The status of an order"),
            "order_items": fields.List(fields.Nested(product))
        })

    restaurant_list = api.model(
        "restaurant list",
        {
            "restaurants": fields.List(fields.Nested(restaurant))
        })

    restaurant_update = api.model(
        "restaurant update",
        {
            "name": fields.String(required=True, description="The name of a restaurant"),
            "email": fields.String(required=True, description="The email of a restaurant"),
            "restaurant_name": fields.String(required=True, description="The restaurant name of a restaurant"),
            "username": fields.String(required=True, description="The username of a restaurant"),
            "joined_date": fields.DateTime,
            "role": fields.String,
            "last_login": fields.DateTime,
            "orders": fields.List(fields.String)
        })

    restaurant_create = api.model(
        "restaurant create",
        {
            "name": fields.String(required=True, description="The name of a restaurant"),
            "email": fields.String(required=True, description="The email of a restaurant"),
            "restaurant_name": fields.String(required=True, description="The restaurant name of a restaurant"),
            "username": fields.String(required=True, description="The username of a restaurant"),
            "joined_date": fields.DateTime,
            "role": fields.String,
            "last_login": fields.DateTime,
            "orders": fields.List(fields.String)
        })

    restaurant_delete = api.model(
        "restaurant delete",
        {
            "name": fields.String(required=True, description="The name of a restaurant"),
            "email": fields.String(required=True, description="The email of a restaurant"),
            "restaurant_name": fields.String(required=True, description="The restaurant name of a restaurant"),
            "username": fields.String(required=True, description="The username of a restaurant"),
            "joined_date": fields.DateTime,
            "role": fields.String,
            "last_login": fields.DateTime,
            "orders": fields.List(fields.String)
        })

    restaurant_login = api.model(
        "restaurant login",
        {
            "name": fields.String(required=True, description="The name of a restaurant"),
            "email": fields.String(required=True, description="The email of a restaurant"),
            "restaurant_name": fields.String(required=True, description="The restaurant name of a restaurant"),
            "username": fields.String(required=True, description="The username of a restaurant"),
            "joined_date": fields.DateTime,
            "role": fields.String,
            "last_login": fields.DateTime,
            "orders": fields.List(fields.String)
        })

    restaurant_logout = api.model(
        "restaurant logout",
        {
            "name": fields.String(required=True, description="The name of a restaurant"),
            "email": fields.String(required=True, description="The email of a restaurant"),
            "restaurant_name": fields.String(required=True, description="The restaurant name of a restaurant"),
            "username": fields.String(required=True, description="The username of a restaurant"),
            "joined_date": fields.DateTime,
            "role": fields.String,
            "last_login": fields.DateTime,
            "orders": fields.List(fields.String)
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

    data_resp = api.model("Restaurant data response", {
        "status": fields.Boolean,
        "message": fields.String,
        "user": fields.Nested(restaurant)
    })

    data_resp_list = api.model("Restaurant data response", {
        "status": fields.Boolean,
        "message": fields.String,
        "users": fields.List(fields.Nested(restaurant))
    })

    data_resp_create = api.model("Restaurant data response", {
        "status": fields.Boolean,
        "message": fields.String,
        "user": fields.Nested(restaurant_create)
    })

    data_resp_delete = api.model("Restaurant data response", {
        "status": fields.Boolean,
        "message": fields.String,
        "user": fields.Nested(restaurant_delete)
    })

    data_resp_login = api.model("Restaurant data response", {
        "status": fields.Boolean,
        "message": fields.String,
        "user": fields.Nested(restaurant_login)
    })

    data_resp_logout = api.model("Restaurant data response", {
        "status": fields.Boolean,
        "message": fields.String,
        "user": fields.Nested(restaurant_logout)
    })

    order_resp = api.model("Order response", {
        "status": fields.Boolean,
        "message": fields.String,
        "order": fields.Nested(order)
    })

    order_resp_list = api.model("Order response", {
        "status": fields.Boolean,
        "message": fields.String,
        "orders": fields.List(fields.Nested(restaurant))
    })

    order_list_req = api.model("Order list request", {
        "restaurant_name": fields.String(required=True, description="The restaurant name of a restaurant"),
        "username": fields.String(required=True, description="The username of a restaurant"),
        "orders": fields.List(fields.String)
    })

    order_detail_req = api.model("Order detail request", {
        "restaurant_name": fields.String(required=True, description="The restaurant name of a restaurant"),
        "username": fields.String(required=True, description="The username of a restaurant"),
        "order_id": fields.String(required=True, description="The order id of a restaurant")
    })

    order_delete_req = api.model("Order delete request", {
        "restaurant_name": fields.String(required=True, description="The restaurant name of a restaurant"),
        "username": fields.String(required=True, description="The username of a restaurant"),
        "order_id": fields.String(required=True, description="The order id of a restaurant")
    })

    order_status_req = api.model("Order status request", {
        "restaurant_name": fields.String(required=True, description="The restaurant name of a restaurant"),
        "username": fields.String(required=True, description="The username of a restaurant"),
        "order_id": fields.String(required=True, description="The order id of a restaurant"),
        "status": fields.String(required=True, description="The status of a restaurant")
    })

    order_status_resp = api.model("Order status response", {
        "status": fields.Boolean,
        "message": fields.String,
        "order": fields.Nested(restaurant)
    })

    restaurant_menu_detail_req = api.model("Restaurant menu detail request", {
        "restaurant_name": fields.String(required=True, description="The restaurant name of a restaurant"),
        "username": fields.String(required=True, description="The username of a restaurant"),
        "menu_id": fields.String(required=True, description="The menu id of a restaurant")
    })

    restaurant_menu_detail_resp = api.model("Restaurant menu detail response", {
        "status": fields.Boolean,
        "message": fields.String,
        "menu": fields.Nested(menu)
    })

    restaurant_menu_update_req = api.model("Restaurant menu update request", {
        "restaurant_id": fields.String(required=True, description="The restaurant id of a restaurant"),
        "menu_name": fields.String(required=True, description="The name of a menu"),
        "products": fields.List(fields.Nested(product))
    })

    restaurant_menu_update_resp = api.model("Restaurant menu update response", {
        "status": fields.Boolean,
        "message": fields.String,
        "menu": fields.Nested(menu)
    })

    restaurant_menu_items_list_req = api.model("Restaurant menu items list request", {
        "restaurant_name": fields.String(required=True, description="The restaurant name of a restaurant"),
        "username": fields.String(required=True, description="The username of a restaurant"),
        "menu_id": fields.String(required=True, description="The menu id of a restaurant")
    })

    restaurant_menu_items_list_resp = api.model("Restaurant menu items list response", {
        "status": fields.Boolean,
        "message": fields.String,
        "menu_items": fields.List(fields.Nested(product))
    })

    restaurant_add_items_menu_req = api.model("Restaurant add menu request", {
        "restaurant_name": fields.String(required=True, description="The restaurant name of a restaurant"),
        "username": fields.String(required=True, description="The username of a restaurant"),
        "menu_id": fields.String(required=True, description="The menu id of a restaurant"),
        "products": fields.List(fields.Nested(product))
    })

    restaurant_add_items_menu_resp = api.model("Restaurant add menu response", {
        "status": fields.Boolean,
        "message": fields.String,
        "menu": fields.Nested(menu)
    })

    restaurant_menu_item_details_req = api.model("Restaurant menu item details request", {
        "restaurant_name": fields.String(required=True, description="The restaurant name of a restaurant"),
        "username": fields.String(required=True, description="The username of a restaurant"),
        "menu_id": fields.String(required=True, description="The menu id of a restaurant"),
        "product_id": fields.String(required=True, description="The product id of a restaurant")
    })

    restaurant_menu_item_details_resp = api.model("Restaurant menu item details response", {
        "status": fields.Boolean,
        "message": fields.String,
        "product": fields.Nested(product)
    })

    restaurant_menu_item_update_req = api.model("Restaurant menu item update request", {
        "restaurant_name": fields.String(required=True, description="The restaurant name of a restaurant"),
        "username": fields.String(required=True, description="The username of a restaurant"),
        "menu_id": fields.String(required=True, description="The menu id of a restaurant"),
        "product_id": fields.String(required=True, description="The product id of a restaurant"),
        "product": fields.Nested(product)
    })

    restaurant_menu_item_update_resp = api.model("Restaurant menu item update response", {
        "status": fields.Boolean,
        "message": fields.String,
        "product": fields.Nested(product)
    })

    restaurant_menu_item_delete_req = api.model("Restaurant menu item delete request", {
        "restaurant_name": fields.String(required=True, description="The restaurant name of a restaurant"),
        "username": fields.String(required=True, description="The username of a restaurant"),
        "menu_id": fields.String(required=True, description="The menu id of a restaurant"),
        "product_id": fields.String(required=True, description="The product id of a restaurant")
    })

    restaurant_menu_item_delete_resp = api.model("Restaurant menu item delete response", {
        "status": fields.Boolean,
        "message": fields.String
    })


