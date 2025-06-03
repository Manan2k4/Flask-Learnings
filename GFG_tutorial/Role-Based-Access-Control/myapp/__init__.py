from flask import Flask
from flask_security import Security, SQLAlchemySessionUserDatastore
from myapp.db import db
from myapp.models import User, Role

import os

def create_app():
    template_path = os.path.join(os.path.dirname(__file__), 'templates')
    app = Flask(__name__, template_folder=template_path)   
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///g4g.sqlite3'
    app.config['SECRET_KEY'] = 'MY_SECRET'
    app.config['SECURITY_PASSWORD_SALT'] = 'some_salt'

    db.init_app(app)

    user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
    Security(app, user_datastore)

    with app.app_context():
        db.create_all()

    # Register blueprints
    from myapp.routes import main_bp
    from myapp.auth import bp as auth_bp
    from myapp.views import admin_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)

    return app