from datetime import datetime
from app import db, bcrypt

# from .users import User
# from .restaurant import Restaurant, Menu, Product


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    order_status = db.Column(db.String(20), default='pending')
    # products = db.relationship('Product', backref=db.backref('order_product', lazy='dynamic'))


class OrderItem(db.Model):
    __tablename__ = 'order_product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    price = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer)
    total_price = db.Column(db.Float)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow)
