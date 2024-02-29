from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig

bootstrap = Bootstrap5()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    bootstrap.init_app(app)

    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app