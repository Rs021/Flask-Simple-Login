from flask import Flask
from routes.auth import auth_bp
from routes.home import main_bp
from flask_login import LoginManager
from models.User import User, db as user_db
from routes.pages.pages import pages_bp
from dotenv import load_dotenv
import os
from routes.usersArea.settings import setting_bp
from flask_migrate import Migrate, migrate
from routes.CreatePosts.post import post_bp
login_m = LoginManager()

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv('secret_key')

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('sql_URI')

    login_m.init_app(app)
    login_m.login_view = 'auth.login'  # Nome correto da rota de login na blueprint
    login_m.login_message = "Por favor, faça login para acessar esta página."

    # Mysql
    user_db.init_app(app)

    migrate = Migrate(app, user_db)

    with app.app_context():
        user_db.create_all()

    @login_m.user_loader
    def user_loader(id):
        return User.query.get(int(id))


    app.register_blueprint(auth_bp)
    main_bp.register_blueprint(post_bp)
    app.register_blueprint(main_bp)

    app.register_blueprint(pages_bp)
    app.register_blueprint(setting_bp)
    return app