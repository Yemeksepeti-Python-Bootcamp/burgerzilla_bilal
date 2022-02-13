def load_data(user_db_obj):
    from app.models.schemas import CustomerSchema

    user_schema = CustomerSchema()
    data = user_schema.dump(user_db_obj)
    return data


def get_customer_id(user_db_obj):
    from app.models.schemas import CustomerSchema

    user_schema = CustomerSchema()
    data = user_schema.dump(user_db_obj)
    return data['id']


def get_customer_order(user_db_obj, order_db_obj):
    from app.models.schemas import CustomerSchema
    from app.models.schemas import OrderSchema

    user_schema = CustomerSchema()
    order_schema = OrderSchema()

    data = user_schema.dump(user_db_obj)
    data['order'] = order_schema.dump(order_db_obj)

    return data['order']


def get_customer_order_id(user_db_obj, order_db_obj):
    from app.models.schemas import CustomerSchema
    from app.models.schemas import OrderSchema

    user_schema = CustomerSchema()
    order_schema = OrderSchema()

    data = user_schema.dump(user_db_obj)
    data['order'] = order_schema.dump(order_db_obj)

    return data['order']['order_id']


def get_customer_name(user_db_obj):
    from app.models.schemas import CustomerSchema

    user_schema = CustomerSchema()
    data = user_schema.dump(user_db_obj)
    return data['name']


def get_customer_email(user_db_obj):
    from app.models.schemas import CustomerSchema

    user_schema = CustomerSchema()
    data = user_schema.dump(user_db_obj)
    return data['email']


def get_customer_orders(user_db_obj):
    from app.models.schemas import CustomerSchema
    from app.models.schemas import OrderSchema

    user_schema = CustomerSchema()
    order_schema = OrderSchema()

    data = user_schema.dump(user_db_obj)
    data['orders'] = []
    for order in user_db_obj.orders:
        data['orders'].append(order_schema.dump(order))
    return data['orders']


def get_customer_order_items(user_db_obj, order_db_obj):
    from app.models.schemas import CustomerSchema
    from app.models.schemas import OrderSchema
    from app.models.schemas import OrderItemSchema

    user_schema = CustomerSchema()
    order_schema = OrderSchema()
    order_item_schema = OrderItemSchema()

    data = user_schema.dump(user_db_obj)
    data['order'] = order_schema.dump(order_db_obj)
    data['order']['order_items'] = []
    for order_item in order_db_obj.order_items:
        data['order']['order_items'].append(order_item_schema.dump(order_item))
    return data['order']['order_items']


def get_customer_order_item_id(user_db_obj, order_db_obj, order_item_db_obj):
    from app.models.schemas import CustomerSchema
    from app.models.schemas import OrderSchema
    from app.models.schemas import OrderItemSchema

    user_schema = CustomerSchema()
    order_schema = OrderSchema()
    order_item_schema = OrderItemSchema()

    data = user_schema.dump(user_db_obj)
    data['order'] = order_schema.dump(order_db_obj)
    data['order']['order_items'] = []
    for order_item in order_db_obj.order_items:
        data['order']['order_items'].append(order_item_schema.dump(order_item))
    return data['order']['order_items'][0]['order_item_id']


def get_customer_order_item_quantity(user_db_obj, order_db_obj, order_item_db_obj):
    from app.models.schemas import CustomerSchema
    from app.models.schemas import OrderSchema
    from app.models.schemas import OrderItemSchema

    user_schema = CustomerSchema()
    order_schema = OrderSchema()
    order_item_schema = OrderItemSchema()

    data = user_schema.dump(user_db_obj)
    data['order'] = order_schema.dump(order_db_obj)
    data['order']['order_items'] = []
    for order_item in order_db_obj.order_items:
        data['order']['order_items'].append(order_item_schema.dump(order_item))
    return data['order']['order_items'][0]['quantity']


def get_customer_order_item_price(user_db_obj, order_db_obj, order_item_db_obj):
    from app.models.schemas import CustomerSchema
    from app.models.schemas import OrderSchema
    from app.models.schemas import OrderItemSchema

    user_schema = CustomerSchema()
    order_schema = OrderSchema()
    order_item_schema = OrderItemSchema()

    data = user_schema.dump(user_db_obj)
    data['order'] = order_schema.dump(order_db_obj)
    data['order']['order_items'] = []
    for order_item in order_db_obj.order_items:
        data['order']['order_items'].append(order_item_schema.dump(order_item))
    return data['order']['order_items'][0]['price']


def get_customer_order_item_product(user_db_obj, order_db_obj, order_item_db_obj):
    from app.models.schemas import CustomerSchema
    from app.models.schemas import OrderSchema
    from app.models.schemas import OrderItemSchema

    user_schema = CustomerSchema()
    order_schema = OrderSchema()
    order_item_schema = OrderItemSchema()

    data = user_schema.dump(user_db_obj)
    data['order'] = order_schema.dump(order_db_obj)
    data['order']['order_items'] = []
    for order_item in order_db_obj.order_items:
        data['order']['order_items'].append(order_item_schema.dump(order_item))
    return data['order']['order_items'][0]['product']


