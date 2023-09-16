from main import db


class ProductImages(db.Model):
    __tablename__ = "product_images"
    image_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product_details.product_id'))
    image_url = db.Column(db.String(100))
    product_details = db.relationship('ProductDetails', backref='product_images')
