from flask import Flask
from flask_security import Security, SQLAlchemySessionUserDatastore
from myapp.db import db
from myapp.models import User, Role

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///g4g.sqlite3'
    app.config['SECRET_KEY'] = 'MY_SECRET'
    app.config['SECURITY_PASSWORD_SALT'] = 'some_salt'

    db.init_app(app)

    user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
    Security(app, user_datastore)

    with app.app_context():
        db.create_all()

    # ✅ Register your blueprint
    from myapp.routes import main_bp
    app.register_blueprint(main_bp)

    return app
