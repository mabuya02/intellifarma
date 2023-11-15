from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_mail import Mail

# Initialize Flask App
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Flask-SQLAlchemy
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)
mail = Mail(app) 
# Import and Register Blueprints
# Example: from .routes import auth_blueprint
#          app.register_blueprint(auth_blueprint, url_prefix='/auth')

# Import and Configure Extensions
# Example: from flask_cors import CORS
#          CORS(app)

# Other Configurations and Initializations
# Example: app.secret_key = 'your_secret_key'

# Create a Function to Initialize the App (for use in run.py)
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and Register Blueprints
    # Example: from .routes import auth_blueprint
    #          app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # Import and Configure Extensions
    # Example: from flask_cors import CORS
    #          CORS(app)

    # Other Configurations and Initializations
    # Example: app.secret_key = 'your_secret_key'

    return app
