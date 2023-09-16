from datetime import datetime
from sqlalchemy import event

from extensions import db


class ProductDetails(db.Model):
    __tablename__ = "product_details"
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(100), nullable=True)
    description = db.Column(db.String(200))
    unit_price = db.Column(db.Integer, nullable=True)
    manufacturer = db.Column(db.String(100))
    category = db.Column(db.String(50))
    createdDate = db.Column(db.DateTime, default=datetime.utcnow)
    modifiedDate = db.Column(db.DateTime, onupdate=datetime.utcnow)
    isDeleted = db.Column(db.Boolean, default=False)


@event.listens_for(ProductDetails, 'before_insert')
def set_created_date(target, value, initiator):
    target.createdDate = datetime.utcnow()


@event.listens_for(ProductDetails, 'before_update')
def set_modified_date(target, value, initiator):
    target.modifiedDate = datetime.utcnow()
