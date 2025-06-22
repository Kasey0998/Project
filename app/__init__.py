from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from .models import User, create_default_admin

    # Register Blueprints
    from .routes.auth import auth_bp
    from .routes.dashboard import dashboard_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)

    with app.app_context():
        db.create_all()
        create_default_admin()

    from .routes.marketing import marketing_bp
    app.register_blueprint(marketing_bp)

    from .routes.sales import sales_bp
    app.register_blueprint(sales_bp)

    from .routes.admin import admin_bp
    app.register_blueprint(admin_bp)



    return app