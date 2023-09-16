from flask import Flask

from flask_migrate import Migrate
from app.main.config import config_by_name
from extensions import db

app = Flask(__name__)
env = 'dev'
app.config.from_object(config_by_name[env])

db.init_app(app)

migrate = Migrate(app, db)

from app.main.controller.hello_controller import hello_blueprint

app.register_blueprint(hello_blueprint)

from app.main.controller.product_details_controller import product_details_blueprint

app.register_blueprint(product_details_blueprint)

from app.main.controller.append_images_controller import product_images_blueprint

app.register_blueprint(product_images_blueprint)

from app.main.controller.order_controller import order_blueprint

app.register_blueprint(order_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
