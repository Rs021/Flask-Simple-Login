from flask import Flask
from tinydb import TinyDB
from views import bp

db = TinyDB("tinydb/My_db.json")

def create_app():
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.register_blueprint(bp)

    return app