from datetime import datetime
from app import db, bcrypt

from .order import Order, OrderItem


class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False, index=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    restaurant_name = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    menu = db.relationship('Menu', backref='restaurant', lazy='dynamic')
    orders = db.relationship('Order', backref='restaurant', lazy='dynamic')


class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True, unique=True, nullable=False)
    restaurant_id = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(64), index=True, unique=True)
    menu = db.Column(db.String(64), db.ForeignKey('restaurant.name'), index=True, unique=True)
    products = db.relationship('Product', backref='menu', lazy='dynamic')


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True, unique=True, nullable=False)
    restaurant_id = db.Column(db.String(64), index=True, unique=True)
    menu_id = db.Column(db.String(64), index=True, unique=True)
    product_name = db.Column(db.String(64), db.ForeignKey('menu.name'), index=True, unique=True)
    price = db.Column(db.Integer)
    description = db.Column(db.String(64), index=True, unique=True)
    image = db.Column(db.String(64), index=True, unique=True)
