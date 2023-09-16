import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET KEY', 'my_previous_key')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin1234@127.0.0.1:3306/inventory-service'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin1234@192.168.56.1/inventory-service'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin1234@host.docker.internal:3306/inventory-service'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    dev=DevelopmentConfig
)

key = Config.SECRET_KEY
