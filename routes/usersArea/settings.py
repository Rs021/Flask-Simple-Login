from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models import db
from models.User import User

setting_bp = Blueprint('settings' ,__name__ , url_prefix='/settings')


@setting_bp.route('/update_user', methods=['GET', 'POST'])
@login_required
def update_user():
    user_form = request.form['about']

    User.query.filter_by(id=current_user.id).update({'about': user_form})
    db.session.commit()

    return redirect(url_for('settings.index'))

@setting_bp.route('/')
@login_required
def index():
    return render_template('settings/index.html')