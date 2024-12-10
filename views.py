from flask import Blueprint, session, redirect, url_for, render_template, request, flash

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route("/login", methods=["POST", "GET"])
def login():
    if 'username' in session:
        return redirect(url_for('main.index'))

    if request.method == "GET":
        return render_template("login.html", title="A Simple Page")

    session['username'] = request.form['user']

    return redirect(url_for('main.index'))

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.login'))
@bp.route('/')
def index():

    if 'username' in session:
        return render_template('index.html', user=session['username'])

    return redirect(url_for('main.login'))
