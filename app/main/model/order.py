from main import db


class Order(db.Model):
    __tablename__ = "order"
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
