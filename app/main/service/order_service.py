from flask import jsonify
from app.main.model.order import Order
from app.main.model.order_details import OrderDetails
from app.main.model.product_details import ProductDetails
from extensions import db


def add_order_service(data):
    user_id = data.get("user_id")
    product_id = data.get("product_id")
    quantity = data.get("quantity")
    unit_price = data.get("unit_price")
    product_data = ProductDetails.query.filter_by(product_id=product_id, isDeleted=0).first()
    if not product_data:
        return False, "Product not found"
    if not user_id or not product_id or not quantity or not unit_price:
        return jsonify({
            "message": "Missing data"
        }), 400
    try:
        order = Order(user_id=user_id)
        db.session.add(order)
        db.session.commit()
        order_details = OrderDetails(
            order_id=order.order_id,
            product_id=product_id,
            quantity=quantity,
            unit_price=unit_price
        )
        db.session.add(order_details)
        db.session.commit()
        return order.order_id
    except Exception as e:
        db.session.rollback()
        return False, str(e)


def get_all_order_details():
    try:
        query_result = db.session.query(Order, OrderDetails, ProductDetails). \
            join(OrderDetails, Order.order_id == OrderDetails.order_id). \
            join(ProductDetails, OrderDetails.product_id == ProductDetails.product_id). \
            filter(ProductDetails.isDeleted == 0).all()
        all_orders = []
        for order, order_details, product_details in query_result:
            order_details_dic = {
                "order_details_id": order_details.order_details_id,
                "order_id": order_details.order_id,
                "product_id": order_details.product_id,
                "quantity": order_details.quantity,
                "unit_price": order_details.unit_price,
                "user_id": order.user_id
            }
            all_orders.append(order_details_dic)
        return all_orders
    except Exception as e:
        return False, str(e)
