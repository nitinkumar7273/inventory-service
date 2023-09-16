from app.main.model.product_details import ProductDetails
from app.main.model.product_images import ProductImages
from extensions import db


def add_images_service(product_id, image_url):
    product_data = ProductDetails.query.filter_by(product_id=product_id, isDeleted=0).first()
    if not product_data:
        return False, "Product not found"
    try:
        for image_url in image_url:
            new_image = ProductImages(image_url=image_url, product_id=product_id)
            db.session.add(new_image)
        db.session.commit()
        return True, "Images added successfully"
    except Exception as e:
        db.session.rollback()
        return False, str(e)


def get_all_product_details_with_images():
    try:
        query_result = db.session.query(ProductDetails, ProductImages.image_url). \
            join(ProductImages, ProductDetails.product_id == ProductImages.product_id). \
            filter(ProductDetails.isDeleted == 0).all()
        product_details_with_images = []
        for product_details, image_url in query_result:
            product_details_dic = {
                "product_id": product_details.product_id,
                "product_name": product_details.product_name,
                "description": product_details.description,
                "unit_price": product_details.unit_price,
                "manufacturer": product_details.manufacturer,
                "category": product_details.category,
                "image_url": image_url
            }
            product_details_with_images.append(product_details_dic)
        return product_details_with_images
    except Exception as e:
        return False, str(e)