def get_customer_order_item_product_id(user_db_obj, order_db_obj, order_item_db_obj):
    from app.models.schemas import CustomerSchema
    from app.models.schemas import OrderSchema
    from app.models.schemas import OrderItemSchema

    user_schema = CustomerSchema()
    order_schema = OrderSchema()
    order_item_schema = OrderItemSchema()

    data = user_schema.dump(user_db_obj)
    data['order'] = order_schema.dump(order_db_obj)
    data['order']['order_items'] = []
    for order_item in order_db_obj.order_items:
        data['order']['order_items'].append(order_item_schema.dump(order_item))
    return data['order']['order_items'][0]['product_id']


def get_customer_order_item_product_name(user_db_obj, order_db_obj, order_item_db_obj):
    from app.models.schemas import CustomerSchema
    from app.models.schemas import OrderSchema
    from app.models.schemas import OrderItemSchema

    user_schema = CustomerSchema()
    order_schema = OrderSchema()
    order_item_schema = OrderItemSchema()

    data = user_schema.dump(user_db_obj)
    data['order'] = order_schema.dump(order_db_obj)
    data['order']['order_items'] = []
    for order_item in order_db_obj.order_items:
        data['order']['order_items'].append(order_item_schema.dump(order_item))
    return data['order']['order_items'][0]['product_name']


def get_customer_order_item_product_description(user_db_obj, order_db_obj, order_item_db_obj):
    from app.models.schemas import CustomerSchema
    from app.models.schemas import OrderSchema
    from app.models.schemas import OrderItemSchema

    user_schema = CustomerSchema()
    order_schema = OrderSchema()
    order_item_schema = OrderItemSchema()

    data = user_schema.dump(user_db_obj)
    data['order'] = order_schema.dump(order_db_obj)
    data['order']['order_items'] = []
    for order_item in order_db_obj.order_items:
        data['order']['order_items'].append(order_item_schema.dump(order_item))
    return data['order']['order_items'][0]['product_description']


def get_customer_order_item_product_image(user_db_obj, order_db_obj, order_item_db_obj):
    from app.models.schemas import CustomerSchema
    from app.models.schemas import OrderSchema
    from app.models.schemas import OrderItemSchema

    user_schema = CustomerSchema()
    order_schema = OrderSchema()
    order_item_schema = OrderItemSchema()

    data = user_schema.dump(user_db_obj)
    data['order'] = order_schema.dump(order_db_obj)
    data['order']['order_items'] = []
    for order_item in order_db_obj.order_items:
        data['order']['order_items'].append(order_item_schema.dump(order_item))
    return data['order']['order_items'][0]['product_image']


def get_customer_order_item_product_price(user_db_obj, order_db_obj, order_item_db_obj):
    from app.models.schemas import CustomerSchema
    from app.models.schemas import OrderSchema
    from app.models.schemas import OrderItemSchema

    user_schema = CustomerSchema()
    order_schema = OrderSchema()
    order_item_schema = OrderItemSchema()

    data = user_schema.dump(user_db_obj)
    data['order'] = order_schema.dump(order_db_obj)
    data['order']['order_items'] = []
    for order_item in order_db_obj.order_items:
        data['order']['order_items'].append(order_item_schema.dump(order_item))
    return data['order']['order_items'][0]['product_price']


def get_customer_order_item_product_quantity(user_db_obj, order_db_obj, order_item_db_obj):
    from app.models.schemas import CustomerSchema
    from app.models.schemas import OrderSchema
    from app.models.schemas import OrderItemSchema

    user_schema = CustomerSchema()
    order_schema = OrderSchema()
    order_item_schema = OrderItemSchema()

    data = user_schema.dump(user_db_obj)
    data['order'] = order_schema.dump(order_db_obj)
    data['order']['order_items'] = []
    for order_item in order_db_obj.order_items:
        data['order']['order_items'].append(order_item_schema.dump(order_item))
    return data['order']['order_items'][0]['product_quantity']


def get_customer_order_item_product_total(user_db_obj, order_db_obj, order_item_db_obj):
    from app.models.schemas import CustomerSchema
    from app.models.schemas import OrderSchema
    from app.models.schemas import OrderItemSchema

    user_schema = CustomerSchema()
    order_schema = OrderSchema()
    order_item_schema = OrderItemSchema()

    data = user_schema.dump(user_db_obj)
    data['order'] = order_schema.dump(order_db_obj)
    data['order']['order_items'] = []
    for order_item in order_db_obj.order_items:
        data['order']['order_items'].append(order_item_schema.dump(order_item))
    return data['order']['order_items'][0]['product_total']


