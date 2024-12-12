from flask import Blueprint, render_template, url_for
from models.Blog import db, Blog

pages_bp = Blueprint('pages', __name__, url_prefix='/pages')


@pages_bp.route('/<int:id>')
def pages(id):
    post = db.session.query(Blog).get(id)

    return render_template("pages/index.html", post=post)