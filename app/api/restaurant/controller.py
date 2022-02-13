from http.client import responses
from flask_restx import Resource
from flask_jwt_extended import jwt_required

from .service import RestaurantService
from .dto import RestaurantDto

api = RestaurantDto.api
data_resp = RestaurantDto.data_resp
data_req = RestaurantDto.data_req
restaurant_model = RestaurantDto.restaurant
product_model = RestaurantDto.product
menu_model = RestaurantDto.menu
order_model = RestaurantDto.order
order_status = RestaurantDto.order_status_req


@api.route('/')
class RestaurantList(Resource):
    @api.doc('list_of_registered_restaurants')
    @api.marshal_list_with(data_resp)
    def get(self):
        """List all registered restaurants"""
        return RestaurantService.get_all_restaurants()


@api.route('/<int:restaurant_id>')
class RestaurantGet(Resource):
    @api.doc("get specified restaurant data", responses={
        200: ("Success", data_resp),
        404: "Restaurant Not Found",
    })
    @jwt_required()
    def get(self, restaurant_id):
        """get customer data"""
        return RestaurantService.get_restaurant_data(restaurant_id)

    @api.doc("update specified restaurant data", responses={
        200: ("Success", data_resp),
        404: "Restaurant Not Found",
    })
    @jwt_required()
    def put(self, restaurant_id):
        """update customer data"""
        return RestaurantService.update_restaurant_data(restaurant_id)

    @api.doc("delete specified restaurant data", responses={
        200: ("Success", data_resp),
        404: "Restaurant Not Found",
    })
    @jwt_required()
    def delete(self, restaurant_id):
        """delete customer data"""
        return RestaurantService.delete_restaurant_data(restaurant_id)

    @api.doc("create new restaurant", responses={
        201: ("Success", data_resp),
        400: "Bad Request",
    })
    @jwt_required()
    def post(self, restaurant_id):
        """create new restaurant"""
        return RestaurantService.create_restaurant(restaurant_id)


@api.route('/<int:restaurant_id>/orders')
class RestaurantOrders(Resource):
    @api.doc("get all orders of specified restaurant", responses={
        200: ("Success", data_resp),
        404: "Restaurant Not Found",
    })
    @jwt_required()
    def get(self, restaurant_id):
        """get all orders of specified restaurant"""
        return RestaurantService.get_restaurant_orders(restaurant_id)

    @api.doc("delete all orders of specified restaurant", responses={
        200: ("Success", data_resp),
        404: "Restaurant Not Found",
    })
    @jwt_required()
    def delete(self, restaurant_id):
        """delete all orders of specified restaurant"""
        return RestaurantService.delete_restaurant_orders(restaurant_id)


@api.route('/<int:restaurant_id>/orders/<int:order_id>')
class RestaurantOrder(Resource):
    @api.doc("get specified order of specified restaurant", responses={
        200: ("Success", data_resp),
        404: "Restaurant Not Found",
    })
    @jwt_required()
    def get(self, restaurant_id, order_id):
        """get specified order of specified restaurant"""
        return RestaurantService.get_restaurant_order_items(restaurant_id, order_id)

    @api.doc("delete specified order of specified restaurant", responses={
        200: ("Success", data_resp),
        404: "Restaurant Not Found",
    })
    @jwt_required()
    def delete(self, restaurant_id, order_id):
        """delete specified order of specified restaurant"""
        return RestaurantService.delete_restaurant_order_items(restaurant_id, order_id)

    @api.doc("update order status of specified order of specified restaurant", responses={
        200: ("Success", data_resp),
        404: "Restaurant Not Found",
    })
    @jwt_required()
    @api.expect(order_status)
    def put(self, restaurant_id, order_id):
        """update order status of specified order of specified restaurant"""
        return RestaurantService.change_order_status(restaurant_id, order_id, order_status)


@api.route('/<int:restaurant_id>/menu')
class RestaurantMenu(Resource):
    @api.doc("get specified menu of specified restaurant", responses={
        200: ("Success", data_resp),
        404: "Restaurant Not Found",
    })
    @jwt_required()
    def get(self, restaurant_id):
        """get specified menu of specified restaurant"""
        return RestaurantService.get_restaurant_menu(restaurant_id)

    @api.doc("delete specified menu of specified restaurant", responses={
        200: ("Success", data_resp),
        404: "Restaurant Not Found",
    })
    @jwt_required()
    def delete(self, restaurant_id, menu_id):
        """delete specified menu of specified restaurant"""
        return RestaurantService.delete_restaurant_menu(restaurant_id, menu_id)

    @api.doc("create new menu of specified restaurant", responses={
        201: ("Success", data_resp),
        400: "Bad Request",
    })
    @jwt_required()
    def post(self, restaurant_id, menu_id):
        """create new menu of specified restaurant"""
        return RestaurantService.create_restaurant_menu(restaurant_id, menu_id)

    @api.doc("update specified menu of specified restaurant", responses={
        200: ("Success", data_resp),
        404: "Restaurant Not Found",
    })
    @jwt_required()
    def put(self, restaurant_id, menu_id):
        """update specified menu of specified restaurant"""
        return RestaurantService.update_restaurant_menu(restaurant_id, menu_id)


@api.route('/<int:restaurant_id>/menu/<int:menu_id>')
class MenuOperations(Resource):
    @api.doc('get menu items of specified menu of specified restaurant', responses={
        200: ("Success", data_resp),
        404: "Restaurant Not Found",
    })
    @jwt_required()
    def get(self, restaurant_id):
        """get menu items of specified menu of specified restaurant"""
        return RestaurantService.get_restaurant_products(restaurant_id)

    @api.doc('delete menu items of specified menu of specified restaurant', responses={
        200: ("Success", data_resp),
        404: "Restaurant Not Found",
    })
    @jwt_required()
    def delete(self, restaurant_id, item_id):
        """delete menu items of specified menu of specified restaurant"""
        return RestaurantService.delete_item_from_restaurant_menu(restaurant_id, item_id)

    @api.doc('create new menu item of specified menu of specified restaurant', responses={
        201: ("Success", data_resp),
        400: "Bad Request",
    })
    @jwt_required()
    @api.expect(product_model)
    def post(self, restaurant_id):
        """create new menu item of specified menu of specified restaurant"""
        return RestaurantService.create_restaurant_product(restaurant_id, product_model)

    @api.doc('update specified menu item of specified menu of specified restaurant', responses={
        200: ("Success", data_resp),
        404: "Restaurant Not Found",
    })
    @jwt_required()
    @api.expect(product_model)
    def put(self, restaurant_id, item_id):
        """update specified menu item of specified menu of specified restaurant"""
        return RestaurantService.update_item_in_restaurant_menu(restaurant_id, item_id, product_model)




