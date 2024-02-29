import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev-flask-wol.db'
    BOOTSTRAP_FONTAWESOME = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    BOOTSTRAP_BOOTSWATCH_THEME = 'lux'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///flask-wol.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
