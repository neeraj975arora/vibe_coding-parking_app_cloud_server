from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """
    Serves the main landing page.
    """
    return render_template('index.html') 