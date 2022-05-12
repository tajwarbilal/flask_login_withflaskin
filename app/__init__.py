from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    from app.users.users_blueprint import user_blueprints
    app.register_blueprint(user_blueprints)

    app.config['SECRET_KEY'] = 'Thisissupposedtobfdsfsfesecret!'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    return app
