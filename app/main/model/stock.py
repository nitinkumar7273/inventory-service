from datetime import datetime

from main import db


class Stock(db.Model):
    __tablename__ = "stock"
    stock_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product_details.product_id'))
    quantity = db.Column(db.Integer)
    last_update = db.Column(db.DateTime, onupdate=datetime.utcnow)
    product_details = db.relationship('ProductDetails', backref='stock')
