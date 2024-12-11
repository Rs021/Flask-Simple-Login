from flask import Blueprint, render_template
from flask_login import login_required, current_user
main_bp = Blueprint('blog', __name__, url_prefix='/')


@main_bp.route("/")
@login_required
def index():

    return render_template('index.html', user=current_user)
