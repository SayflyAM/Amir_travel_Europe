from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)


@home_bp.route('/')
def index():
    whatsapp = '+971565598682'
    return render_template('index.html', whatsapp=whatsapp)
