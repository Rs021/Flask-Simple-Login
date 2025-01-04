from . import db, UserMixin



class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(170))
    about = db.Column(db.String(128))

    def update_user(sobre: str):
        about = sobre
        db.session.commit()