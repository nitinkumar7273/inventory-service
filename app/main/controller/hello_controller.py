from flask import jsonify, Blueprint

hello_blueprint = Blueprint("hello", __name__)


@hello_blueprint.route("/")
def hello():
    return jsonify({"message": "Inventory Service.........."})
