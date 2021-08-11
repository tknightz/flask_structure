from flask import Flask
from .models import db
from .auth import login_manager
from dotenv import dotenv_values


def create_app():
    app = Flask(__name__,
                template_folder='./templates',
                static_folder="./static")

    # Database init
    app.config.from_mapping(**dotenv_values('.env'))
    # app.config['SECRET_KEY'] = 'secret_key'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    login_manager.init_app(app)

    # Routes init
    from .routes.admin.views import admin_bp
    from .routes.public.views import public_bp

    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(public_bp, url_prefix='/')

    return app


app = create_app()
