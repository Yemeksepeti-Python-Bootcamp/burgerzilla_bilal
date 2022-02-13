from http.client import responses
from flask_restx import Resource
from flask_jwt_extended import jwt_required

from .service import CustomerService
from .dto import CustomerDto

api = CustomerDto.api
data_resp = CustomerDto.data_resp
customer_create = CustomerDto.customer_create
customer_delete = CustomerDto.customer_delete
customer_update = CustomerDto.customer_update
customer_list = CustomerDto.customer_list
customer_resp = CustomerDto.customer_resp
customer_req = CustomerDto.customer_req
order_req = CustomerDto.order_req
order_resp = CustomerDto.order_resp
order_delete_req = CustomerDto.order_delete_req
order_delete_resp = CustomerDto.order_delete_resp
order_list_resp = CustomerDto.order_list_resp
order_update_resp = CustomerDto.order_update_resp
order_list_delete_resp = CustomerDto.order_list_delete_resp
order_item_resp_list = CustomerDto.order_item_resp_list


@api.route("/<string:username>")
class CustomerGet(Resource):
    @api.doc("get specified customer data", responses={
        200: ("Success", data_resp),
        404: "Customer Not Found",
    })
    @jwt_required()
    def get(self, username):
        """get customer data"""
        return CustomerService.get_customer_data(username)

    @api.doc("delete customer data", responses={
        200: ("Success", customer_delete),
        404: "Customer Not Found",
    })
    @jwt_required()
    def delete(self, username):
        """delete customer data"""
        return CustomerService.delete_customer_data(username)

    @api.doc("update customer data", responses={
        200: ("Success", customer_update),
        404: "Customer Not Found",
    })
    @jwt_required()
    def put(self, username):
        """update customer data"""
        return CustomerService.update_customer_data(username)


@api.route("/")
class CustomerList(Resource):
    @api.doc("get all customer data", responses={
        200: ("Success", customer_list),
        404: "Customer Not Found",
    })
    @jwt_required()
    def get(self):
        """get all customer data"""
        return CustomerService.get_all_customer_data()


@api.route("/user/orders/<int:user_id>")
class OrderOperations(Resource):
    @api.doc("get all customer orders", responses={
        200: ("Success", order_list_resp),
        404: "Customer Not Found",
    })
    @jwt_required()
    def get(self, user_id):
        """get all customer orders"""
        return CustomerService.get_orders_by_user_id(user_id)

    @api.doc("delete customer orders", responses={
        200: ("Success", order_list_delete_resp),
        404: "Customer Not Found",
    })
    @jwt_required()
    def delete(self, user_id):
        """delete all customer orders"""
        return CustomerService.delete_all_orders_by_user_id(user_id)


@api.route("/user/orders/<int:user_id>/<int:order_id>")
class SpecificOrderOperations(Resource):
    @api.doc("get customer specific order", responses={
        200: ("Success", order_resp),
        404: "Customer Not Found",
    })
    @jwt_required()
    def get(self, user_id, order_id):
        """get customer specific order"""
        return CustomerService.get_order_details_by_user_id(user_id, order_id)

    @api.doc("delete customer specific order", responses={
        200: ("Success", order_delete_resp),
        404: "Customer Not Found",
    })
    @jwt_required()
    def delete(self, user_id, order_id):
        """delete customer specific order"""
        return CustomerService.delete_order_by_user_id(user_id, order_id)

    @api.doc("update customer specific order", responses={
        200: ("Success", order_update_resp),
        404: "Customer Not Found",
    })
    @api.expect(order_req)
    @jwt_required()
    def put(self, user_id, order_id):
        """update customer specific order"""
        return CustomerService.update_order_by_user_id(user_id, order_id, order_req)

    @api.doc("add customer specific order", responses={
        200: ("Success", order_resp),
        404: "Customer Not Found",
    })
    @api.expect(order_req)
    @jwt_required()
    def post(self, user_id):
        """add customer specific order"""
        return CustomerService.create_order_by_user_id(user_id, order_req)



