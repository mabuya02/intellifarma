from flask import Flask
from flask_migrate import Migrate
from .routes import main_bp
from app.database import db
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)

    # Load environment variables from .env
    load_dotenv()

    # Database configuration
    DB_USERNAME = os.getenv('DB_USERNAME', 'default_username')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'default_password')
    DB_NAME = os.getenv('DB_NAME', 'default_database_name')

    if not all([DB_USERNAME, DB_NAME]):
        raise ValueError("Database configuration is incomplete.")

    # Configure the app
    app.config.from_pyfile('config.py')

    # Initialize database and migration
    db.init_app(app)
    migrate = Migrate(app, db)

    # Register blueprints
    app.register_blueprint(main_bp)

    print("App created successfully!")
    return app
