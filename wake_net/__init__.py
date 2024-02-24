from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig
from .views import main


app = Flask(__name__)

app.config.from_object(DevelopmentConfig)

bootstrap = Bootstrap5(app)
db = SQLAlchemy(app)

app.register_blueprint(main)
