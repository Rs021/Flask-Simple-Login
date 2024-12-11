from flask import Flask
from routes.auth import auth_bp
from routes.home import main_bp
from flask_login import LoginManager
from models.db import User, db as user_db
from dotenv import load_dotenv
import os



login_m = LoginManager()

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv('secret_key')

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('sql_URI')


    # Configurando o LoginManager no aplicativo
    login_m.init_app(app)
    login_m.login_view = 'auth.login'  # Nome correto da rota de login na blueprint
    login_m.login_message = "Por favor, faça login para acessar esta página."

    # Mysql
    user_db.init_app(app)

    with app.app_context():
        user_db.create_all()



    # Registrar o loader de usuário

    @login_m.user_loader
    def user_loader(id):
        return User.query.get(int(id))

    # Registrar a blueprint
    app.register_blueprint(auth_bp)

    app.register_blueprint(main_bp)
    app.add_url_rule('/', endpoint='index')
    return app