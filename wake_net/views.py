# views.py
from flask import Blueprint, render_template

# Define a Blueprint named 'main'. This can be named anything.
main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')
