from flask import jsonify, request, Blueprint

product_images_blueprint = Blueprint("product_images", __name__)


@product_images_blueprint.route("/product_details/product_id/<int:product_id>", methods=["POST"])
def add_images_controller(product_id):
    from app.main.service import append_images_product_service
    data = request.get_json()
    image_url = data.get('image_url')

    add_images, message = append_images_product_service.add_images_service(product_id, image_url)
    if add_images:
        return jsonify({
            "message": message
        }), 200
    else:
        return jsonify({
            "message": "Failed to add images",
            "error": message
        }), 400


@product_images_blueprint.route("/product_details/get_all_product_with_images", methods=["GET"])
def get_all_product_with_images_controller():
    from app.main.service import append_images_product_service
    product_details_with_images = append_images_product_service.get_all_product_details_with_images()
    if product_details_with_images:
        return jsonify(product_details_with_images), 200
    else:
        return jsonify({
            "message": "Failed to fetch product details"
        }), 400
