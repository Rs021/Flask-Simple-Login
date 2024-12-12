from flask import request, redirect, url_for
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from hashlib import sha256
from routes.home import *
from models.User import User, db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/register', methods=["POST", "GET"])
def register():

    if request.method == 'GET':
        return """
            <form method="POST">
                <input type="text" name="user">
                <input type="text" name="pass">
                <input type="submit" value="Enviar">
                
            </form>
        """
    username = request.form.get('user')
    password = request.form.get('pass')

    new_user = User(username=username, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('main.index'))

@auth_bp.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html", title="A Simple Page")

    username = request.form.get('user')
    password = request.form.get('pass')

    user = User.query.filter_by(username=username).first()



    if not user or not check_password_hash(user.password, password):
        return render_template("login.html", title="A Simple Page")


    login_user(user)
    return redirect(url_for('blog.index'))


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

