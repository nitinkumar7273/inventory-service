from main import db


class OrderDetails(db.Model):
    __tablename__ = "order_details"
    order_details_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product_details.product_id'))
    quantity = db.Column(db.Integer)
    unit_price = db.Column(db.Integer)
    order = db.relationship('Order', backref='order_details')
    product_details = db.relationship('ProductDetails', backref='order_details')
