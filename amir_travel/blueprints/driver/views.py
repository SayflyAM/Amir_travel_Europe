from flask import Blueprint, render_template

driver_bp = Blueprint('driver', __name__)


@driver_bp.route('/')
def page():
    return render_template('driver.html')
