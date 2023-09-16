from flask import jsonify, Blueprint, request

order_blueprint = Blueprint("order", __name__)


@order_blueprint.route("/order/add", methods=["POST"])
def add_order_controller():
    from app.main.service import order_service
    data = request.json
    order = order_service.add_order_service(data)
    if isinstance(order, int):
        return jsonify({
            "message": "Order placed successfully"
        }), 200
    else:
        return jsonify({
            "message": "Failed to place the order",
            "error": order
        }), 400


@order_blueprint.route("/order/get_all_order_details", methods=["GET"])
def get_all_order_details_controller():
    from app.main.service import order_service
    order_details = order_service.get_all_order_details()
    if order_details:
        return jsonify(order_details), 200
    else:
        return jsonify({
            "message": "Failed to fetch product details"
        }), 400
