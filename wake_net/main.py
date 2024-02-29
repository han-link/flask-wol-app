from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig
from flask_wtf import CSRFProtect

bootstrap = Bootstrap5()
db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    bootstrap.init_app(app)
    csrf.init_app(app)

    from wake_net.views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app