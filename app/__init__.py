from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_restful import Api
from flask_mail import Mail


db = SQLAlchemy()
migrate = Migrate()
api = Api()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    mail.init_app(app)

    from app.routes import main,soil_parameters_bp,logout_user_bp,all_reviews_bp,user_activation_bp,user_review_bp

    # Register the Blueprint with the Flask app
    app.register_blueprint(main)
    app.register_blueprint(soil_parameters_bp) 
    app.register_blueprint(logout_user_bp)
    app.register_blueprint(user_activation_bp)
    app.register_blueprint(user_review_bp)
    app.register_blueprint(all_reviews_bp, name='all_reviews')
    
    
    
    return app