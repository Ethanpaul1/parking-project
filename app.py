from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

# 1. Instantiate the global extensions (unbound)
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    
    # 2. Configure a local development SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parking.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # 3. Bind the extensions to this specific application instance
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    
    # 4. Import models package here so Flask-Migrate tracks them automatically
    import models

    # Core base entry route
    @app.route('/')
    def index():
        return {"status": "Parking API is running"}
        
    return app
