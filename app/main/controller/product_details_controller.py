from flask import jsonify, Blueprint, request

product_details_blueprint = Blueprint("product_details", __name__)


@product_details_blueprint.route("/product_details/add", methods=["POST"])
def create_product_controller():
    data = request.json
    from app.main.service import product_details_service
    success = True
    message = product_details_service.create_product_service(data)

    if success:
        return jsonify(
            {"message": "New product created successfully"}
        ), 200
    else:
        return jsonify(
            {
                "message": "Failed to create new product",
                "error": message
            }
        ), 500


@product_details_blueprint.route("/product_details/get_all", methods=["GET"])
def get_all_product_controller():
    from app.main.service import product_details_service
    get_all_product = product_details_service.get_all_product_service()
    return jsonify(get_all_product)


@product_details_blueprint.route("/product_details/get_by_id/<int:product_id>", methods=["GET"])
def get_product_by_id_controller(product_id):
    from app.main.service import product_details_service
    get_product_by_id = product_details_service.get_product_by_id_service(product_id)
    if product_id is not None:
        return jsonify(get_product_by_id), 200


@product_details_blueprint.route("/product_details/update", methods=["POST"])
def update_product_controller():
    data = request.json
    from app.main.service import product_details_service
    updated_product = product_details_service.update_product_service(data)
    if updated_product:
        return jsonify(
            {"message": "Product updated successfully"}
        ), 200
    else:
        return jsonify(
            {
                "message": "Failed to update product",
                "error": updated_product
            }
        ), 500


@product_details_blueprint.route("/product_details/delete", methods=["POST"])
def delete_product_controller():
    data = request.json
    from app.main.service import product_details_service
    delete_product = product_details_service.delete_product_service(data)
    if delete_product:
        return jsonify(
            {"message": "Product deleted successfully"}
        ), 200
    else:
        return jsonify(
            {
                "message": "Failed to delete product",
                "error": delete_product
            }
        ), 500
