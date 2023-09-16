from main import db
from app.main.model.product_details import ProductDetails


def create_product_service(data):
    product_name = data.get("product_name")
    description = data.get("description")
    unit_price = data.get("unit_price")
    manufacturer = data.get("manufacturer")
    category = data.get("category")

    new_product = ProductDetails(
        product_name=product_name,
        description=description,
        unit_price=unit_price,
        manufacturer=manufacturer,
        category=category
    )

    try:
        db.session.add(new_product)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        return False, str(e)


def get_all_product_service():
    product_data = [
        {"product_id": pd.product_id,
         "product_name": pd.product_name,
         "description": pd.description,
         "unit_price": pd.unit_price,
         "manufacturer": pd.manufacturer,
         "category": pd.category,
         "idDeleted": pd.isDeleted} for pd in ProductDetails.query.filter_by(isDeleted=0).all()]
    return product_data


def get_product_by_id_service(product_id):
    product_data = ProductDetails.query.filter_by(product_id=product_id, isDeleted=0).first()
    if product_data:
        return {
            "product_id": product_data.product_id,
            "product_name": product_data.product_name,
            "description": product_data.description,
            "unit_price": product_data.unit_price,
            "manufacturer": product_data.manufacturer,
            "category": product_data.category
        }
    else:
        return None


def update_product_service(data):
    product_id = data.get("product_id")
    product_data = ProductDetails.query.filter_by(product_id=product_id, isDeleted=0).first()
    if not product_data:
        return False
    product_data.product_name = data.get("product_name")
    product_data.description = data.get("description")
    product_data.unit_price = data.get("unit_price")
    product_data.manufacturer = data.get("manufacturer")
    product_data.category = data.get("category")
    try:
        db.session.commit()
        return product_data
    except:
        db.session.rollback()
        return False


def delete_product_service(data):
    product_id = data.get("product_id")
    product_data = ProductDetails.query.filter_by(product_id=product_id, isDeleted=0).first()
    if not product_data:
        return False
    product_data.isDeleted = 1
    try:
        db.session.commit()
        return product_data
    except:
        db.session.rollback()
        return False
