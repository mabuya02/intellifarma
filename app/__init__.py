from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_restful import Api

db = SQLAlchemy()
migrate = Migrate()
api = Api()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    from app.routes import main,soil_parameters_bp,user_review_bp

    # Register the Blueprint with the Flask app
    app.register_blueprint(main)
    app.register_blueprint(soil_parameters_bp) 
    app.register_blueprint(user_review_bp)
    
 
   

    return app
