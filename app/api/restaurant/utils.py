def load_data(data):
    from app.models.schemas import RestaurantSchema

    restaurant_schema = RestaurantSchema()
    data = restaurant_schema.dump(data)
    return data


def get_restaurant_id(user_db_obj):
    from app.models.schemas import RestaurantSchema

    restaurant_schema = RestaurantSchema()
    data = restaurant_schema.dump(user_db_obj)
    return data['id']


def get_restaurant_name(user_db_obj):
    from app.models.schemas import RestaurantSchema

    restaurant_schema = RestaurantSchema()
    data = restaurant_schema.dump(user_db_obj)
    return data['name']


def get_restaurant_email(user_db_obj):
    from app.models.schemas import RestaurantSchema

    restaurant_schema = RestaurantSchema()
    data = restaurant_schema.dump(user_db_obj)
    return data['email']


def get_restaurant_password(user_db_obj):
    from app.models.schemas import RestaurantSchema

    restaurant_schema = RestaurantSchema()
    data = restaurant_schema.dump(user_db_obj)
    return data['password']


def get_restaurant_password_hash(user_db_obj):
    from app.models.schemas import RestaurantSchema

    restaurant_schema = RestaurantSchema()
    data = restaurant_schema.dump(user_db_obj)
    return data['password_hash']


def get_restaurant_orders(user_db_obj):
    from app.models.schemas import RestaurantSchema

    restaurant_schema = RestaurantSchema()
    data = restaurant_schema.dump(user_db_obj)
    return data['orders']


def get_restaurant_order(user_db_obj, order_id):
    from app.models.schemas import RestaurantSchema

    restaurant_schema = RestaurantSchema()
    data = restaurant_schema.dump(user_db_obj)
    return data['orders'][order_id]


def get_restaurant_order_by_customer_name(user_db_obj, customer_name):
    from app.models.schemas import OrderSchema
    from app.models.schemas import RestaurantSchema

    order_schema = OrderSchema()
    restaurant_schema = RestaurantSchema()

    orders = get_restaurant_orders(user_db_obj)
    for key, value in orders.items():
        if order_schema.dump(value)['customer_name'] == customer_name:
            return key

    return None


def get_order_status(user_db_obj, order_id):
    from app.models.schemas import RestaurantSchema

    restaurant_schema = RestaurantSchema()
    data = restaurant_schema.dump(user_db_obj)
    return data['orders'][order_id]['status']


def get_order_customer_name(user_db_obj, order_id):
    from app.models.schemas import RestaurantSchema

    restaurant_schema = RestaurantSchema()
    data = restaurant_schema.dump(user_db_obj)
    return data['orders'][order_id]['customer_name']


def get_restaurant_menu(user_db_obj):
    from app.models.schemas import RestaurantSchema

    restaurant_schema = RestaurantSchema()
    data = restaurant_schema.dump(user_db_obj)
    return data['menu']


def get_menu_items(user_db_obj):
    from app.models.schemas import RestaurantSchema

    restaurant_schema = RestaurantSchema()
    data = restaurant_schema.dump(user_db_obj)
    return data['menu']['products']


def get_menu_item(user_db_obj, item_id):
    from app.models.schemas import RestaurantSchema

    restaurant_schema = RestaurantSchema()
    data = restaurant_schema.dump(user_db_obj)
    return data['menu']['products'][item_id]
