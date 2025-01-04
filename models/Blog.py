from flask_login import UserMixin
from . import db


class Blog(UserMixin, db.Model):
    __tablename__ = "blog"
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(50))
    data = db.Column(db.String(30))
    title = db.Column(db.String(64))
    content = db.Column(db.String(2048))