from flask import Blueprint, render_template, url_for, request
from flask_login import login_required, current_user
from models.Blog import Blog, db

main_bp = Blueprint('blog', __name__, url_prefix='/')

pp = 4

@main_bp.route('/', defaults={'id': ''})
@main_bp.route("/<int:id>")

def index(id):

    if isinstance(id, str):
        id = 1

    offset = (int(id) - 1) * pp
    posts = db.session.query(Blog).limit(pp).offset(offset).all()

    #Calcular o número total de páginas
    total_posts = db.session.query(Blog).count()
    total_pages = (total_posts + pp - 1) // pp

    db.session.close()

    return render_template('blog/index.html',
                            posts=posts,
                           page=id,
                           total_pages=total_pages,
                           total_posts = total_posts,
                           path=request.path
                           )
