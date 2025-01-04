from flask import Flask, Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models.Blog import db, Blog
import datetime
post_bp = Blueprint('post', __name__, url_prefix='/new_post')

@post_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'GET':
        return render_template('blog/post/index.html', blog_title="Create New Post")

    title = request.form.get('title')
    content = request.form.get('content')
    _data = str(datetime.datetime.now())

    new_post = Blog(title=title, content=content, owner=current_user.username, data=_data)

    db.session.add(new_post)
    db.session.commit()
    db.session.close()

    return redirect(url_for('blog.index'))