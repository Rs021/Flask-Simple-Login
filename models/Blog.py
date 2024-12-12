from flask_login import UserMixin
from . import db


class Blog(UserMixin, db.Model):
    __tablename__ = "blog"
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(50), unique=True)
    data = db.Column(db.String(25))
    content = db.Column(db.String(512))