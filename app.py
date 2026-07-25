import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# Initialize global extension instances
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)

    # Configuration
    db_path = os.path.join(basedir, 'parking.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'dev-assignment-key-123'

    # Bind extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    # Import models at function scope so SQLAlchemy registers the classes
    # to db.Model.metadata BEFORE Alembic inspects them.
    import models

    # Register Blueprints
    from controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)

    @app.route('/')
    def index():
        return {"status": "Parking API is running"}

    return app